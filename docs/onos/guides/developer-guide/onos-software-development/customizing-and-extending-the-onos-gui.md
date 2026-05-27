# Customizing and Extending the ONOS GUI

# Overview

The ONOS Web GUI has been designed to facilitate the runtime injection of additional content by ONOS applications. There are two possible approaches:

* Register a "UI Extension" that adds one or more custom views  
  + See the [Custom View tutorial](../../../tutorials/web-ui-tutorials/web-ui-tutorial-creating-a-custom-view.md)
  + See the [Tabular View tutorial](../../../tutorials/web-ui-tutorials/web-ui-tutorial-creating-a-tabular-view.md)
* Register a "UI Extension" that adds a "Topology Overlay" component, augmenting the behavior of the Topology View
  + See the [Topology Overlay tutorial](../../../tutorials/web-ui-tutorials/web-ui-tutorial-creating-a-topology-overlay.md)
* Register a 'UI Extension' that adds a "Topology Map" asset to the Topology View
  + See the [Add Maps Tutorial](../../../tutorials/web-ui-tutorials/web-ui-tutorials-add-maps-tutorial.md)

As much as possible, reusable code has been made available to the developer, both for client-side code (JavaScript) and server-side code (Java).

## Client-side Framework Libraries

Many useful framework modules are available to use in JavaScript. See the [Web UI - Client side framework libraries](../appendix-f-web-ui-framework-libraries/web-ui-client-side-framework-libraries.md) page for details.

## Server-side Model and Utility Classes

A number of helper classes are available to use in server-side code. See the [Web UI - Server side helper classes](../appendix-f-web-ui-framework-libraries/web-ui-server-side-helper-classes.md) page for details.

# Further Topics

to be documented

* Some notes on conventions and assumptions
* Websocket communication
* Defining key-bindings
* Creating and using "fly-in" panels
* [Defining custom "glyphs"](../../../tutorials/web-ui-tutorials/ui-view-defining-a-custom-glyph.md)
