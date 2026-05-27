# GUI Topology View

# Overview

The *Topology View* provides a visual (cluster-wide) overview of the network topology controlled by ONOS. When the topology view is instantiated it requests topology information from the server; on receipt of that information, the view renders a visualization of devices, hosts, and the links between them. The view uses the web-socket connection established by the UI framework to allow the server to drive updates to the view via topology events (such as *addHost*, *updateDevice*, etc.)

![](../../../../../assets/topo-view-basic.png)

# Quick Help

One of the first things to note is that by pressing the slash '**/**' or backslash '**\**' key, you can bring up the *Quick Help* panel. This gives an outline of the keystroke commands and mouse gestures available to you in the *Topology View*.  Pressing either of these keys again (or pressing the *Esc* key) will dismiss the panel.

![](../../../../../assets/quick-help.png)

* The top section lists global key-bindings (available on every view in the UI)
* The middle section lists view-specific key-bindings
  + The first and second columns show general commands for the Topology view
  + The third column shows commands for the currently active "Topology Overlay" (if any)
* The bottom section lists view-specific mouse gestures and other notes

The available commands listed in this panel are described in more detail in the sections below.

# Toolbar – Topology Functions

The *Topology View*'s key-bindings (listed in *Quick Help*) are also associated with buttons on the toolbar.

The toolbar can be shown or hidden by pressing the dot (.) key.

![](../../../../../assets/toolbar-info.png)

> *Note*: Toolbar button states (toggled on or off) are persisted in user preferences, so may appear differently to those shown.

The toolbar has three rows of buttons:

* The first row and half the second row provide basic functions.
* The second half of the second row provides a radio-button-set of installed "overlays".
* The third row contains buttons contributed by the currently-active "overlay".

Overlays bundled with out-of-the-box ONOS are listed here. Follow the links for more information:

* **[Traffic Overlay](gui-topology-view/gui-topology-overlay-index/topology-overlay-traffic.md)**
* **Maps Overlay** (coming soon)
* ...

Hovering the mouse over a button will display a tooltip describing the button, including the bound key-stroke:

![](../../../../../assets/toolbar-tooltip.png)

## Toolbar First Row

| Icon | Key | Function | Default State | Comments |
| --- | --- | --- | --- | --- |
|  | **I** | Show / hide ONOS cluster instance panel | show | The instance panel is shown by default. |
|  | **O** | Show / hide ONOS summary panel | show | The summary panel is shown by default. |
|  | **D** | Disable / enable details panel | enable | The details panel is enabled by default, and is displayed when one or more topology elements are selected. Disabling this panel keeps it hidden even when something is selected. |
|  |  |  |  |  |
|  | **H** | Toggle host visibility | hide | Shows or hides the hosts (and their links). Hosts are hidden by default. |
|  | **M** | Toggle offline visibility | show | Devices that are offline (but that ONOS still knows about) are shown by default. This toggle will hide offline devices (and any hosts/links connected to them). |
|  | **P** | Toggle port highlighting | on | Port highlighting is when hovering the mouse over a link will highlight the link and label the ends with the appropriate port numbers. This feature can be switched off with this toggle. |
|  | **B** | Toggle background geo map | hide | The background map (hidden by default) can be shown or hidden with this toggle. |
|  | **G** | Select background geo map | n/a | Opens a dialog box which allows selection of a geographic region from a pre-defined set. |
|  | **S** | Toggle sprite layer | hide | The sprite layer (static shapes/text injected into the view) can be shown or hidden with this toggle. |

## Toolbar Second Row

