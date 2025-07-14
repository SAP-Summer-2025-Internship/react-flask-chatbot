# ApiDocumentsGet200ResponseDocumentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**chunk_count** | **int** |  | [optional] 
**embedding_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.api_documents_get200_response_documents_inner import ApiDocumentsGet200ResponseDocumentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsGet200ResponseDocumentsInner from a JSON string
api_documents_get200_response_documents_inner_instance = ApiDocumentsGet200ResponseDocumentsInner.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsGet200ResponseDocumentsInner.to_json())

# convert the object into a dict
api_documents_get200_response_documents_inner_dict = api_documents_get200_response_documents_inner_instance.to_dict()
# create an instance of ApiDocumentsGet200ResponseDocumentsInner from a dict
api_documents_get200_response_documents_inner_from_dict = ApiDocumentsGet200ResponseDocumentsInner.from_dict(api_documents_get200_response_documents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


