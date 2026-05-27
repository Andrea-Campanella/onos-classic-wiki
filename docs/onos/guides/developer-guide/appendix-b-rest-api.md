# Appendix B: REST API

# Auto-generated Swagger Documentation

ONOS uses Swagger to auto-generate REST API documentation. This can be viewed from any running ONOS instance at the following URL: **http://<ONOS IP>:8181/onos/v1/docs/**.

This also offers a nice way to directly run queries or copy&paste *curl* commands for testing. Endpoints contributed by non-core applications can be reached through the top menu.

# Summary of Core APIs

The following specifications are manually-written documentation, so it will inevitably fall out-of-sync with the code. It is recommended to use the above instructions to access the automatically-generated Swagger documentation for the most up-to-date information.

Please note that the all endpoints need to be prefixed with: **http://<controller IP>:8181/onos/v1/**

Example: <http://127.0.0.1:8181/onos/v1/devices> if ONOS is running on your local machine.

The entries in **bold** are currently implemented.

## Device

|  |  |
| --- | --- |
| **GET /devices** | **Lists all infrastructure devices.** |
| **GET /devices/{deviceId}** | **Lists details of a specific infrastructure device.** |
| **GET /devices/{deviceId}/ports** | **Lists ports of a specific infrastructure device.** |
| POST /devices | Creates a new infrastructure device into inventory (future). |
| PUT /devices/{deviceId} | Updates a device - attributes, availability, mastership. |
| **DELETE /devices/{deviceId}** | **Deletes an infrastructure device from inventory.** |

## Link

|  |  |
| --- | --- |
| **GET /links** | **Lists all infrastructure links.** |
| **GET /links?{device=deviceId}{port=portNumber}{direction=[ALL,INGRESS,EGRESS]}** | **Lists details of a link.** |
| POST /links | Creates a new infrastructure link into inventory (future). |
| PUT /links/{linkId} | Updates a link - attributes, e.g. type. |
| DELETE /link/{linkId} | Deletes an infrastructure link from inventory. |

## Host

|  |  |
| --- | --- |
| **GET /hosts** | **Lists all end-stations hosts.** |
| **GET /hosts/{hostId}** | **Lists details of a specific end-station host specified by the host ID.** |
| **GET /hosts/{mac}/{vlan}** | **Lists details of a specific end-station host specified by the host MAC address and VLan Id.** |
| POST /hosts | Creates a new end-station host into inventory (future). |
| PUT /hosts/{hostId} | Updates an end-station host - attributes, e.g. IP, location. |
| DELETE /hosts/{hostId} | Deletes an end-station host from inventory. |

## Topology

|  |  |
| --- | --- |
| **GET /topology** | Gets overview of the current topology. |
| **GET /topology/clusters** | Gets list of topology cluster overviews. |
| **GET /topology/clusters/{clusterId}** | Gets overview of a specific topology cluster. |
| **GET /topology/clusters/{clusterId}/devices** | Gets infrastructure devices that belong to the specified topology cluster. |
| **GET /topology/clusters/{clusterId}/links** | Gets infrastructure links that belong to the specified topology cluster. |
| **GET /topology/broadcast/{connectPoint}** | Gets indication whether the given point permits broadcast. |
| **GET /topology/infrastructure/{connectPoint}** | Gets indication whether the given point belongs to network infrastructure. |

## Path

|  |  |
| --- | --- |
| **GET /paths/{elementId}/{elementId}** | Gets set of pre-computed shortest paths between the specified source and destination network elements. |

## Flow

