# ApiHealthGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**ollama** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**embeddings** | **str** |  | [optional] 
**data_counts** | **object** |  | [optional] 
**test_response** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.api_health_get200_response import ApiHealthGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiHealthGet200Response from a JSON string
api_health_get200_response_instance = ApiHealthGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiHealthGet200Response.to_json())

# convert the object into a dict
api_health_get200_response_dict = api_health_get200_response_instance.to_dict()
# create an instance of ApiHealthGet200Response from a dict
api_health_get200_response_from_dict = ApiHealthGet200Response.from_dict(api_health_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


