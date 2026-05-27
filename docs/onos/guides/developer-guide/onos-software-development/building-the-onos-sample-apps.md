# Building the ONOS Sample Apps

In addition to the core ONOS system and applications, the ONOS project has created sample applications ("ONOS Sample Apps") which provide additional features and can also serve as instructional code or as something that you can extend and modify into a full-featured application.

## Prerequisites

Before building the ONOS Sample Apps, you should make sure that you have installed **Java**, **`git`**, and **Maven**.

Maven vs. Buck

Beware: ONOS and the core applications in the main ONOS source tree are currently built using **`buck`**, but the sample apps in `onos-app-samples` are currently built using **`mvn`**. This may change in the future! It is likely that we will move to a single build system for both ONOS and all of its applications.

## Fetching the Source Code

```
git clone https://gerrit.onosproject.org/onos-app-samples
cd onos-app-samples
```

## Selecting the ONOS Version

By default, the sample apps will be built against a *nightly snapshot* of ONOS master. The functionality and reliability of this snapshot may vary rapidly and unpredictably, but it may also be what you want if an application requires bleeding-edge features.

If you wish to build against a released version of ONOS rather than a random snapshot, you can edit pom.xml to specify a specific ONOS release. For example:

```
<parent>
 <groupId>org.onosproject</groupId>
 <artifactId>onos</artifactId>
 <version>1.8.2</version>
</parent>
```

## Basic Compilation

To simply compile and check for errors, you can `cd` to the `onos-app-samples` directory and run:

```
mvn compile
```

This will download all of the required `.jar` files, including ONOS as well as other required libraries, and compile the Java source into `.class` files.

It will produce a lot of output, but should eventually succeed, printing something like:

```
[INFO] Reactor Summary:
[INFO] 
[INFO] onos-app-samples ................................... SUCCESS [  2.619 s]
[INFO] onos-app-calendar .................................. SUCCESS [  1.290 s]
[INFO] onos-app-database-perf ............................. SUCCESS [  0.272 s]
[INFO] onos-app-flowtest .................................. SUCCESS [  0.359 s]
[INFO] onos-app-ifwd ...................................... SUCCESS [  0.247 s]
...
[INFO] onos-app-icona ..................................... SUCCESS [  0.051 s]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 13.487 s
[INFO] Finished at: 2017-02-03T15:32:55-08:00
[INFO] Final Memory: 76M/379M
[INFO] ------------------------------------------------------------------------
```

## Building the `.oar` files

To compile each app all the way from Java into an `.oar` (ONOS app archive) file which can be installed into ONOS, you can run

```
mvn install
```

in the `onos-apps-samples` directory.

This will produce similar output to that produced by mvn compile, but will take slightly longer since it is creating the `.oar` files as well.

For example:

```
find . -name '*.oar'
./calendar/target/onos-app-calendar-1.9.0-SNAPSHOT.oar
./carrierethernet/target/onos-app-carrierethernet-1.8.0-SNAPSHOT.oar
./database-perf/target/onos-app-database-perf-1.9.0-SNAPSHOT.oar
./ecord/co/target/onos-app-ecord-co-1.9.0-SNAPSHOT.oar
./flowtest/target/onos-app-flowtest-1.9.0-SNAPSHOT.oar
./icona/app/target/onos-app-icona-1.9.0-SNAPSHOT.oar
./icona/domainmgr/target/onos-app-icona-domain-manager-1.9.0-SNAPSHOT.oar
./icona/domainprovider/target/onos-app-icona-domain-provider-1.9.0-SNAPSHOT.oar
./ifwd/target/onos-app-ifwd-1.9.0-SNAPSHOT.oar
./ipfix/target/onos-app-ipfix-1.9.0-SNAPSHOT.oar
./oneping/target/onos-app-oneping-1.9.0-SNAPSHOT.oar
./sdx-l2/target/onos-app-sdx-l2-1.9.0-SNAPSHOT.oar
./tvue/target/onos-app-tvue-1.9.0-SNAPSHOT.oar
./uiref/target/onos-app-uiref-1.9.0-SNAPSHOT.oar
```

The `.oar` files are suitable for installation into the appropriate version of ONOS that you specified in `pom.xml`.

Note that `mvn install` **doesn't actually install** the package into ONOS! Rather you need to follow the appropriate instructions for installing and activating the app into your own ONOS system.

Application installation and activation is discussed in [Managing ONOS applications](../../administrator-guide/configuring-onos/managing-onos-applications.md).
