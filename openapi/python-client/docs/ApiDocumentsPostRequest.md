# ApiDocumentsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_documents_post_request import ApiDocumentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsPostRequest from a JSON string
api_documents_post_request_instance = ApiDocumentsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsPostRequest.to_json())

# convert the object into a dict
api_documents_post_request_dict = api_documents_post_request_instance.to_dict()
# create an instance of ApiDocumentsPostRequest from a dict
api_documents_post_request_from_dict = ApiDocumentsPostRequest.from_dict(api_documents_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


