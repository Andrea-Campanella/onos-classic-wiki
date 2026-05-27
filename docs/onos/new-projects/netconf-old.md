# NETCONF-old

# 

# Team

Add your name if you think it belongs here.

| Name | Organization | Email |
| --- | --- | --- |
| Marc De Leenheer | ON.Lab | marc@onlab.us |
| Hiral Amodia | Happiest Minds Technologies | Hiral.Amodia@happiestminds.com |
| Kapil Aare | Happiest Minds Technologies | Kapil.Aare@happiestminds.com |
| Sanjay S | Happiest Minds Technologies | Sanjay.S@happiestminds.com |
| Samir Anand | Happiest Minds Technologies | Samir.Anand@happiestminds.com |

# Proposed work

Implement NETCONF southbound protocol handler (core NETCONF & notification mechanism), and test against various software and hardware servers. Demonstrate NETCONF capabilities through simple configuration use case.

Possible extensions: integrate YANG processor to automatically expose configuration interface of device. Build use case around this feature, e.g., use ACL model to control forwarding in hybrid network composed of OpenFlow and legacy switches.

1. Build in the SB NETCONF protocol handler
   1. Build the SB NETCONF protocol handler. Potentially leverages an open source NETCONF library.
   2. Add in the missing hooks into ONOS for NETCONF session management and related stuff.
2. Model above NETCONF
   1. On top of this NETCONF protocol handler, pick a few standard models from the ones that exist and builds infra needed with guidance from ON.Lab team
   2. Work with ONOS vendor partners to support at least a few vendor specific models.

# Technical Material

1. [Design document](netconf-old/design-document.md)
2. Technical charts, diagrams, etc.

# Meetings and Minutes

Go [here](netconf-old/meeting-schedule-and-minutes.md) to review the minutes of past meetings.
