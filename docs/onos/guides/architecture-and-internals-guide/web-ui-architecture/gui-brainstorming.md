# GUI Brainstorming

# Introduction

This page captures thoughts and ideas about the long term goals of (and philosophy behind) the ONOS GUI.

The hope is that these ideas will influence the directions we take and the decisions we make as the GUI evolves over time.

# Is / Is Not

The GUI ***is***...

* used in demos to illustrate / visualize ONOS capabilities
* used to monitor the ONOS Cluster:
  + Configuration
  + Installed Apps
  + Health
  + Metrics
* used to inspire app developers to create visualizations for their application
* used by ONOS QA group during testing
* runtime extensible by ONOS Apps (reference implementation(s) provided)
* ...

The GUI ***is not***...

* a complete Network Management solution
* a complete alternative to the ONOS CLI or Rest API
* used for provisioning intents or similar tasks
  + (except, perhaps, for simple "host-to-host intent" demo)
  + The *CLI*, *Java API* and *Rest API* are better suited for such provisioning tasks
  + Is there going to be a big warning label indicating this? If not, is it appropriate to provide APIs for cases where app developers want to implement such tasks via GUI? I figure a dev can look at the 'host-to-host' demo to see that it's possible to provision resources via the GUI, and might question why there is a 'hidden API'...
* ...

## Who might use the GUI?

The GUI may be used by a number of different roles:

* Operators
* App Developers
* ONOS Dev / test

## How might the GUI be used?

The GUI may be used in a number of different scenarios:

* Kiosk mode
  + Large screen in control center / trade-show booth
* Diagnostics
  + Show hotspots - let user "drill down" to an issue
* Demo App
  + Providing a reference implementation, to help App Developers create and integrate their own GUI content
  + An SDK would provide GUI-related API documentation, tutorials etc.

## Finding Information of Interest

The GUI should provide filtering / searching capabilities to allow the user to locate information of interest. Search mode would include:

* Global
* Specific context (eg. selected items, groups?)

Search makes intuitive sense for the tabular view - how would other views e.g. topology show search results? Would it stay in the context of that view (highlighting the results or something), or jump to a 'results' view? 

## Topology View

The topology view is the main "ONOS out-of-the-box" view, and visualizes the network (and how mastership is divided up by cluster members), but it:

* should allow the user to see the state of the network at the "10,000 ft level"
  + from there, the user may zoom in for more detail to areas of interest.
  + E.g., in a large network, individual switches may not be shown, rather they may be collapsed into groups/regions of switches.
  + A suitable gesture should "expand" the group to show the individual subgroups / switches.
* should be augmentable by Apps running on top of ONOS
  + eg. nodes decorated with status badges
  + nodes and/or links selectable / highlightable identifying certain items of interest
* should be customizable by the user
  + add, position, and label subnet 'clouds'
  + additional choice of OOTB background maps selectable
  + ability to add custom (App provided) background map (e.g. map of a campus)

## Tabular Views

Some information may lend itself to be presented in tabular form. For example, list of all:

* Devices
* Hosts
* Links
* Intents
* Flows
* ...

Each line item would be some summary of the item. A gesture (e.g. row double-click) should navigate to a more detailed view of the specific item.

## Other Views

There are bound to be other types of view that would be useful for presenting data. Perhaps charts or graphs showing historical data?
