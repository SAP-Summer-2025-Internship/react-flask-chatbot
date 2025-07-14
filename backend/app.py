# -*- coding: utf-8 -*-
# backend/app.py
# Flask后端服务，提供与Ollama模型的API接口

from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import joinedload
import numpy as np
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'postgresql://postgres:password@postgres:5432/chatdb'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Document(db.Model):
    __tablename__ = 'documents'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'<Document {self.title}>'

class DocumentChunk(db.Model):
    __tablename__ = 'document_chunks'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    document_id = db.Column(db.Integer, db.ForeignKey('documents.id'), nullable=False)
    chunk_text = db.Column(db.Text, nullable=False)
    chunk_index = db.Column(db.Integer, nullable=False)
    embedding = db.Column(ARRAY(db.Float), nullable=True)
    document = db.relationship('Document', backref=db.backref('chunks', lazy=True))
    def __repr__(self):
        return f'<DocumentChunk {self.id}>'

def get_embeddings():
    return OllamaEmbeddings(
        model="bge-m3:latest",
        base_url="http://ollama:11434"
    )

def update_vector_store():
    try:
        chunks_without_embeddings = DocumentChunk.query.filter(
            DocumentChunk.embedding.is_(None)
        ).all()
        if not chunks_without_embeddings:
            logger.info("All chunks have embeddings, skipping update")
            return
        embeddings_model = get_embeddings()
        updated_count = 0
        for chunk in chunks_without_embeddings:
            try:
                embedding_vector = embeddings_model.embed_query(chunk.chunk_text)
                chunk.embedding = embedding_vector
                updated_count += 1
                logger.debug(f"Generated embedding for chunk {chunk.id}")
            except Exception as e:
                logger.error(f"Error generating embedding for chunk {chunk.id}: {str(e)}")
                continue
        if updated_count > 0:
            db.session.commit()
            logger.info(f"Updated embeddings for {updated_count} chunks")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating vector store: {str(e)}", exc_info=True)

def search_similar_chunks(query, k=3):
    try:
        embeddings_model = get_embeddings()
        query_embedding = embeddings_model.embed_query(query)
        chunks_with_embeddings = (DocumentChunk.query
                                 .options(joinedload(DocumentChunk.document))
                                 .filter(DocumentChunk.embedding.isnot(None))
                                 .all())
        if not chunks_with_embeddings:
            logger.warning("No chunks with embeddings found")
            return []
        similarities = []
        query_embedding_np = np.array(query_embedding)
        for chunk in chunks_with_embeddings:
            try:
                chunk_embedding = np.array(chunk.embedding)
                dot_product = np.dot(chunk_embedding, query_embedding_np)
                norm_chunk = np.linalg.norm(chunk_embedding)
                norm_query = np.linalg.norm(query_embedding_np)
                similarity = dot_product / (norm_chunk * norm_query) if norm_chunk != 0 and norm_query != 0 else 0.0
                similarities.append((chunk, similarity))
            except Exception as e:
                logger.warning(f"Error calculating similarity for chunk {chunk.id}: {str(e)}")
                continue
        similarities.sort(key=lambda x: x[1], reverse=True)
        top_chunks = similarities[:k]
        results = []
        for chunk, similarity in top_chunks:
            doc_obj = type('Document', (), {
                'page_content': chunk.chunk_text,
                'metadata': {
                    'document_id': chunk.document_id,
                    'chunk_id': chunk.id,
                    'chunk_index': chunk.chunk_index,
                    'title': chunk.document.title if chunk.document else '未知',
                    'similarity': similarity
                }
            })()
            results.append(doc_obj)
        logger.info(f"Found {len(results)} similar chunks for query: {query}")
        return results
    except Exception as e:
        logger.error(f"Error searching similar chunks: {str(e)}", exc_info=True)
        return []

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    use_rag = data.get('use_rag', True)
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    try:
        logger.debug(f"Processing chat request: {user_message}")
        llm = Ollama(model="deepseek-r1:1.5b", base_url="http://ollama:11434")
        context = ""
        context_found = False
        if use_rag:
            try:
                similar_docs = search_similar_chunks(user_message, k=3)
                if similar_docs:
                    context_parts = []
                    for doc in similar_docs:
                        context_parts.append(
                            f"文档：{doc.metadata.get('title', '未知')}\n"
                            f"内容：{doc.page_content}\n"
                            f"相似度：{doc.metadata.get('similarity', 0):.3f}"
                        )
                    context = "\n\n".join(context_parts)
                    context_found = True
                    logger.info(f"Found {len(similar_docs)} relevant documents")
                else:
                    logger.info("No relevant documents found")
            except Exception as e:
                logger.warning(f"RAG search failed: {str(e)}")
        if context:
            prompt = f"""基于以下文档内容回答用户问题：\n\n{context}\n\n用户问题：{user_message}\n\n请根据上述文档内容准确回答问题。如果文档中没有相关信息，请说明无法找到相关信息。"""
        else:
            prompt = user_message
        logger.debug(f"Sending prompt to model (RAG: {use_rag}, Context found: {context_found})")
        response = llm.invoke(prompt)
        logger.debug(f"Received response from model")
        return jsonify({
            "response": response,
            "used_rag": use_rag and context_found,
            "context_found": context_found,
            "context": context if context_found else None
        })
    except Exception as e:
        logger.error(f"Error with LLM: {str(e)}", exc_info=True)
        return jsonify({
            "error": f"Error communicating with LLM: {str(e)}"
        }), 500

