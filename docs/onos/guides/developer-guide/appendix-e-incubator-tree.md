# Appendix E: Incubator Tree

# Incubator Tree Layout

The ONOS incubator tree is a place that allows contributors to add to the API and to the Core implementations of ONOS in a creative way and on their own time-line while making their interfaces/API exempt from the deprecation policy, meaning that the API can change from release to release. This incubator tree will not effect the main line ONOS deliverables, yet can be used as a showcase for new features and APIs.  
  
The idea is to set up *onos-incubator-api* and *onos-incubator-net|store*modules, with a corresponding Java package namespace *org.onosproject.incubato*r. This could be then viewed as a sandbox or a nursery of future core code. This will allow physical separation of such code for certain production environments, but at the same time will allow experimenters to treat this as part of the ONOS code.  
  
This is in addition to the existing capability where apps can expose their own APIs that can be consumed by other parts of the app, or by other apps.  
  
The following depicts the module dependencies:

![](https://docs.google.com/a/onlab.us/drawings/d/s7uuWPc1lSBE66XWZuHYiWg/image?w=435&h=249&rev=62&ac=1)

## Promotion Notes

To aid developers with migrating their apps that may have previously used code in the incubator area, any API code that will be moved will leave behind a series of tombstone classes or interfaces with pointers to their replacements in core.

# 

# Current Incubator Projects

* Network Config  
  A model and a set of services to track network configurations and changes to them.
* Tunnel Resources  
  A model and a set of services to implement a tunnel abstraction for ONOS.
* Label Resources
