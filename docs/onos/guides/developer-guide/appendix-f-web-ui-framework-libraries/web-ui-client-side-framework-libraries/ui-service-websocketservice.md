# UI Service - WebSocketService

WebSocketService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Remote module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `websocket.js`. It provides functions to request and receive information from the server via the websocket. To use these functions, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `resetSid` | Resets the event sequence identifier back to 0. |
| `resetState` | Resets all internal variables back to their default value. |
| `createWebSocket` | Creates a new WebSocket with options. |
| `bindHandlers` | Binds functions to response messages. |
| `unbindHandlers` | Unbinds handlers for response messages. |
| `addOpenListener` | Bind a function to WebSocket open event. |
| `removeOpenListener` | Remove handler for WebSocket open event. |
| `sendEvent` | Creates an event message and sends it via the WebSocket. |

# Function Descriptions

## resetSid

Resets the event sequence identifier back to 0. *This function is only used in testing.*

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wss.resetSid(); | none | none |

## resetState

Resets all internal service variables back to their default value. *This function is only used in testing.*

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wss.resetState(); | none | none |

## createWebSocket

Creates a new WebSocket with options.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wss.createWebSocket(`opts`, `host`); | `opts` - an object containing:  wsport: a websocket port other than the default 8181  `host` - the host address to use, defaults to current host | the URL in which the websocket was opened |

## bindHandlers

Binds functions to response messages.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wss.bindHandlers(`handlerMap`); | `handlerMap` - an object containing:  <server response event name>: <function reference to execute on response> | none  `null` if **`handlerMap`** was falsy or an empty object |

## unbindHandlers

Unbinds handlers for response messages. This function is expected to be called when a view is destroyed.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wss.unbindHandlers(`handlerMap`); | `handlerMap` - the same object as was used to bindHandlers | none  `null` if **`handlerMap`** was falsy or an empty object |

## addOpenListener

Bind a function to WebSocket open event.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wss.addOpenListener(`callback`); | **`callback`** - function reference to be executed on WebSocket open | object containing:  id: this listener's ID  cb: **`callback`**  error: 'No callback defined' if there was an error |

## removeOpenListener

Remove handler for WebSocket open event.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wss.removeOpenListener(`lsnr`); | `lsnr` - the object returned from addOpenListener | none |

## sendEvent

Creates an event message and sends it via the WebSocket.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| wss.sendEvent(`evType`, `payload`); | `evType` - string of the event type to send to the server  `payload` - object containing the event's payload | none, but sends the event to the server |
