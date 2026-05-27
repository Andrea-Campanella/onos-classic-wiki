# GUI Release Notes

# ONOS GUI - Release Notes

This section provides a reverse-chronological summary of changes to the GUI for each release.

## Toucan - 2.3.0

Build system for GUI2 moved to Angular-Bazel Convergence, replacing Angular CLI

Moved GUI2 to Angular 9

Added Pipeconf view to GUI2

Added Yang GUI to GUI2

Upgraded the Alarm View on GUI2

## Sparrow 2.2.0

Moved GUI2 to Angular 8

Roadm GUI added to GUI2

Added GUI2 [documentation](../../../developer-guide/appendix-i-gui2-development.md)

## Raven - 2.1.0

Moved GUI2 to Angular 7

GUI2 Topology view completed

## Quail - 2.0.0

Made GUI and GUI2 in to OSGi applications - can be unloaded completely or either one

GUI2 was made the default GUI. Legacy GUI loadable through "app activate"

## Junco – 1.9.0

* Region-Aware Topology View:
  + Region transition animation added
  + Sprite layers added
* Partitions View added
* Table View Details Panel refactoring
* Support for Intent Viewing handled by currently active Topology view overlay

## Ibis – 1.8.0

* Region-Aware Topology View:
  + Configurations added for Regions and TopoLayers
* "Resubmit Intent" action added to Intents View
* Topology view icons updated
* Cluster View details panel added
* Local filtering added to Flow, Port, Group, and Meter views

## Hummingbird – 1.7.0

* Region-Aware Topology View:
  + Server-side modeling done
* "Brief" mode introduced to Intent, Group, and Flow views
* Continued work on re-theming UI

## Goldeneye – 1.6.0

* Overhaul of the "Look-n-Feel" (re-skinned).
* Applications View:
  + Drag-n-drop of .oar files to install and activate, now supported.
  + Auto-prompt user to refresh the UI when components are added/removed
* Topology View:
  + "Cluster node ready" checkmark indicator added.
  + Geo-map selection dialog ('G' keystroke) added.
  + Support for topology overlays to provide custom link data.
* Dialog Service
  + Support for chained dialog operations added.
* Chart Service added.
* User preferences now persisted server side.
* Logged-in user name displayed in masthead.

## Falcon – 1.5.0

* Topology View:
  + "Reset Node Locations" command ('X' keystroke) added.
  + Topology Overlay selection with F1, F2, F3... keystrokes added.
* Applications View
  + Confirmation dialog added for application activate/deactivate/uninstall.
  + Application model enhancements supported:
    - columns added for additional application attributes
    - details panel displayed when application row selected
  + Note: applications can now define custom icon and custom URL (link to documentation).
* Dialog Service:
  + Enter and Escape keys bound to OK and Cancel buttons.

## Emu – 1.4.0

* Device View:  
  + Friendly name can be set on a device from the device detail panel.
* Intent View:
  + Button added to navigate to Topology View and display the selected intent.
* Topology View:
  + Traffic Overlay now selected as default.
  + Topology overlays can now highlight devices and hosts with badges (small number/text/glyph).
  + Topology overlays can invoke a dialog box to interact with the user.
* ONOS-Branded ["Loading..." animation](../../../../../assets/demo-delayed-server-1.mp4).
* Sample application (*org.onosproject.uiref*) featuring UI content injection techniques.
* GUI Archetypes (*ui*, *uitab*, *uitopo*) facilitating rapid development of applications with custom UI content.

## Drake – 1.3.0

* Authentication Enabled by default (Login screen; logout action)
* More tabular views added:
  + Settings
  + Tunnels
* Changes to Topology View:
  + Traffic re-implemented as an "overlay"
  + Overlay mechanism now programmable from ONOS Apps
    - highlighting/labeling topology links
    - full control over summary panel content
    - full control over details panel content

## Cardinal – 1.2.0

* Websocket mechanism promoted to be framework-wide; a shared resource amongst the views.
* More tabular views added:
  + Links
  + Hosts
  + Intents
  + Applications
  + Cluster Nodes
  + Device Flows (hidden view)
  + Device Ports (hidden view)
  + Device Groups (hidden view)
* Changes to the Topology View:
  + links are now selectable.
  + toolbar added (note, keystroke commands still available)
    - node layer buttons moved from masthead to toolbar
  + sprite layer added
  + user selection choices persisted across sessions
  + summary and detail panels adjust size to window height
* Changes to the Device View:
  + slide out details panel appears when a device is clicked on
* Navigation Menu changes:
  + glyphs next to links for navigation
  + views organized into categories
* Note that the legacy (Avocet) GUI has been deprecated, and that the (Angular-based) GUI loads by default.

## Blackbird – 1.1.0

* GUI Framework migrated to use [AngularJS](https://angularjs.org/).
  + View-agnostic features refactored as Angular Services.
* Topology View refactored to be an Angular module.
  + Topology source code broken out into multiple source files.
  + Port Highlighting on links added.
* Device View added.
  + Implemented as a simple table for now; one device per row, sortable by column header clicks.
* Sample View added.
  + Skeletal example code.
* Light and Dark themes fully implemented.
  + Press the 'T' key to toggle theme.
* Beginnings of *UIExtension* mechanism implemented
  + Over future releases, this will facilitate the ability of Apps to inject their own content into the GUI.
* Note that the new (Angular-based) GUI currently co-exists with the old (Avocet) GUI.
  + By default, the Avocet GUI is launched; the base URL *<http://localhost:8181/onos/ui>* is mapped to *<http://localhost:8181/onos/ui/>**legacy**/index.html#topo*.
  + The new Angular-based GUI can be launched by manually adjusting the URL to be:  *<http://localhost:8181/onos/ui/index.html#topo>*, (that is, remove "***legacy/***").

## Avocet – 1.0.0

* GUI implemented using a home-grown framework.
* Single view (Topology View) implemented, displaying network topology and providing a certain level of interaction to show traffic & flow information.
* Although the 'T' key-binding (toggle theme) is present, the "dark" theme has not been implemented.
