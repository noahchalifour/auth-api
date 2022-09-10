# auth.ClientsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientsApi.md#create_client) | **POST** /clients/ | 
[**destroy_client**](ClientsApi.md#destroy_client) | **DELETE** /clients/{id}/ | 
[**list_clients**](ClientsApi.md#list_clients) | **GET** /clients/ | 
[**partial_update_client**](ClientsApi.md#partial_update_client) | **PATCH** /clients/{id}/ | 
[**retrieve_client**](ClientsApi.md#retrieve_client) | **GET** /clients/{id}/ | 
[**update_client**](ClientsApi.md#update_client) | **PUT** /clients/{id}/ | 


# **create_client**
> CreateClient create_client()





### Example


```python
import time
import auth
from auth.api import clients_api
from auth.model.create_client import CreateClient
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auth.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = clients_api.ClientsApi(api_client)
    create_client = CreateClient(
        name="name_example",
        description="description_example",
    ) # CreateClient |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_client(create_client=create_client)
        pprint(api_response)
    except auth.ApiException as e:
        print("Exception when calling ClientsApi->create_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client** | [**CreateClient**](CreateClient.md)|  | [optional]

### Return type

[**CreateClient**](CreateClient.md)

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

# **destroy_client**
> destroy_client(id)





### Example


```python
import time
import auth
from auth.api import clients_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auth.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = clients_api.ClientsApi(api_client)
    id = "id_example" # str | A UUID string identifying this client.

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_client(id)
    except auth.ApiException as e:
        print("Exception when calling ClientsApi->destroy_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this client. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients**
> [Client] list_clients()





### Example


```python
import time
import auth
from auth.api import clients_api
from auth.model.client import Client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auth.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = clients_api.ClientsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_clients()
        pprint(api_response)
    except auth.ApiException as e:
        print("Exception when calling ClientsApi->list_clients: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Client]**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_client**
> Client partial_update_client(id)





### Example


```python
import time
import auth
from auth.api import clients_api
from auth.model.client import Client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auth.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = clients_api.ClientsApi(api_client)
    id = "id_example" # str | A UUID string identifying this client.
    client = Client(
        name="name_example",
        description="description_example",
        services={},
    ) # Client |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.partial_update_client(id)
        pprint(api_response)
    except auth.ApiException as e:
        print("Exception when calling ClientsApi->partial_update_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.partial_update_client(id, client=client)
        pprint(api_response)
    except auth.ApiException as e:
        print("Exception when calling ClientsApi->partial_update_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this client. |
 **client** | [**Client**](Client.md)|  | [optional]

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_client**
> Client retrieve_client(id)





### Example


```python
import time
import auth
from auth.api import clients_api
from auth.model.client import Client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auth.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = clients_api.ClientsApi(api_client)
    id = "id_example" # str | A UUID string identifying this client.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_client(id)
        pprint(api_response)
    except auth.ApiException as e:
        print("Exception when calling ClientsApi->retrieve_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this client. |

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> Client update_client(id)





### Example


```python
import time
import auth
from auth.api import clients_api
from auth.model.client import Client
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = auth.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with auth.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = clients_api.ClientsApi(api_client)
    id = "id_example" # str | A UUID string identifying this client.
    client = Client(
        name="name_example",
        description="description_example",
        services={},
    ) # Client |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_client(id)
        pprint(api_response)
    except auth.ApiException as e:
        print("Exception when calling ClientsApi->update_client: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_client(id, client=client)
        pprint(api_response)
    except auth.ApiException as e:
        print("Exception when calling ClientsApi->update_client: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this client. |
 **client** | [**Client**](Client.md)|  | [optional]

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

