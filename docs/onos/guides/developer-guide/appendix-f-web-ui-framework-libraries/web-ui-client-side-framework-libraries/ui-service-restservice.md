# UI Service - RestService

# RestService

RestService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Remote module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `rest.js`. It provides functions to make RESTful calls to the server using the [$http](https://docs.angularjs.org/api/ng/service/$http) service. To use these functions, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `get` | Make a [RESTful GET](http://www.restapitutorial.com/lessons/httpmethods.html) request. |
| `post` | Make a [RESTful POST](http://www.restapitutorial.com/lessons/httpmethods.html) request. |

# Function Descriptions

## get

Make a [RESTful GET](http://www.restapitutorial.com/lessons/httpmethods.html) request.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| rs.get(`url`, `callback`, `errorCb`); | `url` - the path to be used in the rest call (see [UrlFnService](ui-service-urlfnservice.md) for path information)  `callback` - function reference to be executed upon success  `errorCb` - function reference to be executed upon error | none |

## post

Make a [RESTful POST](http://www.restapitutorial.com/lessons/httpmethods.html) request. *(This function is experimental.)*

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| rs.post(`url`, `data`, `callbacks`); | `url` - the path to be used in the rest call (see [UrlFnService](ui-service-urlfnservice.md)  for path information)  `data` - the data you want to POST to the server  `callbacks` - object containing:  success: <function reference to be executed on success>  error: <function reference to be executed on error> | none |
