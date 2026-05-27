# Application Subsystem

## Overview

The purpose of the application subsystem is to facilitate easy software delivery and management across all ONOS instances in a cluster. The subsystem uses ONOS eventually consistent map and the inter-node communication mechanism to fully replicate the inventory of applications across the entire ONOS cluster. To install and ignite software as sets of OSGi bundles, the subsystem relies on the underlying Apache Karaf feature mechanism.

All builtin sample and test applications provided by ONOS are now delivered using this mechanism and come pre-installed - although not activated - as part of the standard ONOS distribution. This includes any providers, such as OpenFlow providers. In this way, all optional software components can be installed into and withdrawn from ONOS without the need to rebuild, or even to reconfigure ONOS itself.

## Application Package

Applications can be packaged into a single *.oar* (ONOS Application aRchive) file for easy delivery of software to a running ONOS cluster. The *.oar* file is a ZIP file that contains all artifacts, such as feature definitions or OSGi bundles, which may otherwise not be available on Maven central. The following describes the structure of the *.oar* file:

* *app.xml* - application descriptor
* *m2/<groupId>/<artifactId>/<version>/<featuresRepo>*
* *m2/<groupId>/<artifactId>/<version>/<artifact>*
* ...

The application package files can be produced using *onos-maven-plugin* quite easily. The *pom.xml* file needs to include *onos-maven-plugin* in its build section and if the *pom.xml* defines *onos.app.name* property, or if the module base directory contains *app.xml* file, the plugin will build the application *.oar* file and this file will be installed into M2 repository during Maven install phase. See the Maven example below.

## Application Definition

Single bundle applications can be easily produced by specifying the following properties in the bundle's *pom.xml* file:

* *onos.app.name* - name of the application, should be specified in reverse DNS notation, e.g. *org.onosproject.fwd*
* *onos.app.origin* - name of the originating entity or company, e.g. *ON.Lab*
* *onos.app.requires* - comma-separated list of applications required by this app

Multi-bundle applications, or those that need to bring in other artifacts, or custom feature dependencies can be defined using the *app.xml* file, located in the module base directory. The *app.xml* file specifies the following attributes:

* *name* - application name, specified in reverse DNS notation
* *version -* application version
* *origin* - company or organization where application originated
* *description* - short description of the application
* *features* - list of Apache Karaf features that comprise the application
* *featuresRepo* - optional URL of application feature definition artifact
* *apps* - comma-separated list of applications required by this app
* *artifact* - lists artifacts that are to be included in application package

The following is an example of an application *app.xml* file:

```
<?xml version="1.0" encoding="UTF-8"?>
<app name="org.onosproject.sample" origin="ON.Lab" version="${project.version}"
     featuresRepo="mvn:${project.groupId}/${project.artifactId}/${project.version}/xml/features"
     features="sample-app">
    <description>${project.description}</description>
    <artifact>mvn:...</artifact>
</app>
```

The *app.xml* file can contain Maven properties such as *${project.groupId},**${project.artifactId}*, *${project.version}*, *${project.description},* which will result in substitution of the appropriate value from the Maven *pom.xml* file. It is highly recommended to use these in order to minimize the amount of maintenance required.

The ONOS code-base contains examples of both approaches under the *apps* source tree.

## CLI Commands

Administrators can interact with the inventory of applications using the following console commands:

* *apps* - lists all installed applications
* *app install <mvn-url> ...* - installs applications by downloading from the specified URLs
* *app activate <app-name> ...* - activates all specified applications
* *app deactivate <app-name> ...* - deactivates all specified applications
* *app uninstall <app-name> ...* - uninstalls all specified applications

## REST API and Shell Utility

Orchestration systems and tools can use the [REST API](../developer-guide/appendix-b-rest-api.md) to interact with the application subsystem either directly, or using the *onos-app* shell utility, which uses the REST API and has the following usage:

* *onos-app install <app.xml or app.zip> ...* - installs application by uploading the specified *app.xml* or application package file
* *onos-app install! <app.xml or app.zip> ...* - installs and activates applications by uploading the specified *app.xml* or application package file
* *onos-app reinstall <app-name> <app.xml or app.zip> ...* - re-installs application by uploading the specified *app.xml* or application package file
* *onos-app reinstall! <app-name> <app.xml or app.zip> ...* - re-installs and activates applications by uploading the specified *app.xml* or application package file
* *onos-app activate <app-name> ...* - activates the specified application
* *onos-app deactivate <app-name> ...* - deactivates the specified application
* *onos-app uninstall <app-name> ...* - uninstalls the specified application

## Maven Example

The following snippet shows the required *onos-maven-plugin* configuration. ONOS built-in and sample application modules inherit this configuration from the ONOS root pom, but external applications, need to include this configuration in their POM hierarchy or they need to inherit from ONOS root POM:

```
<plugins>
    ...
    <plugin>
        <groupId>org.onosproject</groupId>
        <artifactId>onos-maven-plugin</artifactId>
        <version>1.4-SNAPSHOT</version>
        <executions>
            <execution>
                <id>app</id>
                <phase>package</phase>
                <goals>
                    <goal>app</goal>
                </goals>
            </execution>
        </executions>
    </plugin>
    ...
</plugins>
```

Note that the plugin will tag the *.oar* file as installation artifact, resulting in its installation or deployment into the Maven repository when the Maven *install* or *deploy* goals are invoked.

## Builtin Sample and Test Applications

The following list describes the inventory of all builtin drivers, providers and the various sample and test applications:

* *org.onosproject.drivers* - Builtin device drivers
* *org.onosproject.openflow* - OpenFlow protocol southbound providers

* *org.onosproject.bgprouter* - BGP router application, features
* *org.onosproject.config* - Network configuration application
* *org.onosproject.demo* - Flow throughput test application
* *org.onosproject.election* - Master election test application
* *org.onosproject.fwd* - Reactive forwarding application using flow subsystem
* *org.onosproject.intentperf* - Intent performance test application
* *org.onosproject.metrics* - Performance metrics collection
* *org.onosproject.mobility* - Host mobility application
* *org.onosproject.null* - Null southbound providers for testing
* *org.onosproject.optical* - Packet/Optical use-case application
* *org.onosproject.proxyarp* - Proxy ARP/NDP application
* *org.onosproject.sdnip* - SDN/IP use-case application
* ...
