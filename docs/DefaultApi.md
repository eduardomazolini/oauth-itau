# oauth_itau.DefaultApi

All URIs are relative to *https://sts.itau.com.br/sandbox/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postoauthtoken**](DefaultApi.md#postoauthtoken) | **POST** /oauth/token | post /oauth/token


# **postoauthtoken**
> OauthCred postoauthtoken(client_id=client_id, client_secret=client_secret, grant_type=grant_type, scope=scope)

post /oauth/token

Operação responsável por recuperar o tokem de acesso

### Example
```python
from __future__ import print_function
import time
import oauth_itau
from oauth_itau.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oauth_itau.DefaultApi()
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)
grant_type = 'client_credentials' # str |  (optional) (default to client_credentials)
scope = 'scope' # str |  (optional) (default to scope)

try:
    # post /oauth/token
    api_response = api_instance.postoauthtoken(client_id=client_id, client_secret=client_secret, grant_type=grant_type, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->postoauthtoken: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 
 **grant_type** | **str**|  | [optional] [default to client_credentials]
 **scope** | **str**|  | [optional] [default to scope]

### Return type

[**OauthCred**](OauthCred.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

