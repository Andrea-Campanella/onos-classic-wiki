# UI Service - MapService

# MapService

MapService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [SVG module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `map.js`. It provides an API to load geographical maps into SVG layers. To use this API, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `loadMapRegionInto` | Searches for a map in a large datafile and loads a specific map region into to the SVG layer. |
| `loadMapInto` | Load a map region into the SVG layer. |

# Function Descriptions

## loadMapRegionInto

Searches for a map in a large datafile and loads a specific map region into to the SVG layer. This assumes the map file you are providing has multiple maps in it.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| var promise = ms.loadMapRegionInto(`mapLayer`, `filterOpts`);    Example:  `var promise = loadMapRegionInto(svgGroup, {  countryFilter: function (country) {  return country.properties.continent === 'South America';  } });` | `mapLayer` - [d3 selection](https://github.com/mbostock/d3/wiki/Selections) of an SVG <g> element to load the map into  `filterOpts` - an object with a member called 'countryFilter'  'countryFilter': function reference that is a filter function to find the country in the file | a promise to load (asynchronously) the geo-map-data-file |

## loadMapInto

Load a map region into the SVG layer. This assumes the map file you are providing only has one map in it.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ms.loadMapInto(`mapLayer`, `id`, `opts`); | `mapLayer` - [d3 selection](https://github.com/mbostock/d3/wiki/Selections) of an SVG <g> element to load the map into  `id` - the ID used in [fetchTopoData](ui-service-geodataservice.md)  `opts` - the opts used in [createPathGenerator](ui-service-geodataservice.md) | a promise to load (asynchronously) the geo-map-data-file |
