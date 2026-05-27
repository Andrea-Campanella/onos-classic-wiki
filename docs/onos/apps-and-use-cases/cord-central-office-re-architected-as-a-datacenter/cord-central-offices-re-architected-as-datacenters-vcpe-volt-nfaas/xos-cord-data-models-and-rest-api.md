# XOS CORD Data Models and REST API

# CORD-Specific Tenancy Objects

XOS include three tenancy objects in support of CORD. These objects are VOLTTenant, VCPETenant, and VBNGTenant, which correspond to vOLT, vCPE, and vBNG respectively. These data objects are arranged in a hierarchical fashion. The vOLT object subscribers to the vCPE service which in turn subscribes to the vBNG service. Each one of these objects holds a service\_specific\_id attribute which may be used by ONOS to place a handle back to the ONOS-specific object.

The entrypoint for ONOS is intented to be the VOLTTenant object. ONOS will call XOS with the (service\_specific\_id, vlan\_id) that corresponds to a new vOLT subscriber. XOS will then create the VOLTTenant and the remaining objects in the hierarchy. A sliver will be created that will boot the VM that runs the vCPE virtual machine image.

# Prerequisites / Necessary Configuration

The following must be configured in XOS for the CORD objects to work correctly.

* A service of type "vOLT"
* A service of type "vCPE"
  + One slice must be connected to this service. XOS will instantiated vCPE slivers on this slice.
* A service of type "vBNG"
* One or more nodes
  + In the case where there is more than one node, XOS will try to pick the node with the fewest slivers each time a vCPE sliver needs to be instantiated.
