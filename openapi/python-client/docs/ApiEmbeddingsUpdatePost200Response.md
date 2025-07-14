# ApiEmbeddingsUpdatePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**total_chunks** | **int** |  | [optional] 
**embedded_chunks** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.api_embeddings_update_post200_response import ApiEmbeddingsUpdatePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEmbeddingsUpdatePost200Response from a JSON string
api_embeddings_update_post200_response_instance = ApiEmbeddingsUpdatePost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiEmbeddingsUpdatePost200Response.to_json())

# convert the object into a dict
api_embeddings_update_post200_response_dict = api_embeddings_update_post200_response_instance.to_dict()
# create an instance of ApiEmbeddingsUpdatePost200Response from a dict
api_embeddings_update_post200_response_from_dict = ApiEmbeddingsUpdatePost200Response.from_dict(api_embeddings_update_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


