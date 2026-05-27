# UI Service - PrefsService

# PrefsService - Preferences Service

PrefsService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Util module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `prefs.js`. It provides an API to manage preferences using the [$cookies](https://docs.angularjs.org/api/ngCookies/service/$cookies) service. To use these functions, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `getPrefs` | Gets a cookie set with a specific name's value. |
| `asNumbers` | Converts string values to numbers for all or selected keys. |
| `setPrefs` | Sets the cookie preferences as a string into the cache. |

# Function Descriptions

## getPrefs

Gets a cookie set with a specific name's value.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ps.getPrefs(`name`); | `name` - string of the name of the cookie set that you want (an example being 'topo\_prefs') | an object representing the cookie set that you requested  `null` if no cookie for `name` exists |

## asNumbers

Converts string values to numbers for all or selected keys.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ps.asNumbers(`obj`, `keys`); | `obj` - cookie object that has string values representing numbers  `keys` - (optional) a set of keys in `obj` that you want their values to be converted to numbers. If this value is falsy, then all keys in `obj` will be converted to numbers. | **`obj`** with all (or specified **`keys`**) of its values converted from strings to numbers |

## setPrefs

Sets the cookie preferences as a string into the cache.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ps.setPrefs(`name`, `obj`); | `name` - string of the name of the cookie preferences  `obj` - object containing key value pairs for the cookie values. \* | none, but stores cookies |

\* Cookies for the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md) are stored as numbers 0 or 1 for [toggle button](ui-service-buttonservice.md) state.
