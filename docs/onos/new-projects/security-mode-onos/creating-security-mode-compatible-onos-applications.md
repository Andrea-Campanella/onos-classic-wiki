# Creating Security-Mode compatible ONOS applications

When enabled in Security-Mode, ONOS activates security subsystem, which parses and enforces security policy to each application.

Since the security subsystem requires ONOS operators to review and approve the security policy upon the activation of each application,the application must have its security policy specified within the application package.

# **Specifying security policy in app.xml**

ONOS in security-mode requires all the applications to have a security policy specified within app.xml.

For each ONOS application, the developer must specify four different types of security policy.

1. Application role
2. Application permissions
3. OSGi-specific permissions
4. Java native permissions

### Application role

Currently there are two different application roles available, USER and ADMIN.

When given ADMIN role, an application is granted the permissions to access All the ONOS Northbound services including administrative services.

Given USER role, an application is granted the permissions to access ONLY non-administrative Northbound services.

### Application permissions

We have derived various ONOS application permissions based on all the Northbound APIs available. (up to ONOS v.1.5.1)

A complete list of the app permissions can be found [here](onos-application-permissions.md).

In order to provide sufficient understanding of each application's capability, app permissions are named after "type of ONOS resource" + "action".

For example, if FLOWRULE\_WRITE permission is granted to an ONOS app, the app can access the NB APIs that issues flowrules.

### OSGI-specific permissions

OSGi-specific permissions may be specified as well as ONOS-specific ones as introduced above.

OSGi specific permissions can be found [here](https://osgi.org/javadoc/r4v43/core/org/osgi/framework/package-summary.html).

For example, if an application needs an access to arbitrary OSGi service, "org.foo.ExampleService", which is not one of the Northbound services,

OSGi's ServicePermission to "get" "org.foo.ExampleService" must be granted to the application.

### Java native permissions

Just like OSGi permissions, Java native permissions may also be granted to ONOS applications.

If your application needs to access the local file system to leave a log file, FilePermission must be granted to the app.

If your application establishes a socket connection with any external entity (although such an activity is potentially unsafe), SocketPermission must be given.

# ****Creating SM-compatible application packages****

Please refer to [this guide](../../guides/architecture-and-internals-guide/application-subsystem.md) to create application packages, and simply specify your own security policy within the app.xml.

The schema for app.xml and a example app.xml are provided below.

## **Resources**

**app.xml (application manifest) schema for SM-compatible ONOS application: [schema.xsd](../../../assets/schema.xsd)**

**example app.xml with security policy: [app.xml](../../../assets/app.xml)**
