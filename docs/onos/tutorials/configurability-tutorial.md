# Configurability Tutorial

Work-in-progress. Completed page will be linked into the [Tutorials](../tutorials.md) page.

## Overview

This tutorial shows you how to incorporate tunable parameters into your component by making the link-flapping behavior of the *NullLinkProvider* from the [Provider Tutorial](provider-tutorial.md) configurable.

By completing this tutorial, you will understand:

* The usage of `@Property` and `@Modified` annotations to add and use tunable parameters
* The usage of configuration files to apply user configurations

While we use a Provider in this tutorial, the procedure described here is also applicable to applications.

As in the case of other tutorials, ${ONOS\_ROOT} refers to the project root directory of ONOS, and ${KARAF\_ROOT} refers to the installation location of Apache Karaf.

## Modifications

### 1. Modify the component POM file.

We use *Component Contexts* to pass configuration information to the component. The following should be added to the component's POM file, in this case, the Provider-specific *pom.xml*, in *${ONOS\_ROOT}/providers/null/link* :

**Provider-specific pom.xml** Expand source

```
    <!-- This is needed by ComponentContext, used for tunable configuration -->
    <dependencies>
        <dependency>
            <groupId>org.osgi</groupId>
            <artifactId>org.osgi.compendium</artifactId>
        </dependency>
    </dependencies>
```

### 2. Add support for configuration.

We make a few modifications to the `NullLinkProvider`:

**NullLinkProvider.java** Expand source

```
// new imports
import static com.google.common.base.Strings.isNullOrEmpty;

import org.osgi.service.component.ComponentContext;
import org.apache.felix.scr.annotations.Modified;
import java.util.Dictionary;

// ...<snip>...

public class NullLinkProvider extends AbstractProvider implements LinkProvider {

    private final Logger log = getLogger(getClass()); 
 
	// Attention - we need register and unregister our Class (NullLinkProvider),
	// before and after we load the config file
    @Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    protected ComponentConfigService componentConfigService;  

    // The Manager serving as communication point between the ONOS core and this Provider
    @Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
    protected LinkProviderRegistry providerRegistry;

    // The interface that defines how this Provider can interact with the core
    private LinkProviderService providerService;

    public NullLinkProvider() {
        // ProviderId is used by the core to identify this Provider
        // The schema "null" and FQDN of the Null southbound comprise this ID
        super(new ProviderId("null", "org.onosproject.provider.nil"));
    }

    @Activate
    public void activate(ComponentContext context) {
 
		//Attention - register for system-wide configurations
		componentConfigService.registerProperties(getClass());
        providerService = providerRegistry.register(this);
        deviceService.addListener(linkProvider);

        // launch exactly one LinkDriver
        if (!modified(context)) {
            log.info("Using defaults: flicker={}, eventRate={}",
                    FLICKER, DEFAULT_RATE);
            linkDriver.submit(new LinkDriver());
        }
        log.info("started");
    }

    @Deactivate
    public void deactivate(ComponentContext context) {
 
		//Attention - just unregister when deactivate our Class
		componentConfigService.unregisterProperties(getClass(),false);
        // ...
    }

    // The method called when configuration changes are made
    @Modified
    public boolean modified(ComponentContext context) {
        return false;
    }
	
    // ...<snip>...
 }
```

We note two features needed for configurability:

* **`ComponentContext context`** : Used to pass around information read from a configuration file
* **`@Modified`** : Annotation indicating that the `modified()` method should be called when configuration changes are made.

We call `modified()` from `activate()`so that the configuration file is read at module startup. Afterwards, the `@modified` annotation causes `modified()` to be called whenever the file is changed.

### 3. Annotate the tunable parameters.

The two tunable parameters for the NullLinkProvider are:

* Enable/disable link flapping
* Link flapping rate (in milliseconds)

Luckily, we had already defined the variables associated with these parameters, `flicker` and `eventRate`, so we annotate them (and change `FLICKER` to false):

**NullLinkProvider.java** Expand source

```
// new imports
import org.apache.felix.scr.annotations.Property;
 
// ...<snip>...

public class NullLinkProvider extends AbstractProvider implements LinkProvider {

    // ...<snip>...

    // Default values for tunable parameters
    private static final boolean FLICKER = false;
    private static final int DEFAULT_RATE = 3000;
    
    @Property(name = "flicker", boolValue = FLICKER,
            label = "Setting to flap links")
    private boolean flicker = FLICKER;

    @Property(name = "eventRate", intValue = DEFAULT_RATE,
            label = "Duration between Link Event")
    private int eventRate = DEFAULT_RATE;
	
    // ...<snip>...
```

### 4. Add file-parsing code.

Next, we implement `modified()` to parse out the values set for these parameters.

**NullLinkProvider.java - modified()** Expand source

```
    @Modified
    public boolean modified(ComponentContext context) {
        // if there's no file, fall back to defaults
        if (context == null) {
            log.info("No configs, using defaults: flicker={}, eventRate={}",
                    FLICKER, DEFAULT_RATE);
            return false;
        }

        Dictionary<?, ?> properties = context.getProperties();
        boolean flickSetting;
        int newRate;

 
 
        // try to extract values keyed on the parameters' names
        try {
            String s = (String) properties.get("flicker");
            flickSetting = isNullOrEmpty(s) ? flicker : s.trim().equals("true");
            s = properties.get("eventRate");
            newRate = isNullOrEmpty(s) ? eventRate : Integer.parseInt(s.trim());
        } catch (Exception e) {
            log.warn(e.getMessage());
            flickSetting = flicker;
            newRate = eventRate;
        }

        if (flicker != flickSetting) {
            flicker = flickSetting;
        }

        // launch a LinkDriver with the new values, if they were changed
        if (flicker) {
            if (eventRate != newRate) {
                eventRate = newRate;
            }
            linkDriver.submit(new LinkDriver());
            log.info("Using settings: flicker={}, eventRate={}", flicker,
                    eventRate);
            return true;
        }
        return false;
    } 
```

### 5. Verification

We can now rebuild the Null Providers to test the configurability of this Provider.

### 6. Modifying the cfgdef file

Use your favorite editor to modify  $ONOS\_HOME/providers/null/link/target/classes/org/onosproject/provider/nil/link/impl/NullLinkProvider.cfgdef

```
# This file is auto-generated by onos-maven-plugin
flicker|BOOLEAN|false|Setting to flap links
eventRate|INTEGER|3000|Duration between Link Event
```

You can modify one or both parameters and watch for the impact.
