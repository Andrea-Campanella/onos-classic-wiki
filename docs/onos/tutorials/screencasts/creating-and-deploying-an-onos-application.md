# Creating and deploying an ONOS application

## [YouTube Video](https://www.youtube.com/watch?v=mzQubYhJhro)

## Overview

ONOS is a distributed system designed to operate in a symmetric manner, where all cluster instances are software-wise identical. To facilitate this, the ONOS platform includes an application management subsystem for managing network control apps in a distributed context.

In this screencast, we will demonstrate how to use the ONOS CLI and REST API to manage applications on a distributed ONOS cluster. We will also show you how to create an ONOS application project, build it and how to deploy the application.

First, though, let’s provide a little background on OSGi bundles, Karaf features and how they relate to ONOS apps.

## OSGi Bundles, Karaf Features and ONOS apps

ONOS application subsystem is built atop the Apache Karaf feature service, which in turn is built using the standard OSGi bundle management services. Karaf feature service essentially provides means to activate and deactivate a collection of OSGi bundles as a single feature. An ONOS app is defined in terms of such features and provides means to contain the *features.xml* definitions as well as any required OSGi bundles into a single artifact. This artifact, an OAR file - as in ONOS Application aRchive - is then used to deliver the application software across the entire ONOS cluster.

## ONOS CLI console

For our demonstration, we are running a three-node ONOS cluster, which has already been started in the interest of time.

Let’s connect to the ONOS console of any of the cluster nodes, say the second one.

The ONOS console offers a number of commands for interacting with the application subsystem. We can use the apps command to see what applications are installed and which of them are presently active. The applications we see here are the providers, drivers and various sample and test apps that are part of the ONOS codebase. Presently, only the *drivers* and the *openflow* providers are active.

The app command can be used to install, uninstall, activate and deactivate applications across the cluster. For example, typing app activate *org.onosproject.fwd* will activate the reactive forwarding application.

If we check on all the nodes, we can see that the application was activated everywhere and that the backing Apache Karaf feature is active, as expected.

## ONOS REST API and onos-app tools

The same capabilities are accessible through the ONOS REST API and via onos-app shell tool, which uses the REST API to provide means to control ONOS applications directly from the command shell. We will use this tool shortly to install and activate our own application.

## Using ONOS Maven archetypes to create a module

To create our own ONOS app, we will start by creating an ONOS bundle project using the ONOS Maven archetype. We will create the project directly off our home directory by typing the following Maven command:

```
mvn archetype:generate -DarchetypeGroupId=org.onosproject -DarchetypeArtifactId=onos-bundle-archetype -DarchetypeVersion=1.2.0-SNAPSHOT
```

Please note that the archetype version may change over time.

This will launch a short interview process that will allow us to name and version our module. We will use the *org.foo.app* as the groupId and name our module *foo-app* via artifactId. We will leave the version and the Java package at their default values and confirm all selections by pressing Enter.

At this point, the *pom.xml* file and the necessary source files have been generated and are ready to be built.

## Marking module as an ONOS app and building it

However, before we do that, let’s mark the module as an ONOS application by editing the pom.xml file and setting *onos.app.name* property to org.foo.app. Defining this property is all that is required for Maven to produce the application OAR file since the generated pom.xml file already contains the proper configuration of *onos-maven-plugin*.

While here, let’s also define *onos.app.origin* property and set it to value of Foo, Inc. and let’s change the project description to a brief text that describes the purpose of our application.

After saving the changes to the *pom.xml* file, we are ready to build our application. To do that, we simply type ‘*mvn clean install*’ from the command shell. Note that this process not only creates the JAR bundle, but also the application OAR file.

## Installing ONOS app via onos-app shell tool

Now that the application has been built, we can go ahead and install it on our cluster. We will do so with the help of the onos-app shell utility, which in turn uses the REST API.

Simply type in ‘*onos-app $OC1 install target/foo-app-1.0-SNAPSHOT.oar*’. To go ahead and also activate the application immediately after installing it, we can add an exclamation point after the install parameter. Let’s do that.

After submitting the command, we will see some compact JSON output, which is returned by the REST API to indicate that the application has been successfully installed and activated.

If we check its status on all the nodes, we can see that the application is running on the entire cluster.

## Re-installing ONOS app via onos-app shell tool

If we were to make some changes to our application code, say changing the startup message to “Hello World!”, we can then build and re-install the application in a single command-line as follows:

```
mvn clean install && onos-app $OC1 reinstall! org.foo.app target/foo-app-1.0-SNAPSHOT.oar
```

A quick glance at the logs on all the machines in the cluster, we will see the new “*Hello World!*” message, indicating the application was successfully updated. And we did not even have to restart ONOS.

## Multi-bundle applications

What we have done thus far was to build a single-bundle application. ONOS of course, allows defining and packaging multi-bundle and multi-feature applications. In order to do this, one has to explicitly define their own app.xml and *features.xml* files. In case of a single-bundle application, these files were generated automatically by the *onos-maven-plugin*.

The built in BGP router application serves as an example of how this can be accomplished. This is an example of a multi-bundle *features.xml* file and a corresponding *app.xml file*, which specified what artifacts are to be included in the application OAR file.

For more information on the application subsystem and on creating applications, please see the ONOS wiki.

## Conclusion

Hopefully, this screencast gave you some insight on what is involved in building and deploying an ONOS application.

Have a great day… and happy coding!