* An image named "Ubuntu-14.04-LTS" or "Ubuntu 14.04 LTS"  (eventually we'll use a vCPE-specific image)

# REST API

The REST API may be used to create, read, update, and delete objects.

### Create a new VOLTTenant Object

The following example uses Curl to invoke the REST API from the Linux command line:

```
HOST=10.254.1.22:8000
AUTH=padmin@vicci.org:letmein
SERVICE_SPECIFIC_ID=5678
VLAN_ID=1234

curl -H "Accept: application/json; indent=4" -H "Content-Type: application/json" -u $AUTH -X POST -d "{\"service_specific_id\": \"$SERVICE_SPECIFIC_ID\", \"vlan_id\": \"$VLAN_ID\"}" $HOST/xoslib/volttenant/
```

Note that XOS enforces a uniqueness constraint on the service\_specific\_id argument, and it is an error to attempt to create two VOLTTenant objects with the same service\_specific\_id.

### List all VOLTTenant Objects

```
HOST=10.254.1.22:8000
AUTH=padmin@vicci.org:letmein

curl -H "Accept: application/json; indent=4" -H "Content-Type: application/json" -u $AUTH $HOST/xoslib/volttenant/
```

### Delete a VOLTTenant Object

```
HOST=10.254.1.22:8000
AUTH=padmin@vicci.org:letmein
ID=974

curl -H "Accept: application/json; indent=4" -H "Content-Type: application/json" -u $AUTH -X DELETE $HOST/xoslib/volttenant/$ID/
```

Note that the ID used is the XOS ID of the VOLTTenant object, not the service\_specific\_id or the vlan\_id. If you've forgotten the XOS ID that goes with a particular service\_specific\_id, then you can query for it.

### Query for a specific service\_specific\_id

```
HOST=10.254.1.22:8000
AUTH=padmin@vicci.org:letmein
SERVICE_SPECIFIC_ID=1234

curl -H "Accept: application/json; indent=4" -H "Content-Type: application/json" -u $AUTH $HOST/xoslib/volttenant/?service_specific_id=$SERVICE_SPECIFIC_ID
```

---

# CORD-VTN Specific API Reference (work in progress)

## Ports

**GET api/service/vtn/ports**    list ports including port details

**GET api/service/vtn/ports/{port\_id}** show port details

**Port Details**

| Parameter | Type | Description |
| --- | --- | --- |
| id | UUID | UUID of the port |
| name (optional) | string | port name |
| network\_id | UUID | ID of the attached network |
| mac\_address | string | MAC address |
| ip\_address | string | IP address |

**Example JSON response: api/service/vtn/ports**

```
{
    "ports": [
        {
            "id": "55d1b71f-efe2-455d-a78c-e48e9d3a4094",
            "name": "",
            "network_id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
            "mac_address": "fa:16:3e:ca:05:9b",
            "ip_address": "10.0.3.2"
        },
        {
            "id": "7098f0a8-cdcb-4bce-9706-05aecacb784b",
            "name": "stag-222",
            "network_id": "8ab38619-327e-47ce-9304-2c595c1b6708",
            "mac_address": "fa:16:3e:ca:05:9b",
            "ip_address": "10.0.2.2"
        }
    ]
}
```

**Example json response: api/service/vtn/ports/55d1b71f-efe2-455d-a78c-e48e9d3a4094**

```
{
    "port": {
        "id": "55d1b71f-efe2-455d-a78c-e48e9d3a4094",
        "name": "",
        "network_id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
        "mac_address": "fa:16:3e:ca:05:9b",
        "ip_address": "10.0.3.2"
    } 
}
```

## Networks

**GET api/service/vtn/networks**   list networks including network details

**GET api/service/vtn/networks/{network\_id}**  show network details

**Network Details**

| Parameters | Type | Description |
| --- | --- | --- |
| id | UUID | UUID of the network |
| name | string | name name |
| type | string | type of the network [PRIVATE|PUBLIC|MANAGEMENT] |
| service\_id | UUID | UUID of the associated service *(always equals to network ID?)* |
| segmentation\_id | string | identifier of isolated network segment. VNI in VXLAN, for example. |
| subnet | string | subnet CIDR of the network |
| gateway | string | gateway IP address of the subnet |

**Example json response: api/service/vtn/networks** 

```
{
    "networks": [
        {
            "id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
            "name": "one_access",
            "type": "private",
            "service_id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
            "segementation_id": "1017",
            "subnet": "10.0.3.0/24",
            "gateway": "10.0.3.1"
        },
        {
            "id": "8ab38619-327e-47ce-9304-2c595c1b6708",
            "name": "mysite_vsg-access",
            "type": "private",
            "service_id": "8ab38619-327e-47ce-9304-2c595c1b6708",
            "vni": "1017",
            "subnet": "10.0.2.0/24",
            "gateway": "10.0.2.1"
        }
    ]
}
```

**Example json response: api/service/vtn/networks/a14d7a6b-dffb-4271-8a17-5d715b362d1e**

```
{
    "network": {
        "id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
        "name": “one_access",
        "type": "private",
        "service_id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
        "vni": "1017",
        "subnet": "10.0.3.0/24",
        "gateway": "10.0.3.1"
    }
}
```

## Services

**GET api/service/vtn/services**   list services including service details

**GET api/service/vtn/services/{service\_id}**  show service details

**Service Details**

| Parameters | Type | Description |
| --- | --- | --- |
| id | UUID | UUID of the service |
| name | string | service name |
| type | string | service type [VSG|OLT\_AGENT|DEFAULT] |
| network\_id | UUID | ID of the associated network |
| providers | list | list of provider service IDs of the service |
| tenants | list | list of tenant service IDs of the service |
| bidirectional | boolean | the dependency, which is bidirectional(true) or unidirectional(false) |

**Example json response: api/service/vtn/services**

```
{
    “services": [
        {
            "id": "8ab38619-327e-47ce-9304-2c595c1b6708",
            "name": "vsg",
            "type": "vsg",
            "network_id": "8ab38619-327e-47ce-9304-2c595c1b6708"
        },
        {
            "id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
            "name": "access_one",
            "type": "default",
            "network_id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
            "providers": [],
            "tenants": [
                {
                    "id": "71cc8c93-f809-42ff-b1d6-0c8d92c6cd2b",
                    "bidirectional": true
                }
            ]
        }
    ]
}
```

**example json response: api/service/vtn/services/a14d7a6b-dffb-4271-8a17-5d715b362d1e**

```
{
    "service": {
        "id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
        "name": "access_one",
        "type": "default",
        "network_id": "a14d7a6b-dffb-4271-8a17-5d715b362d1e",
        "providers": [],
        "tenants": [
            {
                "id": "71cc8c93-f809-42ff-b1d6-0c8d92c6cd2b",
                "bidirectional": true
            }
        ]
    }
}
```
