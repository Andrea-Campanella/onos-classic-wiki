# GUI Flow View

# 

# Overview

The *Flow View* provides a top level listing of the flows associated with a chosen device. Flows are displayed in [tabular form](gui-tabular-view.md).

![](../../../../../assets/image2015-5-12-11745.png)

Each row in the table (that spans 3 lines) is a single flow on the device. To see more flows, scroll down inside the table body.

# Navigating to the Flow View

You can get to the Flow View in a few ways, although it is not on the main navigation menu.

## Topology View

To get to the flows view for a certain device on the [Topology View](gui-topology-view.md), select a device, **make sure the Details Pane is enabled**, and click on the button as shown below:

![](../../../../../assets/image2015-5-12-1185.png)

This will navigate you to the flows table for the device you have selected.

## Device View

To get to the flows table from the [Device View](gui-device-view.md), select a device (row) of the table to have the details panel appear. To get to the flows view, click on the button as shown below:

![](../../../../../assets/image2015-5-12-11925.png)

This will navigate you to the flows table for the device you have selected.

## Query String via URL

You can also get to the flows view for a specific device by altering the query string in the URL.

The URL format for the flows table is:

***http://<HOST>:<PORT>/onos/ui/index.html#/flow?devId=<DEVICE URI>***

Notice that the end of the URL contains query parameters. If you choose to navigate to the flows view directly, type in the device's URI after ***?devId=***.

For example, to get to flows table for the device with the URI "of:0000000000000002" while using the domain *localhost* and the default port, use the URL:

***http://localhost:8181/onos/ui/index.html#/flow?devId=of:0000000000000002***

# Header

The header of the Flow View will tell you which device's flows you are currently viewing, with how many flows there are in total on that device.

# Table Body

## Column Headers

The column headers for each section in the table are sortable (see [tabular view page](gui-tabular-view.md)). By default, the flows are sorted in ascending order by Flow ID. You can toggle between ascending and descending on any header.

## Information Not Under a Header

For readability, Criteria and Treatment Instructions about the flow are displayed in the lines below the other information displayed in columns.
