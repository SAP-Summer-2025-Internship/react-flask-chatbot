# Frontend Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm install
COPY . .
EXPOSE 3000
ENV HOST 0.0.0.0
CMD ["npm", "start"]
