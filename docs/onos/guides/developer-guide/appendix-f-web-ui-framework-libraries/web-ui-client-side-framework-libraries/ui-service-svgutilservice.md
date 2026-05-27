# UI Service - SvgUtilService

# SvgUtilService - SVG Utility Service

SvgUtilService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [SVG module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `svgUtil.js`. It provides an API to manipulate SVG elements in Javascript. To use this API, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

## API Functions

| Name | Summary |
| --- | --- |
| `createDragBehavior` | Creates drag behavior for SVG nodes on the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md). |
| `loadGlowDefs` | Creates the SVG glow effect for links on the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md). |
| `cat7` | Returns an API to get the theme colors for the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md). |
| `translate` | Returns a string representing translation in SVG transform attribute syntax. |
| `scale` | Returns a string representing scaling in SVG transform attribute syntax. |
| `skewX` | Returns a string representing skewing in the X direction in SVG transform attribute syntax. |
| `rotate` | Returns a string representing rotation in SVG transform attribute syntax. |
| `stripPx` | Returns the string given but without 'px' on the end. |
| `safeId` | Returns a safe ID for nodes to use on the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md). |
| `visible` | Toggle an element's visibility or query an element's visibility. |

# Function Descriptions

## createDragBehavior

Creates drag behavior for SVG nodes on the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md).

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.createDragBehavior(`force`, `selectCb`, `atDragEnd`, `dragEnabled`, `clickEnabled`); | `force` - Topology View force layout object  `selectCb` - function reference to be executed at the end of the drag if click is enabled  `atDragEnd` - function reference to be executed on the end of the drag if drag is enabled  `dragEnabled` - function reference that returns a boolean of whether drag is enabled  `clickEnabled` - function reference that returns a boolean of whether click is enabled | [d3 drag behavior](https://github.com/mbostock/d3/wiki/Drag-Behavior) object |

## loadGlowDefs

Creates the SVG glow effect for links on the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md).

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.loadGlowDefs(`defs`); | `defs` - [d3 selection](https://github.com/mbostock/d3/wiki/Selections) of the [<defs> element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/defs) of an SVG | none, but defines a glow effect for links |

## cat7

Returns an API to get the theme colors for the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md).

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| var cat7 = sus.cat7(); | none | an object that contains an API, see below |
| Returned API Example Usage | Arguments | Return Value |
| cat7.testCard(`svg`); | `svg` - [d3 selection](https://github.com/mbostock/d3/wiki/Selections) of an SVG element | none, but creates a circle, rectangle, and text in a specific color scheme for color testing |
| cat7.getColor(`id`, `muted`, `theme`); | `id` - string of the ID the device master or ONOS instance  `muted` - truthy or falsy value of whether the colors should be muted  `theme` - string of the name of the current theme | [d3 scale ordinal range](https://github.com/mbostock/d3/wiki/Ordinal-Scales) for the chosen theme |

## translate

Returns a string representing translation in SVG transform attribute syntax.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.translate(`x`, `y`); | `x` - String or number representing the x translation amount  or  An array of length 2 with x[0] as the x translation amount and x[1] as the y translation amount  `y` - String or number representing the y translation amount  or  `undefined` | string representing the translation amount given that can be used in the SVG transform attribute  Ex:  'translate(2,3)' |

## scale

Returns a string representing scaling in SVG transform attribute syntax.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.scale(`x`, `y`); | `x` - String or number representing the x scale translation amount  `y` - String or number representing the y scale translation amount | string representing the scale amount given that can be used in the SVG transform attribute  Ex:  'scale(2,3)' |

## skewX

Returns a string representing skewing in the X direction in SVG transform attribute syntax.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.skewX(`x`); | `x` - String or number representing the skewX amount | string representing the skewX amount given that can be used in the SVG transform attribute  Ex:  'skewX(2)' |

## rotate

Returns a string representing rotation in SVG transform attribute syntax.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.rotate(`deg`); | `deg` - String or number representing the rotation amount in degrees | string representing the rotate amount given that can be used in the SVG transform attribute  Ex:  'rotate(90)' |

## stripPx

Returns the string given but without 'px' on the end. Usually this is a measurement in pixels.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.stripPx(`s`); | **`s`** - String ending with 'px' | `s` without 'px' at the end |

## safeId

Returns a safe ID for nodes to use on the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md).

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.safeId(`s`); | `s` - string device or host ID | string of a safe attribute ID. Safe IDs take the original string and replace unsafe characters with a '-', using the regular expression: `/[^a-z0-9]/gi` |

## visible

Toggle an element's visibility or query an element's visibility.

This function is both setter and getter.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| sus.isVisible(`el`,`b`); | `el` - [d3 selection](https://github.com/mbostock/d3/wiki/Selections) of an element  `b` - (optional) boolean of whether element should be visible or hidden | if `b` was `undefined`, will return boolean of `el`'s 'visibility' style equaling 'visible'  if `b` is truthy, `el`'s visibility style will be 'visible' otherwise 'hidden' |
