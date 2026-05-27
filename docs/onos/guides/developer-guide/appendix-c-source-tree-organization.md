# Appendix C : Source Tree Organization

The following is a summary of the organization of the ONOS source tree. This section is not intended to be comprehensive list of all packages and files, but rather an overview to provide developers with a general idea of how ONOS is organized (think `man hier` on UNIX-like operating systems).

## POM Hierarchy

ONOS is organized as multiple projects, each with its own pom.xml file so that it can be built with Maven. The pom.xml files are organized in a hierarchy, so that projects with shared dependencies and configurations can be built from a parent pom.xml file defined closer to the root.The root of the source tree contains the top-level pom file that builds all of the projects comprising ONOS.

Since the POM hierarchy reflects the logical organization of ONOS, it is used as the reference for this page.

## Project Layout

The following is the rough layout of the project. The indentation level reflects directory level depth for directory names. For example, "calendar" is ***onos-next/apps/calendar/***.

Similarly, the bundle names correspond to the POM files for the project modules; all bundles indented under a bundle may be built by building the latter, using its POM file. For example, if one wishes to build just the OpenFlow subsystem components:

```
cd onos-next/providers/openflow && mvn clean install
```

Please note that neither the full file hierarchy nor all modules are shown. '-' denotes directories that do not contain POM files (i.e. not modules), or are deprecated. Entries in italics are not modules, but are described for convenience.

### Bundle name

* onos
  + onos-apps
    - onos-app-bgprouter
    - onos-app-calendar
    - onos-app-config
    - onos-app-database-perf
    - onos-app-demo
    - onos-app-election
    - onos-app-foo
    - onos-app-fwd
    - onos-app-grouphandler
    - onos-app-ifwd
    - onos-app-intent-perf
    - onos-app-metrics
    - onos-app-mobility
    - onos-app-oecfg
    - onos-app-optical
    - onos-app-proxyarp
    - -
    - onos-app-routing
    - onos-app-routing-api
    - onos-app-sdnip
    - -
    - onos-app-tvue
  + onos-cli
  + onos-core
    - onos-api
    - onos-core-common
    - -
    - onos-core-net
    - onos-core-store
    - -
  + onos-docs
  + onos-features
  + -
    - -
    - -
  + onos-of
    - onos-of-api
    - onos-of-ctl
    - onos-of-drivers
  + onos-providers
    - onos-host-provider
    - onos-lldp-provider
    - onos-null-providers
    - -
    - onos-of-providers
  + -
    - maven-source-plugin
    - -
    - -
    - -
    - -
  + onlab-utils
    - onlab-junit
    - onlab-misc
    - onlab-netty
    - onlab-nio
    - onlab-osgi
    - onlab-rest
    - onlab-thirdparty
  + onos-web
    - onos-rest
    - onos-gui

### Directory Name

* onos-next
  + apps
    - bgprouter
    - calendar
    - config
    - database-perf
    - demo
    - election
    - foo
    - fwd
    - grouphandler
    - ifwd
    - intent-perf
    - metrics
    - mobility
    - oecfg
    - optical
    - proxyarp
    - proxyndp
    - routing
    - routing-api
    - sdnip
    - test
    - tvue
  + cli
  + core
    - api
    - common
    - json
    - net
    - store
    - trivial
  + docs
  + features
  + net
    - api
    - core
  + openflow
    - api
    - ctl
    - drivers
  + providers
    - host
    - lldp
    - null
    - of
    - openflow
  + tools
    - build
    - dev
    - package
    - test
    - tutorials
  + utils
    - junit
    - misc
    - netty
    - nio
    - osgi
    - rest
    - thirdparty
  + web
    - api
    - gui

### Description

* Open Network Operating System root project
  + ONOS sample applications
    - BGP router application
    - ONOS simple calendaring REST interface for intents
    - ONOS simple network configuration reader
    - ONOS partitioned database perf test app bundle
    - ONOS demo app bundle
    - ONOS app leadership election test
    - ONOS application for miscellaneous experiments
    - ONOS simple reactive forwarding app
    - ONOS sample application using group service
    - ONOS simple reactive forwarding app that uses intent service
    - ONOS intent perf app bundle
    - ONOS metrics applications
    - ONOS simple Mobility app
    - Standalone utility for converting ONOS JSON config to OE-Linc JSON config
    - ONOS application for packet/optical deployments
    - ONOS simple proxy arp module
    - -
    - Libraries for routing applications
    - API for routing applications
    - SDN-IP peering application
    - -
    - ONOS simple topology viewer
  + ONOS administrative console command-line extensions
  + ONOS Core root project
    - ONOS network control API
    - ONOS utilities common to the core modules
    - -
    - ONOS network control core subsystems
    - ONOS Core Store subsystem
    - -
  + ONOS Java API documentation
  + ONOS Apache Karaf feature definitions
  + -
    - -
    - -
  + ONOS OpenFlow Protocol subsystem
    - ONOS OpenFlow controller subsystem API
    - ONOS OpenFlow controller subsystem API
    - ONOS OpenFlow switch drivers & factory
  + ONOS information providers & control/management protocol adapter
    - ONOS host tracking provider
    - ONOS LLDP Link Discovery
    - ONOS null protocol adapters
    - -
    - ONOS OpenFlow protocol adapters
  + *Miscellaneous utilities and scripts*  
    - *release, distribution and packaging utilities*
    - *development environment sample configurations*
    - *remote ONOS instance management*
    - *onos-\* utilities and cell definition files*
    - *configuration files for tutorials*
  + Domain agnostic ON.Lab utilities
    - ON.Lab JUnit test utilities
    - Miscellaneous ON.Lab utilities
    - Network I/O using Netty framework
    - Fast network I/O using Java NIO
    - ON.Lab OSGI utilities
    - ON.Lab JAX-RS utilities
    - ONLab third-party dependencies
  + ONOS web root project
    - ONOS REST API
    - ONOS Web GUI

---

[Previous : Appendix B : REST API](appendix-b-rest-api.md)  
[Next : Appendix D : Troubleshooting Multi-module Projects](appendix-d-troubleshooting-multi-module-projects.md)

---
