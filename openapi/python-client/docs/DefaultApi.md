# openapi_client.DefaultApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_chat_post**](DefaultApi.md#api_chat_post) | **POST** /api/chat | Chat with LLM
[**api_documents_get**](DefaultApi.md#api_documents_get) | **GET** /api/documents | List all documents
[**api_documents_post**](DefaultApi.md#api_documents_post) | **POST** /api/documents | Add a new document
[**api_embeddings_update_post**](DefaultApi.md#api_embeddings_update_post) | **POST** /api/embeddings/update | Update all embeddings
[**api_health_get**](DefaultApi.md#api_health_get) | **GET** /api/health | Health check


# **api_chat_post**
> ApiChatPost200Response api_chat_post(api_chat_post_request)

Chat with LLM

### Example


```python
import openapi_client
from openapi_client.models.api_chat_post200_response import ApiChatPost200Response
from openapi_client.models.api_chat_post_request import ApiChatPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    api_chat_post_request = openapi_client.ApiChatPostRequest() # ApiChatPostRequest | 

    try:
        # Chat with LLM
        api_response = api_instance.api_chat_post(api_chat_post_request)
        print("The response of DefaultApi->api_chat_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_chat_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_chat_post_request** | [**ApiChatPostRequest**](ApiChatPostRequest.md)|  | 

### Return type

[**ApiChatPost200Response**](ApiChatPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LLM response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_documents_get**
> ApiDocumentsGet200Response api_documents_get()

List all documents

### Example


```python
import openapi_client
from openapi_client.models.api_documents_get200_response import ApiDocumentsGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # List all documents
        api_response = api_instance.api_documents_get()
        print("The response of DefaultApi->api_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_documents_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiDocumentsGet200Response**](ApiDocumentsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of documents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_documents_post**
> ApiDocumentsPost200Response api_documents_post(api_documents_post_request)

Add a new document

### Example


```python
import openapi_client
from openapi_client.models.api_documents_post200_response import ApiDocumentsPost200Response
from openapi_client.models.api_documents_post_request import ApiDocumentsPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    api_documents_post_request = openapi_client.ApiDocumentsPostRequest() # ApiDocumentsPostRequest | 

    try:
        # Add a new document
        api_response = api_instance.api_documents_post(api_documents_post_request)
        print("The response of DefaultApi->api_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_documents_post_request** | [**ApiDocumentsPostRequest**](ApiDocumentsPostRequest.md)|  | 

### Return type

[**ApiDocumentsPost200Response**](ApiDocumentsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document added |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_embeddings_update_post**
> ApiEmbeddingsUpdatePost200Response api_embeddings_update_post()

Update all embeddings

### Example


```python
import openapi_client
from openapi_client.models.api_embeddings_update_post200_response import ApiEmbeddingsUpdatePost200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Update all embeddings
        api_response = api_instance.api_embeddings_update_post()
        print("The response of DefaultApi->api_embeddings_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_embeddings_update_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiEmbeddingsUpdatePost200Response**](ApiEmbeddingsUpdatePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Embeddings updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_health_get**
> ApiHealthGet200Response api_health_get()

Health check

### Example


```python
import openapi_client
from openapi_client.models.api_health_get200_response import ApiHealthGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Health check
        api_response = api_instance.api_health_get()
        print("The response of DefaultApi->api_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiHealthGet200Response**](ApiHealthGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

