# UI Service - UrlFnService

# UrlFnService - URL Function Service

UrlFnService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Remote module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `urlfn.js`. It provides functions that build rest and websocket URLs for rest and websocket requests. To use these functions, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `rsUrl` | Construct a URL for rest calls. |
| `wsUrl` | Construct a URL for websocket calls. |

# Function Descriptions

## rsUrl

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ufs.rsUrl(`path`); | `path` - string of the path you want the rest call to send a request to | a string of the form:  *http[s]://<HOST>:<PORT>/onos/ui/rs/`path`*  *[s] – if applicable* |

## wsUrl

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ufs.wsUrl(`path`, `wsport`, `host`); | `path` - string of the path you want the websocket call to send a request to  `wsport` - the websocket port (`undefined` will use the current port)  `host` - the websocket host (`undefined` will use the current host) | a string of the form:  *ws[s]://**`host`**:**`port`**/onos/ui/websock/`path`*  [s] – if applicable |
