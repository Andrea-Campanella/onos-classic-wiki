# GUI Group View

The *Group View* provides a top level listing of the groups a chosen device belongs to. Groups are displayed in [tabular form](gui-tabular-view.md).

![](../../../../../assets/image2015-5-13-1068.png)

Each row in the table is a single group on the device. To see more groups, scroll down inside the table body.

# Navigating to the Group View

You can get to the Group View in a few ways, although it is not on the main navigation menu.

## Topology View

To get to the groups view for a certain device on the [Topology View](gui-topology-view.md), select a device, **make sure the Details Pane is enabled**, and click on the button as shown below:

![](../../../../../assets/image2015-5-12-114635.png)

This will navigate you to the group table for the device you have selected.

## Device View

To get to the groups table from the [Device View](gui-device-view.md), select a device (row) of the table to have the details panel appear. To get to the groups view, click on the button as shown below:

![](../../../../../assets/image2015-5-12-114747.png)

This will navigate you to the group table for the device you have selected.

## Query String via URL

You can also get to the groups view for a specific device by altering the query string in the URL.

The URL format for the groups table is:

***http://<HOST>:<PORT>/onos/ui/index.html#/group?devId=<DEVICE URI>***

Notice that the end of the URL contains query parameters. If you choose to navigate to the groups view directly, type in the device's URI after ***?devId=***.

For example, to get to groups table for the device with the URI "of:0000000000000002" while using the domain *localhost* and the default port, use the URL:

***http://localhost:8181/onos/ui/index.html#/group?devId=of:0000000000000002***

# Header

The header of the Group View will tell you which device's groups you are currently viewing, with how many groups there are in total on that device.

# Table Body

## Column Headers

The column headers for each section in the table are sortable (see [tabular view page](gui-tabular-view.md)). By default, the groups are sorted in ascending order by Group ID. You can toggle between ascending and descending on any header.
