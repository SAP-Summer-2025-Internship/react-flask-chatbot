# ApiDocumentsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**document_id** | **int** |  | [optional] 
**chunks_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.api_documents_post200_response import ApiDocumentsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsPost200Response from a JSON string
api_documents_post200_response_instance = ApiDocumentsPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsPost200Response.to_json())

# convert the object into a dict
api_documents_post200_response_dict = api_documents_post200_response_instance.to_dict()
# create an instance of ApiDocumentsPost200Response from a dict
api_documents_post200_response_from_dict = ApiDocumentsPost200Response.from_dict(api_documents_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


