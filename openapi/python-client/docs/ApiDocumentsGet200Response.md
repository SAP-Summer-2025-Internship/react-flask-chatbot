# ApiDocumentsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[ApiDocumentsGet200ResponseDocumentsInner]**](ApiDocumentsGet200ResponseDocumentsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_documents_get200_response import ApiDocumentsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsGet200Response from a JSON string
api_documents_get200_response_instance = ApiDocumentsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsGet200Response.to_json())

# convert the object into a dict
api_documents_get200_response_dict = api_documents_get200_response_instance.to_dict()
# create an instance of ApiDocumentsGet200Response from a dict
api_documents_get200_response_from_dict = ApiDocumentsGet200Response.from_dict(api_documents_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


