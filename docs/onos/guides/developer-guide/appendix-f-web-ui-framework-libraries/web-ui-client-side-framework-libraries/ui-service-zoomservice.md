# UI Service - ZoomService

# ZoomService

ZoomService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [SVG module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `zoom.js`. It creates an API (based on user settings) that allows the SVG [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md) layer (managed by [d3](https://github.com/mbostock/d3)) to zoom in and out. To use this API, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `createZoomer` | Creates the ability to zoom on the given SVG layer and returns an API to control the zoom. |

# Function Descriptions

## createZoomer

Creates the ability to zoom on the given SVG layer and returns an API to control the zoom.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| var zoomer = zs.createZoomer(`opts`); | `opts` - an object containing:  svg: <d3 selection of svg element>  zoomLayer: <d3 selection of g element, child of svg element>  zoomEnabled: (optional) function reference that returns truthy values when zoom should be enabled and falsy values otherwise  zoomCallback: (optional) function reference to be called when the layer is zoomed | an object containing an API, see below |
| Returned API Example Usage | Arguments | Return Value |
| zoomer.panZoom(`translate`, `scale`); | `translate` - an array which is the zoom translation vector that you want to translate to  `scale` - a Number which is the scale that you want to zoom in to | none, but the view will be zoomed |
| zoomer.reset(); | none | none, but resets the pan and zoom levels back to default |
| zoomer.translate(); | none | the [current translation vector](https://github.com/mbostock/d3/wiki/Zoom-Behavior) |
| zoomer.scale(); | none | the [current zoom scale](https://github.com/mbostock/d3/wiki/Zoom-Behavior) |
| zoomer.scaleExtent(); | none | the [current zoom scale's range](https://github.com/mbostock/d3/wiki/Zoom-Behavior) |
