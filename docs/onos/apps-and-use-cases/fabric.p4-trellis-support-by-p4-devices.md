# fabric.p4: Trellis support by P4 devices

NOTE: WORK IN PROGRESS

# Background & Goal:

Currently, the Trellis project is based on fixed-function pipelines controlled using the OpenFlow protocol. Developers need to follow the fixed-function pipeline specification when they add new features to Trellis.

Fixed-function pipeline support may require flows and groups chaining.  The controller needs to maintain different chains of flows and groups; different chain may have a relationship.  Also, the fixed-function pipeline spec already defined how to use the pipeline. Developers need to follow the spec to define flows and groups for different network scenario (e.g., Bridging, Routing). It is hard to add a new scenario if the pipeline does not support it.

There is a lot of work done in ONOS about design and maintenance of flows and groups for different pipelines. However, the maintain cost increase significantly when adding new chips/pipelines/features.

The goal of fabric.p4 (fabric pipeline) is to provide simplified ONOS pipeliner implementation and support current Trellis project. Applications on top of the fabric pipeline should not need to be modified.

# Outline:

#### [Pipeconf](fabric.p4-trellis-support-by-p4-devices/pipeconf.md)

#### [Pipeline design](fabric.p4-trellis-support-by-p4-devices/pipeline-design.md)

#### [Try fabric.p4 with ONOS and bmv2](fabric.p4-trellis-support-by-p4-devices/try-fabric.p4-with-onos-and-bmv2.md)

# Future work:

* IP Multicast
* VLAN translation
