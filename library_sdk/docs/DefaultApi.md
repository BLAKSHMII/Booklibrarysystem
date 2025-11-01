# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_book_books_post**](DefaultApi.md#add_book_books_post) | **POST** /books/ | Add Book
[**cancel_reservation_reservations_reservation_id_delete**](DefaultApi.md#cancel_reservation_reservations_reservation_id_delete) | **DELETE** /reservations/{reservation_id} | Cancel Reservation
[**get_books_books_get**](DefaultApi.md#get_books_books_get) | **GET** /books/ | Get Books
[**reserve_book_books_book_id_reserve_post**](DefaultApi.md#reserve_book_books_book_id_reserve_post) | **POST** /books/{book_id}/reserve | Reserve Book


# **add_book_books_post**
> BookOut add_book_books_post(book_create)

Add Book

### Example


```python
import openapi_client
from openapi_client.models.book_create import BookCreate
from openapi_client.models.book_out import BookOut
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    book_create = openapi_client.BookCreate() # BookCreate | 

    try:
        # Add Book
        api_response = api_instance.add_book_books_post(book_create)
        print("The response of DefaultApi->add_book_books_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_book_books_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_create** | [**BookCreate**](BookCreate.md)|  | 

### Return type

[**BookOut**](BookOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_reservation_reservations_reservation_id_delete**
> object cancel_reservation_reservations_reservation_id_delete(reservation_id)

Cancel Reservation

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    reservation_id = 56 # int | 

    try:
        # Cancel Reservation
        api_response = api_instance.cancel_reservation_reservations_reservation_id_delete(reservation_id)
        print("The response of DefaultApi->cancel_reservation_reservations_reservation_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cancel_reservation_reservations_reservation_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_books_books_get**
> List[BookOut] get_books_books_get()

Get Books

### Example


```python
import openapi_client
from openapi_client.models.book_out import BookOut
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get Books
        api_response = api_instance.get_books_books_get()
        print("The response of DefaultApi->get_books_books_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_books_books_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BookOut]**](BookOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reserve_book_books_book_id_reserve_post**
> ReservationOut reserve_book_books_book_id_reserve_post(book_id, reservation_create)

Reserve Book

### Example


```python
import openapi_client
from openapi_client.models.reservation_create import ReservationCreate
from openapi_client.models.reservation_out import ReservationOut
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    book_id = 56 # int | 
    reservation_create = openapi_client.ReservationCreate() # ReservationCreate | 

    try:
        # Reserve Book
        api_response = api_instance.reserve_book_books_book_id_reserve_post(book_id, reservation_create)
        print("The response of DefaultApi->reserve_book_books_book_id_reserve_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->reserve_book_books_book_id_reserve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**|  | 
 **reservation_create** | [**ReservationCreate**](ReservationCreate.md)|  | 

### Return type

[**ReservationOut**](ReservationOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

