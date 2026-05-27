# Test Plan - Platform-Level Tests (PLAT*)

### Purpose:

The purpose of this platform test is to test ONOS on the platform level.

### Test Overview:

Objectives:

* Pull latest ONOS (image, tar ball, etc)
* Starting up ONOS
* Form a cluster
* Activate and deactivate applications after startup

Test Suite: **PLATdockertest**

| Test Case # | Description | Pass/Fail Criteria |
| --- | --- | --- |
| 0 | Pull all docker images and get a list of image tags. | Pass: No duplicate image tags, and image tag list pulled successfully. |
| 1 | Set up test parameters | Pass: Parameters are set and docker service is running. |
| 5 | Pull "onosproject/onos:latest" image from docker repo. (unused) | Pass: Image is pulled successfully. |
| 10 | Start three ONOS containers as standalone ONOS and obtain IPs of all nodes. | Pass: ONOS node IPs are obtained and container successfully started. |
| 110 | Step 1: Check default startup standalone ONOS applications status. | Pass: "drivers" app is in ACTIVE state AND all builtin apps have "INSTALLED" state. |
|  | Step 2: Form ONOS cluster with all nodes. | Pass: ONOS forms cluster with correct number of nodes. |
|  | Step 3: Check cluster startup apps status. | Pass: "drivers" app is in ACTIVE state AND all builtin apps have "INSTALLED" state |
|  | Step 4: Activate "proxyarp", "fwd", and "openflow" apps and check apps status. | Pass: Newly activated apps have "ACTIVE" state. |
| 120 | Docker Mininet Testing | Pass: Mininet Topology is successfully loaded. |
| 130 | Docker Intents Check | Pass: Intents check was successful. |
| 140 | Docker Flows Test | Pass: Flows successfully added. |
| 299 | Cleanup previous Docker testing, including deactivating "proxyarp", "fwd", and "openflow" apps, and checking app status. | Pass: Successful cleanup. Newly deactivated apps have "INSTALLED state. |
| 900 | Check ONOS log for exceptions after test. | Pass: Exception check passes. |
| 1000 | Pre/Post-test clean environment: Delete ONOS container (if existing), delete images with <none>:<none> tag (if existing). | Pass: Containers and images do not exist in docker. |
