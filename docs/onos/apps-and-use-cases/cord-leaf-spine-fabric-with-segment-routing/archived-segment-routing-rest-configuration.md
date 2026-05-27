# [Archived] Segment Routing REST Configuration

Deprecated

This page is deprecated and may be removed in a near future.  
The new entry point of Trellis underlay fabric installation guide can be found at [Fabric Installation Guide](https://wiki.opencord.org/display/CORD/Fabric+Installation+Guide).

The Segment-Routing application can be configured from several places.  
  
The latest configuration file can be found [in here](https://github.com/opennetworkinglab/cord-config/blob/master/cord-fabric.json).

## How to add a VSG.

One can add a new VSG to the fabric in three steps.

* Adding the VSG host information
* Adding routing information on how to reach the VSG
* Restarting ONOS.

This can be done using the REST interface.

### Adding host information.

First check the model of the JSON file by doing the following:

```
curl -X GET --header "Accept: application/json" "http://10.242.11.187:8181/onos/v1/network/configuration/hosts"
```

You should see something like this:

```
{
  "02:42:1D:1D:00:05/-1": {
    "basic": {
      "ips": [
        "29.29.0.5"
      ],
      "location": "of:0000000000000102/5"
    }
  },
  "E4:1D:2D:2D:B3:E0/-1": {
    "basic": {
      "ips": [
        "10.0.2.1"
      ],
      "location": "of:0000000000000103/5"
    }
  },
  "02:42:1D:1D:00:07/-1": {
    "basic": {
      "ips": [
        "29.29.0.7"
      ],
      "location": "of:0000000000000102/5"
    }
  }
}
```

To add a new host you should add a new entry using the VSG MAC as key.

This one add a VSG with IP 29.29.0.32 with MAC 02:42:1D:1D:00:20.

```
curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d "{
    \"basic\": {
      \"ips\": [
        \"29.29.0.32\"
      ],
      \"location\": \"of:0000000000000102/5\"
    }
  }" "http://10.242.11.187:8181/onos/v1/network/configuration/hosts/02%3A42%3A1D%3A1D%3A00%3A20%2F-1"
```

Next, you should add a new route to the segment routing app.

### Adding routing information for the vSG

First, you have to get the current config using:

```
curl -X GET --header "Accept: application/json" "http://10.242.11.187:8181/onos/v1/network/configuration/ports/of%3A0000000000000102%2F5"
```

You should get something like this:

```
{
  "interfaces": [
    {
      "ips": [
        "10.0.1.254/24"
      ]
    },
    {
      "ips": [
        "29.29.0.3/32"
      ]
    },
    {
      "ips": [
        "29.29.0.4/32"
      ]
    },
    {
      "ips": [
        "29.29.0.2/32"
      ]
    },
    {
      "ips": [
        "29.29.0.5/32"
      ]
    },
    {
      "ips": [
        "29.29.0.8/32"
      ]
    },
    {
      "ips": [
        "29.29.0.7/32"
      ]
    },
    {
      "vlan": "10"
    },
    {
      "vlan": "15"
    },
    {
      "vlan": "5"
    }
  ]
}
```

After you should add the value that you need to the array inside interfaces. For example:

```
curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d "{
  \"interfaces\": [
    {
      \"ips\": [
        \"29.29.0.32/32\"
      ]
    },
    {
      \"ips\": [
        \"10.0.1.254/24\"
      ]
    },
    {
      \"ips\": [
        \"29.29.0.3/32\"
      ]
    },
    {
      \"ips\": [
        \"29.29.0.4/32\"
      ]
    },
    {
      \"ips\": [
        \"29.29.0.2/32\"
      ]
    },
    {
      \"ips\": [
        \"29.29.0.5/32\"
      ]
    },
    {
      \"ips\": [
        \"29.29.0.8/32\"
      ]
    },
    {
      \"ips\": [
        \"29.29.0.7/32\"
      ]
    },
    {
      \"vlan\": \"10\"
    },
    {
      \"vlan\": \"15\"
    },
    {
      \"vlan\": \"5\"
    }
  ]
}" "http://10.242.11.187:8181/onos/v1/network/configuration/ports/of%3A0000000000000102%2F5"
```

Lastly, you need to restart onos and reconnect the switches to make sure the SR app is properly configuring them.
