# Security advisories

1. [Security vulnerabilities fixed in ONOS](#Securityadvisories-svlist)
2. [Reporting security vulnerability in ONOS](security-advisories/security.md)
3. [ONOS Security Response team](security-advisories/security.md)

# Security vulnerabilities fixed in ONOS

This page lists all security vulnerabilities fixed in ONOS. Each vulnerability is assigned a security impact rating on a four-point scale (low, moderate, important and critical). The versions that are affected by each vulnerability are also listed.

You can find the template demonstrating the structure of advisories [here](security-advisories/security-advisory-templates.md).

## [Important] [CVE-2018-12691] onos-acl: Data plane access control bypass

### Description

It was found that the ONOS access control application (onos-acl) was vulnerable to a time-of-check to time-of-use race condition that permitted an end host to bypass the intended data plane access control policy. A malicious end host could send a semantically invalid packet into the data plane to corrupt the host information base, which prevented onos-acl from instantiating a flow deny rule.

### Affected versions

ONOS 1.12.0, 1.13.0 are confirmed to be affected.

### Patch commit(s)

<https://gerrit.onosproject.org/#/c/18867/>

### Patched versions

Patches have been committed to 1.12, 1.13 and will be included in future builds.

### Credit

Benjamin E. Ujcich (University of Illinois at Urbana-Champaign) in cooperation with Richard Skowyra (MIT Lincoln Laboratory) and Hamed Okhravi (MIT Lincoln Laboratory)

## [Important] [CVE-2017-1000081] Unauthenticated upload of applications

### Description

It was found that ONOS allows the upload and execution of applications via the ONOS UI without authentication.

### Affected versions

ONOS 1.8.0, 1.9.0 are confirmed to be affected.

### Patch commit(s)

<https://gerrit.onosproject.org/#/c/13830/>

### Patched versions

Patches has been committed to 1.8, 1.9, 1.10 and will be included in future builds.

### Credit

Mathias Morbitzer (Fraunhofer AISEC), Johann Vierthaler (Fraunhofer AISEC) in cooperation with Marcel Winandy (Huawei)

## [Important] [CVE-2017-1000080] Unauthenticated websocket usage

### Description

It was found that ONOS allows the use of websockets without authentication. This allows unauthenticated users to execute the functionalities provided by websocket endpoints. 

### Affected versions

ONOS 1.8.0, 1.9.0 are confirmed to be affected.

### Patch commit(s)

<https://gerrit.onosproject.org/#/c/14261/>

### Patched versions

Patches have been committed to 1.8, 1.9, 1.10 and will be included in future builds.

### Credit

Mathias Morbitzer (Fraunhofer AISEC), Johann Vierthaler (Fraunhofer AISEC) in cooperation with Marcel Winandy (Huawei)

## [Important] [CVE-2017-1000079] DoS by using very long strings

### Description

It was found that ONOS seems to encounter severe problems with its storage facilities once a valid json with very long strings is uploaded.  After posting such a request, ONOS is unable to perform a variety of different tasks (e.g., registering a new device, performing the wipe-out command, etc.).

### Affected versions

ONOS 1.8.0, 1.9.0 are confirmed to be affected.

### Patch commit(s)

<https://gerrit.onosproject.org/#/c/14351/>

<https://gerrit.onosproject.org/#/c/14466/>

### Patched versions

Patches have been committed to 1.8, 1.9, 1.10 and will be included in future builds.

### Credit

Mathias Morbitzer (Fraunhofer AISEC), Johann Vierthaler (Fraunhofer AISEC) in cooperation with Marcel Winandy (Huawei)

## [Important] [CVE-2017-1000078] XSS vulnerability in adding devices/hosts via REST interface

### Description

It is possible to add new devices or hosts via the REST interface. It was found that if javascript code is used in the parameters, such as serial, swVersion, hwVersion or manufacturer, it is later executed when a user visits, e.g., the topology in the GUI and clicks on the device-icon.

### Affected versions

ONOS 1.8.0, 1.9.0 are confirmed to be affected.

### Patch commit(s)

<https://gerrit.onosproject.org/#/c/14170/>

<https://gerrit.onosproject.org/#/c/14182/>

### Patched versions

Patches have been committed to 1.8, 1.9, 1.10 and will be included in future builds.

### Credit

Mathias Morbitzer (Fraunhofer AISEC), Johann Vierthaler (Fraunhofer AISEC) in cooperation with Marcel Winandy (Huawei)

## [Important] [CVE-2015-7516] Denial-of-Service (DoS) due to exceptions in application packet processors

### Description

It was found that the ONOS core did not properly protect itself from exceptions thrown in application packet processors. Exceptions thrown by applications were not caught and handled, which would result in the relevant switch being disconnected because an exception occurred in an I/O thread. An application could exhibit behavior (either intentionally or unintentionally) which would allow a remote unauthenticated attacker to perform a denial-of-service (DoS) attack by causing ONOS to disconnect switches.

### Affected versions

ONOS 1.3.0 Drake is confirmed to be affected.

### Patch commit(s)

<https://gerrit.onosproject.org/#/c/6137/>

### Patched versions

A patch has been committed and will be included in a future build.

### Credit

This issue was reported by Kashyap Thimmaraju (Technische Universität Berlin & T-Labs Berlin), Liron Schiff (Tel Aviv University), and Dr. Stefan Schmid (Technische Universität Berlin & T-Labs Berlin).

## [Important] [CVE-2015-1166] onos-of-ctl: denial-of-service (DoS) due to exception handling while deserializing malformed packets

### Description

It was found that the packet deserializers in ONOS would throw exceptions when handling malformed, truncated or maliciously-crafted packets. The exceptions were not caught and handled, which would result in the relevant switch being disconnected because an exception occurred in an I/O thread. A remote unauthenticated attacker could use this flaw to perform a denial-of-service (DoS) attack by causing ONOS to disconnect switches. See [ONOS-605](https://jira.onosproject.org/browse/ONOS-605) for more details.

### Affected versions

ONOS 1.0.0 Avocet is confirmed to be affected.

### Patch commit(s)

<https://gerrit.onosproject.org/#/c/2207/>

### Patched versions

Avocet 1.0.1 contains the fix and this patched build is available [here](../downloads.md). Release Notes for Avocet 1.0.1 are available [here](../../release-notes/release-notes-avocet-1.0.1.md).

### Credit

This issue was reported by Charles M.C. Chan and Jonathan Hart.
