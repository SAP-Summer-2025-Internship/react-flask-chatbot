# ApiChatPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**use_rag** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.api_chat_post_request import ApiChatPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiChatPostRequest from a JSON string
api_chat_post_request_instance = ApiChatPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiChatPostRequest.to_json())

# convert the object into a dict
api_chat_post_request_dict = api_chat_post_request_instance.to_dict()
# create an instance of ApiChatPostRequest from a dict
api_chat_post_request_from_dict = ApiChatPostRequest.from_dict(api_chat_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


