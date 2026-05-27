# Web UI Tutorials

**Important!**

This guide is mostly concerned with the legacy ONOS GUI (GUI1 - based on [AngularJS](#) - the obsolete version 1.x of Angular). The code for this is under **onos/web/gui**

It does not cover ONOS GUI2 (based on [Angular](https://angular.io/) 7+ - the replacement).

GUI2 replaces only the front end (Javascript side of the GUI) - the Java backend for the 2 are the same.

For GUI2 it is recommended to follow the [Template Application Tutorial](template-application-tutorial.md) and use the **ui2** archetype at [onos/tools/package/archetypes/ui2](https://github.com/opennetworkinglab/onos/tree/master/tools/package/archetypes/ui2)

The archetype supports only creating a Custom View. This can be changed to a Tabular view by following the design of any tabular view e.g. [Device View](https://github.com/opennetworkinglab/onos/tree/master/web/gui2/src/main/webapp/app/view/device). Topology overlays are not supported yet in GUI2

For GUI2 the main code is under:

* **[onos/web/gui2-fw-lib](https://github.com/opennetworkinglab/onos/tree/master/web/gui2-fw-lib)** - the GUI framework utility components and classes
* **[onos/web/gui2-topo-lib](https://github.com/opennetworkinglab/onos/tree/master/web/gui2-topo-lib)** - the Topology view
* **[onos/web/gui2](https://github.com/opennetworkinglab/onos/tree/master/web/gui2)** - the main GUI2 application

The text below is not modified for GUI2 and remains as it was for legacy GUI.

It is possible to run GUI1 or GUI2 on ONOS - GUI2 is the default - change to GUI1 use "app deactivate gui2" and then "app activate gui".

---

There are a number of ways that your application can integrate new content into the ONOS Web GUI, as described below.

The following tutorials – using a fictitious company, *Meowster, Inc.* – show how each of these styles of content can be created. The tutorials build on each other, so it is recommended that you work through them in order.

* [Creating a Custom View](web-ui-tutorials/web-ui-tutorial-creating-a-custom-view.md)
* [Creating a Tabular View](web-ui-tutorials/web-ui-tutorial-creating-a-tabular-view.md)
* [Creating a Topology Overlay](web-ui-tutorials/web-ui-tutorial-creating-a-topology-overlay.md)

Also see the tutorial session presented at ONS 2016

* [ONOS Web UI – Designed for Extensibility](https://www.youtube.com/watch?v=rymQpbozlyk)

Further topics can be viewed in the Developer's Guide for [Customizing and Extending the ONOS GUI](../guides/developer-guide/onos-software-development/customizing-and-extending-the-onos-gui.md):

* *Websocket communication*
* *Defining key-bindings*
* *Creating and using "fly-in" panels*
* *Defining custom "glyphs"*
