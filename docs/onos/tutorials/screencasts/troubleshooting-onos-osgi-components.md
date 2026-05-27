# Troubleshooting ONOS OSGi components

## [YouTube Video](https://www.youtube.com/watch?v=x3sE17r78GQ)

## Overview

When developing new subsystems for ONOS, whether they are part of the core or part of an application, developers may encounter a number of issues with respect to activation of components or loading of OSGi bundles and Apache Karaf features.

This screencast will show you how to use the various Apache Karaf tools for troubleshooting such issues.

## Service Component Runtime

ONOS core components use OSGi Service Component Runtime, or SCR, for activation of components and for auto-wiring components together.

SCR operation is driven by XML files located in the classes/OSGI-INF folder of each OSGi bundle. For example, let’s examine the *PathManager.xml* file from the *core/net* module. This file identifies the *PathManager* class as a component, which should be activated immediately, meaning as soon as possible. It also indicates that the *PathManager* provides a service defined by the *PathService* interface and that it requires two references, *TopologyService* and *HostService*.

While these files can be created by hand, ONOS code-base instead uses Apache Felix compile-time annotations, in conjunction with `maven-scr-plugin` to generate these files at build-time.

## SCR Annotations

For example, if we were to examine *PathManager.java*, we can see that the class is annotated with *@Component* and *@Service* annotations. These imply that the class is a component, which should be activated as soon as possible and that this class offers service advertised as all implemented interfaces, which in this case is just *PathService*.

Similarly, we can see that *PathManager* requires two other services,*TopologyService* and *HostService* as evidenced by the *@Reference* annotation. The mandatory unary value of the cardinality property implies that *PathManager* will not be activated until both of these references have been satisfied; meaning until these two services become available.

When the requirements are met, the *activate* method, annotated by *@Activate* will be invoked. Conversely, when either of the requirements are no longer satisfied, or when the PathManager component is explicitly deactivated, the *deactivate* method, decorated with *@Deactivate* annotation, will be invoked.

You can see the correspondence between the annotations in this source file and the information in the generated XML file that we examined earlier.

## SSH Console

One way to interact with the SCR subsystem, is via the ONOS Apache Karaf ssh console. For example, the scr:list command provides a listing of all known components and their current state.

Furthermore, the `scr:activate` and `scr:deactivate` commands can be used to manually activate and deactivate specific components.

If we were to deactivate the HostManager component, and then list the components, we will see that number of them will now show with state `UNSATISFIED`; *PathManager* component will be among those.

Displaying details of *PathManager* component, via scr:details command, will reveal that the *hostService* reference is unsatisfied, which is the reason why the component is no longer active.

Activating the *HostManager* component will now result in all components returning back to `ACTIVE` state, including the *PathManager*.

Similarly, you can examine the loaded OSGi bundles via `bundle:list` command and likewise for Apache Karaf features, via `feature:list` command.  Just like with components, bundles and features can be stopped, started and examined. However, it is highly recommended not to use these commands directly, and instead use the onos:app command to manage software.

This will allow the software to remain in step for all instances of an ONOS cluster; otherwise, the software configuration could drift apart between different ONOS instances.

## Web Console

Similar capability to list bundles, features and components is available from the Apache Karaf web-console, which can be accessed at the following URL:

<http://server:8181/system/console>

When presented with login prompt, simply enter karaf for both username and for password. These are the default Apache Karaf credentials.

The main screen shows the loaded bundles and their state. To see the state of the components, select the Components item from the Main menu. Clicking on a component will show you its details, similar to the `scr:details` command. You can also use the *Play/Stop* buttons to start and stop each component.

## Conclusion

These tools come in very handy when developing software for the ONOS platform. There are times when some components may fail in their activation and this can result in a cascading failure where a number of components suddenly appear to be unavailable.  The ONOS log files in conjunction with the web-console or the ssh console can be used to diagnose the problem.

I hope you found this screencast informative… Have a great day… and good luck with troubleshooting!