| Icon | Key | Description | Default State | Comments |
| --- | --- | --- | --- | --- |
|  | **Z** | Toggle oblique view (experimental) | regular view | Creates a split-level visualization of the packet and optical layers of the network. Note that this feature is experimental and may be slightly buggy. |
|  | **N** | Cycle node layers | show all layers | Cycles between three view modes: show all layers, show packet layer, show optical layer. |
|  | **L** | Cycle device labels | hide labels | Cycles between three modes of showing labels on devices: hide labels, show friendly labels, show device ID. |
|  | **R** | Reset pan / zoom | - | This function restores the pan and zoom levels to default settings. |
|  |  |  |  |  |
|  | **E** | Equalize mastership roles | - | Sends a command to ONOS to invoke a mastership equalization request. |
|  |  |  |  |  |
|  |  | No overlay |  | De-activates the current overlay. |
|  |  | **[Traffic overlay](gui-topology-view/gui-topology-overlay-index/topology-overlay-traffic.md)** | (tick) | Provides traffic monitoring functions. |
| ``` ... ``` |  | ``` ... ``` |  | *<Topology Overlays installed by ONOS Apps will appear here>* |

## Toolbar Third Row

The third row of the toolbar is space reserved for the currently active topology overlay.

# Cluster Instance Panel

The cluster instance panel shows summary information about the ONOS instances in the cluster. There will be one box per instance, showing the instance ID, IP address, and number of switches for which the instance is master.

The panel can be hidden (and subsequently re-shown) by pressing the '**I**' (for "Instances") key.

![](../../../../../assets/cluster-panel.png)

The color coding indicates controller mastership; each device in the topology will be colored corresponding to which instance has mastership over it. For example:

![](../../../../../assets/master-0.png)

For a clearer indication of mastership, clicking on an instance box in the instance panel will highlight the appropriate devices, subduing all else:

![](../../../../../assets/side-by-side.png)

Click again on the same instance box (or press *Esc*) to cancel the affinity highlighting.

# Summary Panel

The summary panel displays key properties of the network.

The panel can be hidden (and subsequently re-shown) by pressing the '**O**'  (for *"ONOS summary"*) key.

![](../../../../../assets/summary-panel.png)

# Nodes and Links

The network topology is represented by an undirected graph of nodes and links. The nodes represent devices (switches) and hosts; the links represent, uh, links.