@app.route('/api/documents', methods=['POST'])
def add_document():
    data = request.json
    title = data.get('title', '')
    content = data.get('content', '')
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    try:
        document = Document(title=title, content=content)
        db.session.add(document)
        db.session.commit()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = text_splitter.split_text(content)
        for i, chunk in enumerate(chunks):
            doc_chunk = DocumentChunk(
                document_id=document.id,
                chunk_text=chunk,
                chunk_index=i,
                embedding=None
            )
            db.session.add(doc_chunk)
        db.session.commit()
        logger.info(f"Added document '{title}' with {len(chunks)} chunks")
        try:
            update_vector_store()
        except Exception as e:
            logger.warning(f"Failed to generate embeddings immediately: {str(e)}")
        return jsonify({
            "message": "Document added successfully",
            "document_id": document.id,
            "chunks_count": len(chunks)
        })
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error adding document: {str(e)}", exc_info=True)
        return jsonify({"error": f"Error adding document: {str(e)}"}), 500

@app.route('/api/documents', methods=['GET'])
def list_documents():
    try:
        documents = Document.query.all()
        result = []
        for doc in documents:
            chunk_count = DocumentChunk.query.filter_by(document_id=doc.id).count()
            embedding_count = DocumentChunk.query.filter(
                DocumentChunk.document_id == doc.id,
                DocumentChunk.embedding.isnot(None)
            ).count()
            result.append({
                "id": doc.id,
                "title": doc.title,
                "content": doc.content[:200] + "..." if len(doc.content) > 200 else doc.content,
                "created_at": doc.created_at.isoformat(),
                "chunk_count": chunk_count,
                "embedding_count": embedding_count
            })
        return jsonify({"documents": result})
    except Exception as e:
        logger.error(f"Error listing documents: {str(e)}", exc_info=True)
        return jsonify({"error": f"Error listing documents: {str(e)}"}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    ollama_status = "disconnected"
    db_status = "disconnected"
    embedding_status = "disconnected"
    test_response = None
    errors = []
    try:
        llm = Ollama(model="deepseek-r1:1.5b", base_url="http://ollama:11434")
        test_response = llm.invoke("hello")
        ollama_status = "connected"
    except Exception as e:
        errors.append(f"Ollama: {str(e)}")
    try:
        with db.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        errors.append(f"Database: {str(e)}")
    try:
        embeddings_model = get_embeddings()
        test_embedding = embeddings_model.embed_query("test")
        if test_embedding:
            embedding_status = "connected"
    except Exception as e:
        errors.append(f"Embeddings: {str(e)}")
    doc_count = 0
    chunk_count = 0
    embedding_count = 0
    try:
        doc_count = Document.query.count()
        chunk_count = DocumentChunk.query.count()
        embedding_count = DocumentChunk.query.filter(
            DocumentChunk.embedding.isnot(None)
        ).count()
    except Exception as e:
        errors.append(f"Data query: {str(e)}")
    if ollama_status == "connected" and db_status == "connected" and embedding_status == "connected":
        status = "ok"
        status_code = 200
    else:
        status = "degraded"
        status_code = 207
    response_data = {
        "status": status,
        "ollama": ollama_status,
        "database": db_status,
        "embeddings": embedding_status,
        "data_counts": {
            "documents": doc_count,
            "chunks": chunk_count,
            "embeddings": embedding_count
        },
        "test_response": test_response,
        "errors": errors if errors else None
    }
    return jsonify(response_data), status_code

@app.route('/api/embeddings/update', methods=['POST'])
def update_embeddings():
    try:
        DocumentChunk.query.update({DocumentChunk.embedding: None})
        db.session.commit()
        update_vector_store()
        total_chunks = DocumentChunk.query.count()
        embedded_chunks = DocumentChunk.query.filter(
            DocumentChunk.embedding.isnot(None)
        ).count()
        return jsonify({
            "message": "Embeddings updated successfully",
            "total_chunks": total_chunks,
            "embedded_chunks": embedded_chunks
        })
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating embeddings: {str(e)}", exc_info=True)
        return jsonify({"error": f"Error updating embeddings: {str(e)}"}), 500

def init_db():
    try:
        with app.app_context():
            db.create_all()
            logger.info("Database tables created successfully")
            existing_doc = Document.query.filter_by(title="SAP2025暑期实习小组").first()
            if not existing_doc:
                logger.info("Adding SAP internship group data...")
                sap_doc = Document(
                    title="SAP2025暑期实习小组",
                    content="SAP2025暑期实习小组有三个人，男生leo和michael，女生zoe。这个小组是为了SAP公司2025年暑期实习项目而组建的团队，成员包括两名男性实习生leo和michael，以及一名女性实习生zoe。团队主要负责开发和测试SAP系统的新功能模块。"
                )
                db.session.add(sap_doc)
                db.session.commit()
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=50
                )
                chunks = text_splitter.split_text(sap_doc.content)
                for i, chunk in enumerate(chunks):
                    doc_chunk = DocumentChunk(
                        document_id=sap_doc.id,
                        chunk_text=chunk,
                        chunk_index=i,
                        embedding=None
                    )
                    db.session.add(doc_chunk)
                db.session.commit()
                logger.info(f"SAP internship group document added with {len(chunks)} chunks")
                try:
                    update_vector_store()
                    logger.info("Vector embeddings generated successfully")
                except Exception as e:
                    logger.warning(f"Failed to generate embeddings during initialization: {str(e)}")
            else:
                logger.info("SAP internship group data already exists")
            doc_count = Document.query.count()
            chunk_count = DocumentChunk.query.count()
            embedding_count = DocumentChunk.query.filter(
                DocumentChunk.embedding.isnot(None)
            ).count()
            logger.info(f"Database initialized: {doc_count} documents, {chunk_count} chunks, {embedding_count} embeddings")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}", exc_info=True)
        db.session.rollback()

if __name__ == '__main__':
    init_db()
    app.run(debug=False, host="0.0.0.0", port=5000)


