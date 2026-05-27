# ONOS : An Overview

This section provides a high-level view of ONOS, and its general design points.

## Design Goals

ONOS is a multi-module project whose modules are managed as OSGi bundles. ONOS is designed with a few goals in mind:

* Code Modularity : It should be possible to introduce new functionalities as self-contained units.
* Configurability : It should be possible to load and unload various features, whether it be at startup or at runtime.
* Separation of Concern : There should be clear boundaries between subsystems to facilitate modularity.
* Protocol agnosticism : It, and its applications, should not be bound to specific protocol libraries or implementations.

We take a succinct look at each below.

### Code Modularity

The project is comprised of a set of sub-projects, each with their own source tree that can be built independently. To do this, the ONOS source tree is organized in a hierarchical fashion that takes advantage of Maven's notion of a hierarchical POM file organization. Each sub-project has its own *pom.xml* file, and intermediate directories have parent aggregate *pom.xml* files. The latter contains shared dependencies and configurations for those sub-projects, enabling them to be built independent of unrelated sub-projects. The ONOS root contains the top-level pom file used to build the full project and all of its modules. 

For implementation details of the source tree organization, refer to [Appendix C](../developer-guide/appendix-c-source-tree-organization.md) of the Developer's Guide.

### Configurability

ONOS is written to leverage Apache Karaf as its OSGi framework. In addition to dependency resolution at startup and dynamic module loading at runtime, Karaf provides the following:

* Enable use of standard JAX-RS API to develop our REST APIs and make them secure
* The notion of features as a set of bundles allowing assembly of custom setups
* Strict semantic versioning of code bundles, including third-party dependencies
* Local and remote ssh console with easily extensible CLI
* The notion of run-time log levels

### Separation of Concern

ONOS is partitioned into :

1. Protocol-aware network-facing modules that interact with the network
2. Protocol-agnostic system core that tracks and serves information about network state, and
3. Applications that consume and act upon the information provided by the core

Each of the above are tiers in a layered architecture, where network-facing modules interact with the core via a *southbound (provider) API*, and the core with the applications via the *northbound (consumer) API*. The southbound API defines protocol-neutral means to relay network state information to the core, and for the core to interact with the network via the network-facing modules. The northbound API provides applications with abstractions that describe network components and properties, so that they may define their desired actions in terms of policy instead of mechanism. 

### Protocol Agnosticism

If ONOS needs to support a new protocol, it should be possible to build a new network-facing module against the southbound API as a plugin that may be loaded into the system.

## The Remaining Sections

The remaining sections of the Architecture Guide elaborate on the design and implementation of the subsystems that make up the above-mentioned tiers, and the OpenFlow provider that ships with ONOS.

Some terms and conventions used in the rest of the guide are:

* "infrastructure" and "network" refer to the network controlled by ONOS, and may be physical, virtual, or emulated.
* A "device" is a network node, such as a switch, router, access point, or middle box. They usually have multiple interfaces, and may be software or hardware.
* A "path" is a set of one or more links. The links must be adjacent.
* Proper nouns, such as "Network" and "Link", are ONOS's representations of the infrastructure component of the same name.

It is impossible to avoid referring back to the codebase when we speak of implementation. The following conventions are used with regards to code:

* Class, Interface, and Object names are monotype, e.g. `DeviceManager.`
* Method names are monotype and end in parentheses, e.g. `emit().`
* Inlined package names are surrounded by square brackets, e.g. `[org.onlab.onos.net.DeviceId]`

 

 

---

 [Home : Architecture Guide](../architecture-and-internals-guide.md)  
[Next : System Components](system-components.md)

---