The [D3 Force Layout](https://github.com/mbostock/d3/wiki/Force-Layout) algorithm is used to provide a reasonable initial layout of the nodes and links in the absence of any other spatial information. As an example, the following image shows a (free-floating) network of 25 nodes:

![](../../../../../assets/topo-model-freeform.png)

The ***onos-topo-cfg*** command (script) can be used to upload topology meta-data to the server. This may include longitude/latitude information for each of the nodes. The following commands upload topology information for the 25 device use case shown in the image:

> ```
> cd $ONOS_ROOT/tools/test/topos
> ```
>
> ```
> onos-topo-cfg $OCI attmpls.json
> ```

On receipt of the data, the server sends node updates to the UI. On the client-side, the longitude/latitude data is used to calibrate node positions with the background map:

![](../../../../../assets/topo-model-latlong.png)

Note that, by default, hosts are hidden. Pressing the '**H**' key will toggle the host visibility:

![](../../../../../assets/topo-model-hosts.png)

Additionally, pressing the '**L**' key will cycle through the devices labels (*"friendly", "ID", "no-label"*):

![](../../../../../assets/topo-model-labels.png)

# Mouse Gestures

A node (device / host) may be repositioned manually (and pinned into place) by clicking and dragging it to a new location.

> NOTE: To unpin a pinned node, hover the mouse over the node and press the '**U**' (Unpin) key.

Clicking on a node or link will select it (and deselect any other selections). Details of the selected node or link will appear in the details panel. Note that action buttons relating to the selection may be provided at the bottom of the panel.

Multiple selections (nodes only, not links) may be achieved by holding down the *Shift* key while clicking on a node - this toggles the selection state of that node.

Clicking elsewhere on the map or pressing the *Esc* key will clear the current selection.

Panning and zooming the view may be achieved with *Cmd-drag* (or *Alt-drag*) and *Cmd-scroll* (or *Alt-scroll*) gestures respectively. Pressing the '**R**' key will reset the *pan/zoom* settings to the default values.

# Details Panel - Single Selections

The details panel appears (unless disabled with the '**D**' command) when something of interest is "selected".

## Device Selected

When a *single device* is selected, properties of that device are displayed, along with action buttons:

![](../../../../../assets/select-1device-traffic.png)

The four action buttons (with white backgrounds) are navigation buttons detailed below. The two action buttons on the right are added to the panel if the Traffic Overlay is currently active. See the **[Traffic Overlay](gui-topology-view/gui-topology-overlay-index/topology-overlay-traffic.md)** page for details.

| Navigation Actions | |
| --- | --- |
|  | *Navigate to the **[Device View](gui-device-view.md)** for the selected device* |
|  | *Navigate to the **[Flow View](gui-flow-view.md)** for the selected device* |
|  | *Navigate to the **[Port View](gui-port-view.md)** for the selected Device* |
|  | *Navigate to the **[Group View](gui-group-view.md)** for the selected Device* |

## Host Selected

When a *single host* is selected, properties of that host are displayed.

![](../../../../../assets/select-host.png)

If an overlay is currently active, action buttons may also be displayed, depending on the overlay.

## Link Selected

When a *link* is selected, properties of that link are displayed:

![](../../../../../assets/select-link.png)

Note that it is not possible to select multiple links.

# Details Panel - Multiple Selections

It is possible to select multiple nodes (devices / hosts) at the same time. In these cases the details panel lists the identities of the selected elements in the order of selection:

![](../../../../../assets/select-multi.png)

Action buttons may also be provided if the active overlay has functions that operate on a multi-selection.

# Port Highlighting

By default, port highlighting is enabled, which means that as the mouse hovers over a link, the link highlights and the port numbers at both ends of the link are shown:

![](../../../../../assets/port-numbers.png)

The port highlighting feature can be toggled on / off by pressing the '**P**' (for 'Port highlighting') key.

The following section will be migrated to a new page real soon now!!!!

# Traffic Overlay functions

| Icon | Key | Description |
| --- | --- | --- |
|  | **V** | Show all related intents |
|  | **Right Arrow** | Show next related intent |
|  | **Left Arrow** | Show previous related intent |
|  | **W** | Monitor traffic of selected intent |
|  | **A** | Monitor all traffic |
|  | **F** | Show device link flows |

# Visualizing Traffic

A number of commands allow different visualizations of traffic on the network.

## All Traffic

If there is traffic flowing on the network (for example, if reactive forwarding is active, and a pingall is run on mininet), then pressing the 'A' key will display something like the following:

![](../../../../../assets/gui-topo-alltraffic.png)

Note that the labels on the links show the cumulative number of bytes traversing that link since traffic monitoring was requested, (i.e. since the 'A' key was pressed).

## Device Link Flows

If a specific device is selected, and the 'F' key pressed, then the number of flows egressing from the device will be shown:

![](../../../../../assets/image2015-5-12-134754.png)

## Host to Host Intent

The following 4 images show the selection of two hosts and the installation of a host-to-host intent:

(1) Host (.15) at Denver (DNVR) is selected:

![](../../../../../assets/image2015-5-12-135227.png)

(2) Host (.14) at Orlando (ORLD) is selected:

![](../../../../../assets/image2015-5-12-135417.png)

(3) *"Create Host-to-Host Flow"* action button pressed (on Detail Panel):

![](../../../../../assets/gui-topo-h2hintent-03.png)

(4) Monitor traffic of selected intent ('W' key pressed). Note the traffic showing as labels on the links:

![](../../../../../assets/gui-topo-h2hintent-04.png)

## Show Related Intents

If a device is selected, pressing the 'V' key will show all related intents, i.e. all intents for which the selected device is a part. Note that if multiple devices are selected, a logical AND operation is applied, meaning that only those intents for which all the selected devices are a part will be highlighted.

(1) Related intent which passes through both Denver (DNVR) and Dallas (DLLS):

![](../../../../../assets/gui-topo-relatedintents-1.png)

(2) There are no related intents that pass through Denver (DNVR), Dallas (DLLS), and Kansas City (KSCY):

![](../../../../../assets/gui-topo-relatedintents-2.png)

## A Set of Related Intents

It is quite probable that a device will be associated with a set of intents. For our example here, let's set up two more host-to-host intents that pass through Dallas:

(1) From host (.13) at Dallas (DLLS) to host (.9) at St Louis (STLS):

![](../../../../../assets/gui-topo-moreintents-05.png)

(2) From host (.12) at San Antonio (SNAN) to host (.2) at Chicago (CHCG):

![](../../../../../assets/gui-topo-moreintents-06.png)

Clearing the selection, then selecting the Dallas device and pressing the 'V' key, we can see the related intents:

![](../../../../../assets/gui-topo-moreintents-07.png)

Now, by repeatedly pressing the *Right-Arrow* key (for next-related-intent) or *Left-Arrow* key (for previous-related-intent), we can step through the intents one at a time. Notice how one intent will be highlighted in orange (the primary selection) and all the other (related) intents are highlighted in green (the secondary selection):

(1) Press '→' key

![](../../../../../assets/gui-topo-nextintent-08.png)

(2) Press '→' key

![](../../../../../assets/gui-topo-nextintent-09.png)

(3) Press '→' key

![](../../../../../assets/gui-topo-nextintent-10.png)

# ONOS Instance Failover

The GUI is designed to detect when the Cluster Instance to which it is connected fails, and to seamlessly "failover" to an alternate cluster member.

(1) Note the three instances, each master of a number of switches (8, 8, and 9, respectively). Note also that the UI is attached to the first instance, as indicated by the icon:

![](../../../../../assets/gui-topo-failover-01.png)

(2) Here, the first instance has failed and the UI has switched over to the second instance. Note also that the remaining two instances have picked up mastership of the switches (now, 9, and 16 respectively):

![](../../../../../assets/gui-topo-failover-02.png)

(3) When the first instance recovers it comes back online, but note how the UI remains attached to the second instance, and also that there is no automatic re-balancing of switch mastership. (now, 0, 9, and 16, respectively):

![](../../../../../assets/gui-topo-failover-03.png)

(4) Pressing the 'E' key sends a command to the server to "Equalize" the mastership roles across the cluster. Note now how the switches have been rebalanced, (now 8, 9, and 8, respectively):

![](../../../../../assets/gui-topo-failover-04.png)

# Miscellaneous Controls

The remaining keystrokes are:

* **M** - Toggle offline device visibility
  + Normally, offline devices are shown as grayed-out icons. This can be toggled to where offline devices are hidden instead.
* **B** - Toggle background image
  + The map of the Continental US can be toggled off and on.
* **S** - Toggle sprite layer
  + The sprite layer (with injected sprites) can be toggled on and off.
* **X** - Lock / unlock node positions
  + The default is to allow click-and-drag to move nodes (devices & hosts) on the display.
* **Z** - Toggle oblique view (Experimental)
  + This mode will show a "sideways" view of the network, separating packet-layer nodes from optical-layer nodes.
  + As noted, this mode is currently experimental.

# Topology Overlay Components

An ONOS application can provide a [Topology Overlay Component](gui-topology-view/topology-overlay-components.md) to inject additional detail and behavior to the topology view.

# Background Map

The background map provides a geographic reference for the topology. The default map is the Continental US. The map layer's visibility can be toggled on and off with the 'B' (for background) key.  
See [Providing Alternate Maps for the Topology View](gui-topology-view/topology-alternate-maps.md) for additional details.

The scale of background map can be changed on demand. To do that, simply append ***?mapscale=<real-number>*** at the end of the URL. For example,

http://localhost:8181/onos/ui/index.html#/topo**?mapscale=1.5**

# Custom Sprites

The [Topology Sprite Layer](gui-topology-view/topology-sprite-layer.md) mechanism allows custom "background" elements to be displayed (above the background map, but below the topology elements). This could be used, for example, to inject labeled "subnet clouds", or the plan of an office building or campus into the topology view. Typically, one would want to hide the background map layer (press '**B**') and show the sprite layer (press '**S**') instead.

In the current release (1.3.0 "Cardinal") sprite layers are defined in an external JSON format and uploaded to the controller via a REST command. They are loaded into the Topology view by manually adjusting the browser URL to include a "sprites" query parameter. We hope to provide a more user-friendly mechanism (directly through the GUI) in some future release.
