# UI Service - TableBuilderService

# TableBuilderService

TableBuilder is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Widget module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `tableBuilder.js`. It provides a function that builds a generic model for [tabular views](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-tabular-view.md). To use this service, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `buildTable` | Creates the model for a [basic tabular view](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-tabular-view.md). |

# Function Descriptions

## buildTable

This function was made in order to reuse the code that all tabular views share – websocket calls, autorefresh, and selecting rows. It has side effects which are listed below.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| tbs.buildTable(`o`); | `o` - an object with settings to create the tabular view, see below | none |

### Object Arguments

```
tbs.buildTable({
	scope: $scope,            // required
	tag: 'foo',               // required
	selCb: selectCallback,    // optional
	respCb: responseCallback, // optional
	query: params             // optional
});
```

| Name of Property | Value of Property | Purpose |
| --- | --- | --- |
| scope \*\* | injected Angular [$scope](https://docs.angularjs.org/api/ng/type/$rootScope.Scope) service | buildTable attaches several functions and variables to the $scope that can be accessed from the table's controller and in the HTML |
| tag \*\* | string of what view this is, examples being "device", "link", or "app" | ***This must be singular – no 's' at the end!*** buildTable uses this to build the strings for websocket calls and naming the root node of received data. |
| selCb | function reference of a function you want to be called when a table row is selected | Stands for "select callback". This function is called when a table row is clicked on. |
| respCb | function reference of a function you want to be called when the table data is received from the server | Stands for "response callback". This function is called when the table data is received from the server. |
| query | object with query parameters (usually gotten from $location.search()) | Sends these query parameters to the server. For example, this is used in the [Flow View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-flow-view.md) to filter flows by a certain device ID. |

\*\* These properties are required for buildTable to work properly.

### Side Effects

The buildTable function puts several variables and functions on the scope to be used in controllers and directives. Here is a summary.

| $scope Property | Type | Summary |
| --- | --- | --- |
| `tableData` | array | Array of objects that model the data displayed in the table. |
| `changedData` | array | Array of objects that are new or have changed between the previous tableData and the new tableData just received. |
| `sortParams` | object | Current sort parameters – the column (`sortCol`) and sort direction (`sortDir`). |
| `loading` | boolean | True if the page is loading for the first time, or if it is taking longer than 500ms to get a response from the server. |
| `autoRefresh` | boolean | True if auto refresh is toggled "on", false otherwise. |
| `autoRefreshTip` | string | Message for the [tooltip directive](ui-service-tooltipservice.md) for the auto refresh button. |
| `sortCallback` | function reference | Function that sends the websocket request for the `tableData`.  (takes one optional argument that is an object of the sort parameters) |
| `selId` | string or `null` | ID of the currently selected item or `null` if nothing is selected. |
| `selectCallback` | function reference | Function that sets `selId` and calls user-given selCb if given. |
| `toggleRefresh` | function reference | Function that toggles auto refresh on and off. |
