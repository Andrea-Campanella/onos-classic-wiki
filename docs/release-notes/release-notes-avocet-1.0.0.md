# Release Notes - Avocet 1.0.0

# Avocet Release

Version: 1.0.0

Release Date: 5th December, 2014

Download [here](../onos/downloads.md)

## About Avocet Release

Avocet is the first open source release for ONOS. It is an important milestone in the journey to bringing SDN to service provider and other mission critical networks. Developers and architects at ON.Lab and partner companies spent countless hours solving complex distributed systems problems and designing and developing the architecture of this first version. The first release of ONOS has a clean-slate, modular architecture with a distributed core for high availability, performance and scale-out. It provides Application Intent Framework- a high-level, network agnostic programmatic abstraction and interface.

Having said that, a good set of release notes should not only contain what got done, but also a candid assessment of where things fell short along with the plan to get these remaining tasks done. What got done in the Avocet release of ONOS was inline with the following priorities:

* Release ONOS with coherent and modular architecture
* Enable and demonstrate high-availability operation
* Enable sustained pursuit of performance and scale objectives
* Enable development of apps and engagement of SDN community
* Demonstrate SDN-IP & Packet-Optical use cases
* User Interface

We fell short in delivering the performance at scale we had hoped to provide and a comprehensive set of associated measurements. But based on the current distributed architecture and what has been demonstrated with prior prototypes of ONOS and the preliminary measurements with Avocet release, these performance targets seem well within reach and working towards these will be the focus of the next release Blackbird ( Feb 2015) and in fact beyond that as a sustained effort to always improve and push the limits of performance and scale.

Avocet will always remain a special release. It is the release that was open sourced and brought in each one of you into the ONOS community to help ONOS become richer, more robust, faster and a driving force for SDN adoption!

## What's in Avocet Release?

* [ONOS with the following key features](../onos/guides/architecture-and-internals-guide/onos-an-overview.md)

+ high-availability\*, scalability\*, performance\*
+ northbound abstractions ([Application Intent Framework](https://wiki.onosproject.org/display/ONOS/The+Intent+Framework))
+ southbound abstractions (OpenFlow adapters)
+ [modular code-base](https://wiki.onosproject.org/display/ONOS/Segment+Routing)
+ GUI

* Open source

+ ONOS code-base on GitHub
+ documentation & infrastructure processes to engage the community

* Use-case demonstrations

+ [SDN-IP](../onos/apps-and-use-cases/sdn-ip.md), [Packet-Optical](../onos/apps-and-use-cases/packet-optical.md)
+ Note - [Segment Routing](https://wiki.onosproject.org/display/ONOS/Segment+Routing) use case code is in a separate repo [here](../onos/apps-and-use-cases/cord-leaf-spine-fabric-with-segment-routing/archived-onfs-spring-open-project/installation-guide.md). It will be in mainstream ONOS in Blackbird release.
+ [NFaaS POC](../onos/apps-and-use-cases/cord-central-office-re-architected-as-a-datacenter/nfv-nfaas.md)

* Sample applications

  + reactive forwarding, mobility, proxy arp

*\*More work on this in Blackbird release*

## What did not get done for Avocet Release and is next for ONOS in Blackbird release (February 2015)?

* Prove out performance at scale

+ testing with real hardware
+ provide comprehensive assessment

* Continue to increase robustness

+ defects, edge-cases, additional failure scenarios
+ continuous testing framework

* Segment Routing use-case

+ Is available for use on an older version of ONOS and will be ported to the released version of ONOS in Blackbird release.

* REST API & Security
* Support for OpenFlow 1.3 multiple-tables ( addressed with bringing in segment routing into mainstream ONOS)

## License

ONOS is distributed under the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0).

## Code Audit Results (Black Duck)

Below are the compatibility reports (pdf) powered by [Black Duck Software](http://www.blackducksoftware.com).

* [Summary Report](../assets/summary.pdf)
* [BOM Report](../assets/bom.pdf)
* [Legal Report](../assets/legal.pdf)
* [All reports](../assets/combined-report.pdf) in one PDF file

## Installation

Installation details can be found in the [User's guide](https://wiki.onosproject.org/display/ONOS/User%27s+Guide) and [Developer Guide](../onos/guides/developer-guide.md).

## Javadocs

Javadocs for the Avocet release can be found [here](http://api.onosproject.org/1.0.0/).

## Bugs and Known Issues

All bugs for Avocet release are tracked in JIRA. You can view these bugs [here](https://jira.onosproject.org/secure/RapidBoard.jspa?rapidView=1&view=planning&selectedIssue=ONOS-144&quickFilter=12&versions=visible).
