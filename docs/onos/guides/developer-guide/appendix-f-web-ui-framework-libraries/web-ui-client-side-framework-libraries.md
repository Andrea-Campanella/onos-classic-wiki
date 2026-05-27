# Web UI - Client side framework libraries

# Overview

Most of the ONOS Web UI framework code is implemented as [Angular services](https://docs.angularjs.org/guide/services) ([factories, in fact](http://stackoverflow.com/questions/15666048/service-vs-provider-vs-factory)). This page provides a brief summary of these factories, with links to pages giving more detail.

The source code can be found in ***[web/gui/src/main/webapp/app/fw/](https://github.com/opennetworkinglab/onos/tree/master/web/gui/src/main/webapp/app/fw)***.

# Layer

The module holding these services is **`onosLayer`** defined in **`layer/layer.js`**.

| Service | Description |
| --- | --- |
| [FlashService](web-ui-client-side-framework-libraries/ui-service-flashservice.md) | Allows application code to flash transient messages on the screen. |
| [LoadingService](web-ui-client-side-framework-libraries/ui-service-loadingservice.md) | Provides the ONOS-branded "Loading..." animation. |
| [PanelService](web-ui-client-side-framework-libraries/ui-service-panelservice.md) | Provides an API to create and destroy "fly-in" panels. |
| [DialogService](web-ui-client-side-framework-libraries/ui-service-dialogservice.md) | Builds on the panel service to create a dialog panel. |
| [QuickHelpService](web-ui-client-side-framework-libraries/ui-service-quickhelpservice.md) | Renders the Quick Help panel. |
| [VeilService](web-ui-client-side-framework-libraries/ui-service-veilservice.md) | Manages an masking layer that appears when the web-socket connection fails. |

# Mast

The module holding these services is **`onosMast`** defined in **`mast/mast.js`**.

| Service | Description |
| --- | --- |
| [MastService](web-ui-client-side-framework-libraries/ui-service-mastservice.md) | Provides functions relating to the masthead. |

# Nav

The module holding these services is **`onosNav`** defined in **`nav/nav.js`**.

| Service | Description |
| --- | --- |
| [NavService](web-ui-client-side-framework-libraries/ui-service-navservice.md) | Manages the menu navigation pane. |

# Remote

The module holding these services is **`onosRemote`** defined in **`remote/remote.js`**.

| Service | Description |
| --- | --- |
| [RestService](web-ui-client-side-framework-libraries/ui-service-restservice.md) | Abstracts rest calls using the `$http` service. |
| [UrlFnService](web-ui-client-side-framework-libraries/ui-service-urlfnservice.md) | Creates URL strings for REST or web-socket calls. |
| [WebSocketService](web-ui-client-side-framework-libraries/ui-service-websocketservice.md) | Handles Websocket events (bind, unbind, listeners). |
| [WSock](web-ui-client-side-framework-libraries/ui-service-wsock.md) | Web-socket wrapper to facilitate unit-testing with mock web-sockets. |

# SVG

The module holding these services is **`onosSvg`** defined in **`svg/svg.js`**.

| Service | Description |
| --- | --- |
| [GeoDataService](web-ui-client-side-framework-libraries/ui-service-geodataservice.md) | Fetches and caches TopoJSON data, providing an API for creating a path generator for that data. |
| [GlyphService](web-ui-client-side-framework-libraries/ui-service-glyphservice.md) | Add, load, and register SVG symbols (glyphs). |
| [IconService](web-ui-client-side-framework-libraries/ui-service-iconservice.md) | Add, load, and register SVG icons via a service (abstraction of GlyphService) or a directive. |
| [MapService](web-ui-client-side-framework-libraries/ui-service-mapservice.md) | Loads graphical maps into the SVG layer. |
| [SvgUtilService](web-ui-client-side-framework-libraries/ui-service-svgutilservice.md) | General SVG utility functions. |
| [ZoomService](web-ui-client-side-framework-libraries/ui-service-zoomservice.md) | Creates a "zoomer" to manage zoom functions in an SVG layer. |

# Util

The module holding these services is **`onosUtil`** defined in **`util/util.js`**.

| Service | Description |
| --- | --- |
| [FnService](web-ui-client-side-framework-libraries/ui-service-fnservice.md) | Provides general purpose functions useful throughout the application. |
| [KeyService](web-ui-client-side-framework-libraries/ui-service-keyservice.md) | Provides key-bindings to function callbacks. |
| [PrefsService](web-ui-client-side-framework-libraries/ui-service-prefsservice.md) | Persists user settings in the browser's cookies. |
| [RandomService](web-ui-client-side-framework-libraries/ui-service-randomservice.md) | Encapsulated randomness. |
| [ThemeService](web-ui-client-side-framework-libraries/ui-service-themeservice.md) | Manages UI themes (*light* and *dark*). |

# Widget

The module holding these services is **`onosWidget`** defined in **`widget/widget.js`**.

| Service | Description |
| --- | --- |
| [ButtonService](web-ui-client-side-framework-libraries/ui-service-buttonservice.md) | Provides an API to create buttons, toggles, and radio button sets. |
| [Table Directives](web-ui-client-side-framework-libraries/ui-service-table-directives.md) | Defines Angular directives for [tabular views](../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-tabular-view.md). |
| [TableBuilderService](web-ui-client-side-framework-libraries/ui-service-tablebuilderservice.md) | Provides an API to create a generic table view client model. |
| [ToolbarService](web-ui-client-side-framework-libraries/ui-service-toolbarservice.md) | Provides an API to create a toolbar. |
| [TooltipService](web-ui-client-side-framework-libraries/ui-service-tooltipservice.md) | Provides an API and a directive to install tooltips. |