|  |  |
| --- | --- |
| **POST /flows/{deviceId}** | **Creates a single flow rule applied to the specified infrastructure device.** |
| **GET /flows/{deviceId}** | **Gets list of flow rules applied to the specified infrastructure device.** |
| **GET /flows/{deviceId}/{flowId}** | **Gets details of a specified flow rule.** |
| **GET /flows** | **Gets details of all flow rules in the system.** |
| **POST /flows/** | **Adds a batch of flow rules.** |
| **DELETE /flows/{deviceId}/{flowId}** | **Deletes a flow rule from the specified device.** |
| GET /statistics/flows/link/{linkId} | Gets aggregate statistics for all flows traversing the given link. |

## Flow Objectives

|  |  |
| --- | --- |
| **POST /flowobjectives/{deviceId}/filter** | **Creates and installs a new filtering objective for the specified device.** |
| **POST /flowobjectives/{deviceId}/forward** | **Creates and installs a new forwarding objective for the specified device.** |
| **POST /flowobjectives/{deviceId}/next** | **Creates and installs a new next objective for the specified device.** |
| **GET /flowobjectives/next** | **Gets the globally unique nextId.** |
| **POST /flowobjectives/policy** | **Installs the filtering rules onto the specified device.** |

## Group

|  |  |
| --- | --- |
| **POST /groups/{deviceId}** | **Creates a single group entry applied to the specified infrastructure device.** |
| **GET /groups/{deviceId}** | **Gets list of group entries applied to the specified infrastructure device.** |
| **GET /groups/{deviceId}/{groupKey}** | **Gets details of a specified group entry.** |
| **GET /groups** | **Gets details of all group entries in the system.** |
| **DELETE /groups/{deviceId}/{groupKey}** | **Deletes a group entry from the specified device.** |

## Meter

|  |  |
| --- | --- |
| **POST /meters/{deviceId}** | **Creates a single meter entry applied to the specified infrastructure device.** |
| **GET /meters/{deviceId}** | **Gets list of meter entries applied to the specified infrastructure device.** |
| **GET /meters/{deviceId}/{meterId}** | **Gets details of a specified meter entry.** |
| **GET /meters** | **Gets details of all meter entries in the system.** |
| **DELETE /meters/{deviceId}/{meterId}** | **Deletes a meter entry from the specified device.** |

## Intent

|  |  |
| --- | --- |
| **GET /intents/{app-id}/{intent-id}** | **Gets the details for the given Intent object.** |
| **GET /intents** | **Gets a collection containing all the Intent objects currently in the system.** |
| **POST /intents** | **Creates a new Intent object.** |
| POST /intents | Creates a batch of Intent objects (pending -may not be included in finalized API). |
| **DELETE /intents/{app-id}/{intent-id}** | **Removes an intent from the system.** |

## Application

|  |  |
| --- | --- |
| **GET /applications** | **Gets a list of all installed applications.** |
| **GET /applications/{app-name}** | **Gets information about the named application.** |
| **POST /applications/** | **Installs application using the posted *app.xml* or application package file (ZIP).** |
| **DELETE /applications/{app-name}** | **Uninstalls the named application.** |
| **POST /applications/{app-name}/active** | **Activates the named application.** |
| **DELETE /applications/{app-name}/active** | **Deactivates the named application.** |
| **GET /applications/ids/entry** | **Gets applicationId entry by either id or name** |
| **GET /applications/ids/** | **Gets a list of all registered applicationIds** |

## Component Configuration

Each OSGI component within ONOS can have its own set of configuration values.  The REST APIs present these as a map when generating JSON:

```
{
```

```
    "org.onosproject.provider.host.impl.HostLocationProvider":
```

```
    {
```

```
        "ipv6NeighborDiscovery":"false",
```

```
        "hostRemovalEnabled":"true"
```

```
    }
```

```
}
```

|  |  |
| --- | --- |
| **GET /configuration** | **Gets a list of all active components and their configuration values** |
| **GET /configuration/{component}** | **Gets the configuration values for a single component** |
| **POST /configuration/{component}** | **Adds a set of configuration values to a component** |
| **DELETE /configuration/{component}** | **Removes the configuration values for a component and sets them back to their default values** |

---

[Previous : Appendix A : List of ONOS Test Scripts (onos-\* scripts)](appendix-a-list-of-onos-utility-scripts-onos-scripts.md)  
[Next : Appendix C : Source Tree Organization](appendix-c-source-tree-organization.md)

---
