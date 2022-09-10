# auth.InitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_init**](InitApi.md#create_init) | **POST** /init/ | 


# **create_init**
> bool, date, datetime, dict, float, int, list, str, none_type create_init()





### Example


```python
import time
import auth
from auth.api import init_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auth.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = init_api.InitApi(api_client)
    body = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_init(body=body)
        pprint(api_response)
    except auth.ApiException as e:
        print("Exception when calling InitApi->create_init: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

