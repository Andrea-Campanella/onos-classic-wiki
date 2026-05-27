# Appendix I - GUI2 Development

## Legacy ONOS GUI

Legacy ONOS GUI (aka GUI1) is the primary GUI for ONOS for all 1.x releases.

It still remains available in ONOS 2.x but is not started by default. GUI2 is started by default and should be disabled before GUI1 is started.

It is AngularJS 1.x based with Java backend - Web Sockets. Since Angular 1.x is now obsolete GUI2 was created to have the same look and feel as the legacy GUI where possible.

## ONOS GUI2

ONOS GUI2 was developed to replace the legacy ONOS GUI1. It is the default GUI for ONOS 2.x releases.   
It is Angular 7.x based with same Java backend and Web sockets  
It has been divided in to Framework library, Topo Library and main app

## Documentation

Instead of adding material here to the Wiki, documentation is in [README.md](http://README.md) files in the project itself, at:

<https://github.com/opennetworkinglab/onos/tree/master/web/gui2>  
  
<https://github.com/opennetworkinglab/onos/tree/master/web/gui2-fw-lib>  
  
<https://github.com/opennetworkinglab/onos/tree/master/web/gui2-topo-lib>

There is also an external documentation (in the form of Stack Overflow answer) to build a custom gui2 app using source code with two types of implementations. The link for the same is below :-

<https://stackoverflow.com/questions/62698926/getting-error-while-clicking-on-custom-gui-navigation-item-in-onos-2-4-0>

## Archetype

For creating a new GUI2 application inside ONOS - please use the **ui2 archetype**  
General Instructions at [https://wiki.onosproject.org/display/ONOS/Template+Application+Tutorial](../../tutorials/template-application-tutorial.md)  
and the UI2 archetype is at <https://github.com/opennetworkinglab/onos/tree/master/tools/package/archetypes/ui2>

## ONF Connect 2019 presentation

A general overview of GUI2 is available in the slides [here](https://www.opennetworking.org/wp-content/uploads/2019/09/4.30pm-Sean-Condon-Extending-and-Reusing-the-New-ONOS-GUI2.pdf),

with the accompanying video presentation from ONF Connect 2019 at
