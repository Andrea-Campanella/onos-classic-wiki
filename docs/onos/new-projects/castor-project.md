# Castor Project

# 

**NOTE: For Castor application, use-cases and documentation, please log on to the website [www.castor.live](http://www.castor.live)**

**Primary Contact: Himal Kumar , E-Mail: himal@castor.live**

# Introduction

Project CASTOR is a controller-based architecture for interconnections in data centres, specifically targeting two market segments:

(a) public peering between domains (Autonomous Systems) at an Internet Exchange Point (IXP)

(b) private peering between enterprises and cloud service providers.

The advantages for the public peering use case, compared to a traditional model (based on a route server together with a L2 learning switch) are:

* Better switch hygiene or IXP policy enforcement (e.g. enforcing a single router MAC address per port, enforcing only the allowed traffic types, etc.
* ARP flood management (ARP requests can be sent only to the appropriate peer rather than broadcast over the fabric)
* Improved telemetry (e.g. reporting traffic volume between every pair of peers).

Advantages for the private peering use-case for cloud-connectivity, compared to the current model that uses a fabric with distributed control, are:

* Scaleout by adding data-plane elements all managed by a single logical controller
* Management of on demand, elastic bandwidth between peers
* Web-based self-provisioning by customers.
