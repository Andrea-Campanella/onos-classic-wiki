# Creating your own apps

ONOS is an extensible and programmable network control platform that supports the development of arbitrary software packages. The switch from fixed-function networking platforms to programmable SDN platforms is analogous to the switch from fixed-function "feature" phones to smartphones, and ONOS is designed to facilitate an expansive ecosystem of network applications that are developed independently from the core ONOS system, much as user applications are developed separately from the kernel in desktop and server systems.

One way to get started with developing ONOS applications is to try modifying the existing [ONOS Sample Applications](building-the-onos-sample-apps.md). This is a good way to get your feet wet by experimenting with changes to existing functionality, and may be easier than creating an entirely new application from scratch.

If you wish to create an application from scratch, or wish to create a small program with minimal code and functionality, you can start with a "template application" which uses a Maven archetype to create skeleton code which doesn't do much beyond setting up the basic infrastructure that can be compiled and installed into ONOS, and can interact with the ONOS CLI and GUI. Any additional functionality can be added as desired until it does what you want.

Creating a template application is described in the [Template Application Tutorial](../../../tutorials/template-application-tutorial.md).
