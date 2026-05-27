# Component Configuration

## Overview

OSGi provides a framework for individual software components to declare certain parameters to be configurable. This framework allows changing these parameters in-flight and tracks their values across system restart. However, this occurs only on the local container, which in ONOS's case is Apache Karaf. For this reason, ONOS provides a subsystem, which overlays the OSGi mechanism, but which manages the configurations in a distributed fashion across the entire ONOS cluster. This assures that all ONOS cluster instances are running using the same configuration and at the same time provides a convenient means to view the state of the configuration parameters.

This subsystem continues to use the OSGi mechanism to persistently track configurable parameters in the local instance context and to notify components when the parameters change. In this way the application components can continue to use the standard and well-understood OSGi configuration via *ComponentContext.* Furthermore, if components use the Apache Felix compile-time *@Property* annotation, the ONOS build process generates a configuration catalog as a jar/bundle resource, which the component can register, allowing the ONOS administrator to see what parameters can be configured. The component configuration subsystem will then make sure that when a change is made on one ONOS instance, the same change will be propagated across the entire ONOS cluster and reflected on all ONOS instances in that cluster.

## Component Code Example

To allow parameters to be configurable, components must first designate their fields using the *@*Property** annotation as follows:

```
private static final int DEFAULT_MAX_EVENTS = 1000;

@Property(name = "maxEvents", intValue = DEFAULT_MAX_EVENTS,
        label = "Maximum number of events to accumulate")
private int maxEvents = DEFAULT_MAX_EVENTS;

private static final int DEFAULT_EMAIL = "onos-dev@onosproject.org";

@Property(name = "notificationEmail", value = DEFAULT_EMAIL,
          label = "Notification email address")
private String notificationEmail = DEFAULT_EMAIL;
```

In order to allow these parameters to be changed dynamically, a component should define a *modified* method, annotated using *@Modified* compile-time annotation as in this example:

```
@Modified
public void modified(ComponentContext context) {
    Dictionary<?, ?> properties = context.getProperties();

    String s = Tools.get(properties, "newMaxEvents");
    maxEvents = Strings.isNullOrEmpty(s) ? DEFAULT_MAX_EVENTS : Integer.parseInt(s.trim())

    s = Tools.get(properties, "notificationEmail");
    notificationEmail = Strings.isNullOrEmpty(s) ? DEFAULT_EMAIL : s;
    ...
}
```

Note that there is a slight anomaly in the OSGi framework where sometimes the parameters for fields of type other than *String* are returned from the properties dictionary as their specific type, i.e. *Integer*, *Boolean*, and sometime the value for the same parameter will be returned as a *String*. This is why the above example uses the *Tools.get()* method for retrieving the property value. This method forces all values to be returned as a *String*, allowing the component code in the *modified* method to be simpler and safer. It is recommended that all configurable components use the same method.

Finally, the component should register and unregister the configuration properties from its *activate* and *deactivate* methods:

```
@Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
protected ComponentConfigService cfgService;

@Activate
public void activate(ComponentContext context) {
    cfgService.registerProperties(getClass());
    modified(context);
    ...
}

@Deactivate
public void deactivate(ComponentContext context) {
    cfgService.unregisterProperties(getClass(), false);
    ...
}
```

## Maven Example

Modules that contain configurable components should contain the following configuration of *onos-maven-plugin*:

```
<plugins>
    ...
    <plugin>
        <groupId>org.onosproject</groupId>
        <artifactId>onos-maven-plugin</artifactId>
        <version>1.9</version>
        <executions>
            <execution>
                <id>app</id>
                <phase>generate-resources</phase>
                <goals>
                    <goal>cfg</goal>
                </goals>
            </execution>
        </executions>
    </plugin>
    ...
</plugins>
```

This Maven plugin will generate the jar/bundle resource containing the dictionary of configurable properties using the annotations. This is then used by the CLI, and in the future GUI, to present the ONOS administrator with a list of configurable parameters, description of their purpose, their current and default values. This configuration is already contained in the root ONOS *pom.xml* and consequently any child subproject will inherit this capability. Therefore, only applications outside of the ONOS source-code will need to include the above in their Maven *pom.xml* file(s).

## CLI Command

To allow configuration of properties via CLI, ONOS provides a command-line handler with the following usage:

* *cfg* - lists class names of all configurable components that have registered with the subsystem
* *cfg get* - lists all class names and their properties as a full dump
* *cfg get componentClass* - lists all properties of the specified class
* *cfg get componentClass name* - lists the value of the specified component property
* *cfg set componentClass name value* - sets the value of the specified component property
* *cfg set componentClass name* - clears the value of the specified component property restoring it to its default value

## REST API

Presently, there is no REST API access to this functionality, but one will be provided as part of the next (Cardinal) release.
