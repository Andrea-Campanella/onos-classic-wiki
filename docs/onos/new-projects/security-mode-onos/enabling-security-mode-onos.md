# Enabling Security-Mode ONOS

Work-in-progress.

# **Enabling Security-Mode on ONOS**

## **Shortcuts (smile)**

**Note: Shortcuts are broken after conversion to BUCK build system (Dec 2016)**

To enable Security-Mode in your local ONOS environment:

$> onos-setup-karaf secure

To create a Security-Mode-enabled ONOS tarball:

$> onos-package -s -t

## **OR ... you may also ...**

## **Manually enable Security-Mode:**

## **1)** **KARAF-3400 bug fix**

 Karaf 3.0.3 uses Felix Config Admin 1.8.0 by default; however, its not compatible with Karaf (<https://issues.apache.org/jira/browse/KARAF-3400> for the details)

**Step 1: Download and Install Felix Config Admin version 1.6.0**

$> wget <http://archive.apache.org/dist/felix/org.apache.felix.configadmin-1.6.0.jar>

$> mkdir $KARAF\_ROOT/system/org/apache/felix/org.apache.felix.configadmin/1.6.0

$> mv org.apache.felix.configadmin-1.6.0.jar $KARAF\_ROOT/system/org/apache/felix/org.apache.felix.configadmin/1.6.0/

### **Step 2: Change Karaf configuration to use Felix CA ver. 1.6.0**

**<Modify Karaf /etc/startup.properties>**

$> vim $KARAF\_ROOT/etc/startup.properties

//Change the version number from 1.8.0 to 1.6.0 as shown below:

mvn\:org.apache.felix/org.apache.felix.configadmin/1.6.0 = 10

## **2)** **Install Felix Framework Security Extension (ONOS ver.)**

We’ve modified Felix Framework Security extension to enable some of the key features of Security Mode ONOS. We need to install this modified extension to the maven repository.

$> git clone <https://gerrit.onosproject.org/onos-felix>

$> cd onos-felix/framework.security

$> git checkout onos

$> mci

## **3)** **Change KARAF configurations to enable Security-Mode**

Karaf needs to be properly configured to enable Security-Mode.

**<Modify Karaf / etc / system.properties>**

**… at the very very bottom of the file**

#

# Security properties

#

# To enable OSGi security, uncomment the properties below,

# install the framework-security feature and restart.

#

java.security.policy=${karaf.etc}/all.policy    **(Uncomment these two lines)**

org.osgi.framework.security=osgi                **(Uncomment these two lines)**

#org.osgi.framework.trust.repositories=${karaf.etc}/trustStore.ks

**<Modify Karaf / etc / org.apache.karaf.features.cfg>**

featuresBoot = onos-security, …

**That’s it! Security-Mode is enabled!**

# **CLI.**

**review [app-name]**

**: print specified application’s security policy**

**review [app-name] accept**

**: accept and enforce the security policy**
