# Managing ONOS applications

The following section describes how to perform basic tasks on ONOS applications, such as installing, uninstalling, listing, activating applications, in production environments.

For production deployments, apps can be either included in the ONOS package before deploying, or installed later, in form of ONOS Application aRchives (OARs).

# Distributed application management

As any other cluster operation, managing applications can be done from one node of the cluster. The cluster itself will know how to copy the bits to the other nodes of the cluster (target machines) and/or replicate configurations.

# Installation vs. activation

*Installing* an application means copying the application to the target machine running ONOS. As on your PC, installing an application doesn't mean necessarily run the application.

In order to run (execute) an application, you need to explicitly *activate* it.

Of course, related uninstall and deactivate options follow the same semantic.

# ONOS applications user guides

ONOS comes in its standard distribution with a number of default applications, such as [SDN-IP](../../../apps-and-use-cases/sdn-ip.md) and [VPLS](../../../apps-and-use-cases/virtual-private-lan-service-vpls.md). These applications do not have to be installed explicitly via OAR files, but they do need to be activated and configured. Detailed instructions for configuring and running these applications can be found in the appropriate sections of [Apps and Use Cases](../../../apps-and-use-cases.md).

# Managing applications using REST-APIs

Specific REST APIs to manage applications won't be discussed in the sections below. You can find a complete list of applications related REST APIs under the development guide, here: [Appendix B: REST API#Application](../../developer-guide/appendix-b-rest-api.md)

# Listing installed applications

Installed applications can be listed through the CLI, the GUI and the REST APIs.

In the CLI, use the *apps* command to list all the applications installed. You can add the -s (summary) parameter to see a more compact version of the list, and the -a (active) parameter to see only the active applications. Active applications should have an asterisk near their name.

**Example of the apps, ONOS CLI command**

```
onos> apps -s
    4 org.onosproject.scalablegateway      1.9.0.SNAPSHOT Scalable GW App
    5 org.onosproject.distributedprimitives 1.9.0.SNAPSHOT Distributed Primitives Test App
    6 org.onosproject.patchpanel           1.9.0.SNAPSHOT Patch Panel
    7 org.onosproject.netcfglinksprovider  1.9.0.SNAPSHOT Network Config Link Provider
    8 org.onosproject.isis                 1.9.0.SNAPSHOT ISIS Provider
    9 org.onosproject.cip                  1.9.0.SNAPSHOT Cluster IP alias App
   10 org.onosproject.openflow-message     1.9.0.SNAPSHOT Control Message Stats Provider
   11 org.onosproject.segmentrouting       1.9.0.SNAPSHOT Segment Routing App
   12 org.onosproject.virtualbng           1.9.0.SNAPSHOT Virtual Broadband Gateway App
   13 org.onosproject.metrics              1.9.0.SNAPSHOT OpenStack Interface App
   14 org.onosproject.ovsdb-base           1.9.0.SNAPSHOT OVSDB Provider
   15 org.onosproject.drivers.ovsdb        1.9.0.SNAPSHOT OVSDB Device Drivers
   16 org.onosproject.yms                  1.9.0.SNAPSHOT YANG Management System App
   17 org.onosproject.influxdbmetrics      1.9.0.SNAPSHOT InfluxDB Report and Query App
   18 org.onosproject.bgp                  1.9.0.SNAPSHOT BGP Provider
   19 org.onosproject.restsb               1.9.0.SNAPSHOT REST Provider
*  20 org.onosproject.hostprovider         1.9.0.SNAPSHOT Host Location Provider
*  21 org.onosproject.lldpprovider         1.9.0.SNAPSHOT LLDP Link Provider
*  22 org.onosproject.optical-model        1.9.0.SNAPSHOT Optical information model
*  23 org.onosproject.openflow-base        1.9.0.SNAPSHOT OpenFlow Provider
*  24 org.onosproject.openflow             1.9.0.SNAPSHOT OpenFlow Meta App
```

You can list applications from the GUI accessing the specific view. For more details, please look at the [ONOS Web GUI section](#).

# (Re)-install/uninstall an ONOS application (OAR)

ONOS applications in form of OAR bundles can be (re)-installed and uninstalled from the ONOS GUI. To do that, go in the application view and click on the plus button on the top-right corner of the page, choose your OAR file from your local storage and click ok. From the same view, an application can be selected and uninstalled (removed) using the bin icon.

Soon, an onos-app CLI utility (included for now only in the ONOS development repository) will also be added to the ONOS package to facilitate the CLI application management.

# Activate and deactivate ONOS applications

Once installed, applications can be activated and deactivated through the ONOS CLI, GUI and REST APIs.

To activate/deactivate an application from the ONOS CLI use the app command:

```
onos> app (de)activate org.onosproject.$YOUR_APP_NAME
```

From the ONOS GUI, access the application view, select the application you like to (de)activate, and click either the start or stop icons in the top-right corner of the screen.
