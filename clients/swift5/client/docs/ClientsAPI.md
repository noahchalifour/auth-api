# ClientsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createClient**](ClientsAPI.md#createclient) | **POST** /clients/ | 
[**destroyClient**](ClientsAPI.md#destroyclient) | **DELETE** /clients/{id}/ | 
[**listClients**](ClientsAPI.md#listclients) | **GET** /clients/ | 
[**partialUpdateClient**](ClientsAPI.md#partialupdateclient) | **PATCH** /clients/{id}/ | 
[**retrieveClient**](ClientsAPI.md#retrieveclient) | **GET** /clients/{id}/ | 
[**updateClient**](ClientsAPI.md#updateclient) | **PUT** /clients/{id}/ | 


# **createClient**
```swift
    open class func createClient(createClient: CreateClient? = nil, completion: @escaping (_ data: CreateClient?, _ error: Error?) -> Void)
```





### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import Auth

let createClient = CreateClient(id: 123, secret: "secret_example", name: "name_example", description: "description_example", services: "TODO") // CreateClient |  (optional)

ClientsAPI.createClient(createClient: createClient) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createClient** | [**CreateClient**](CreateClient.md) |  | [optional] 

### Return type

[**CreateClient**](CreateClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroyClient**
```swift
    open class func destroyClient(id: String, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```





### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import Auth

let id = "id_example" // String | A UUID string identifying this client.

ClientsAPI.destroyClient(id: id) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String** | A UUID string identifying this client. | 

### Return type

Void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listClients**
```swift
    open class func listClients(completion: @escaping (_ data: [Client]?, _ error: Error?) -> Void)
```





### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import Auth


ClientsAPI.listClients() { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partialUpdateClient**
```swift
    open class func partialUpdateClient(id: String, client: Client? = nil, completion: @escaping (_ data: Client?, _ error: Error?) -> Void)
```





### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import Auth

let id = "id_example" // String | A UUID string identifying this client.
let client = Client(id: 123, name: "name_example", description: "description_example", services: "TODO", dateCreated: Date()) // Client |  (optional)

ClientsAPI.partialUpdateClient(id: id, client: client) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String** | A UUID string identifying this client. | 
 **client** | [**Client**](Client.md) |  | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveClient**
```swift
    open class func retrieveClient(id: String, completion: @escaping (_ data: Client?, _ error: Error?) -> Void)
```





### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import Auth

let id = "id_example" // String | A UUID string identifying this client.

ClientsAPI.retrieveClient(id: id) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String** | A UUID string identifying this client. | 

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateClient**
```swift
    open class func updateClient(id: String, client: Client? = nil, completion: @escaping (_ data: Client?, _ error: Error?) -> Void)
```





### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import Auth

let id = "id_example" // String | A UUID string identifying this client.
let client = Client(id: 123, name: "name_example", description: "description_example", services: "TODO", dateCreated: Date()) // Client |  (optional)

ClientsAPI.updateClient(id: id, client: client) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String** | A UUID string identifying this client. | 
 **client** | [**Client**](Client.md) |  | [optional] 

### Return type

[**Client**](Client.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

