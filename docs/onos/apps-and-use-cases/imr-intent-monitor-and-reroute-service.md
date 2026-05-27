# IMR - Intent Monitor and Reroute service

## Overview

Intent Monitor and Reroute (IMR) application offers ONOS applications and users the possibility to expose statistics and re-routing capabilities, of specific intents, to external Off-Platform Application (OPA).

The OPA can re-route those monitored intents based on the collected flow level statistics optimizing a global network objective.

IMR requires little code modification to the ONOS application that wants to take advantage from the OPA, it doesn't affect the way the application submits intents to the Intent Framework, IMR only needs to be aware of which Intents the ONOS application wants to expose to the OPA and then it will automatically collect statistics and re-route intents.

## Tutorial

It's possible to try an example of a possible OPA logic to be interconnected with the IMR service by following the instructions provided [here](https://github.com/ANTLab-polimi/onos-opa-example).
