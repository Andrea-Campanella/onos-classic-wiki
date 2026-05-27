# UI Service - GeoDataService

# GeoDataService

GeoDataService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [SVG module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `geodata.js`. It provides an API to fetch and cache [TopoJSON](https://github.com/mbostock/topojson/wiki) data from the server, as well as providing a way of creating a path generator for the data to be used to render the map in an SVG layer. To use this API, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `clearCache` | Clear the cache for [TopoJSON](https://github.com/mbostock/topojson/wiki) data. |
| `fetchTopoData` | Get TopoData via a [$http](https://docs.angularjs.org/api/ng/service/$http) request. |
| `createPathGenerator` | Converts given [TopoJSON](https://github.com/mbostock/topojson/wiki) format data into corresponding GeoJSON data and creates a path generator for it. |
| `rescaleProjection` | Adjust projection scale and translation to fill the view with the map. |

# Function Descriptions

## clearCache

Clear the cache for [TopoJSON](https://github.com/mbostock/topojson/wiki) data.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| gds.clearCache(); | none | none, but clears the cache |

## fetchTopoData

Get TopoData via a [$http](https://docs.angularjs.org/api/ng/service/$http) request.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| var promise = gds.fetchTopoData(`id`); | **`id`** - string of the name of the TopoJSON map, or the URL of where the TopoJSON is   * IDs that start with an asterisk (\*) identify maps bundled with the ONOS GUI. * IDs that do not start with an asterisk are assumed to be URLs to externally provided data. | an [$http](https://docs.angularjs.org/api/ng/service/$http) promise object with the following extra members:  meta: an object with members id (given), url (used to get the data), and wasCached (boolean)  topodata: [TopoJSON](https://github.com/mbostock/topojson/wiki) data upon response from server |

## createPathGenerator

Converts given [TopoJSON](https://github.com/mbostock/topojson/wiki) format data into corresponding GeoJSON data and creates a path generator for it.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| var pathGen = gds.createPathGnerator(`topoData`, `opts`); | `topoData` - the topodata from the returned [fetchTopoData](#UIServiceGeoDataService-fetchTopoData) promise object  `opts` - object that allows the override of default settings (see below) | an object with the following members:  geodata: [d3 feature data](https://github.com/mbostock/topojson/wiki/API-Reference)  pathgen: [d3 geo path projection](https://github.com/mbostock/d3/wiki/Geo-Paths)  settings: the settings object used to create the map |

### Default Settings

These can be overwritten in `opts`.

```
var defaultGenSettings = {
    objectTag: 'states',                  // the top level member under "objects" tag in TopoJSON
    projection: d3.geo.mercator(),        // type of geo projection, see https://github.com/mbostock/d3/wiki/Geo-Projections
    logicalSize: 1000,                    // logical size of the projection
    mapFillScale: .95                     // how large the map fills the area
};
```

## rescaleProjection

Adjust projection scale and translation to fill the view with the map.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| gds.rescaleProjection(**`proj`**, **`mfs`**, `dim`, `path`, `geoData`); | see `defaultGenSettings` from above  `proj` - the projection for the map  `mfs` - map fill scale  `dim` - logical size  `path` - the path projection  `geoData` - the TopoJSON feature data | none, but scales and translates the map to fit in the space |
