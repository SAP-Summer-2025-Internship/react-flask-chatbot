# ApiChatPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** |  | [optional] 
**used_rag** | **bool** |  | [optional] 
**context_found** | **bool** |  | [optional] 
**context** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_chat_post200_response import ApiChatPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiChatPost200Response from a JSON string
api_chat_post200_response_instance = ApiChatPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiChatPost200Response.to_json())

# convert the object into a dict
api_chat_post200_response_dict = api_chat_post200_response_instance.to_dict()
# create an instance of ApiChatPost200Response from a dict
api_chat_post200_response_from_dict = ApiChatPost200Response.from_dict(api_chat_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


