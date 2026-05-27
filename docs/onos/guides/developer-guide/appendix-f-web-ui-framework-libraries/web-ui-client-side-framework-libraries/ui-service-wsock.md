# UI Service - WSock

# WSock - WebSocket

WSock is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Remote module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `wsock.js`. This service was added as a wrapper for creating WebSockets specifically so that they could be mocked during unit tests. To use this function, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `newWebSocket` | Creates a new Javascript WebSocket. |

# Function Description

## newWebSocket

Creates a new Javascript WebSocket.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wsock.newWebSocket(`url`); | `url` - url for the new [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications) to connect to | the WebSocket object |
