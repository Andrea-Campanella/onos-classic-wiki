# Flow Rules

# Flow Rule Criteria

## JSON Format

During a flow POST request to the ONOS REST APIs the passed JSON data can contain different objects in the criteria array . This is an example of a JSON document with all the possible criterion. Any combination of zero or more of these criterion will work in a POST request.

```
{
  "priority": 40000,
  "timeout": 0,
  "isPermanent": true,
  "deviceId": "of:0000000000000001",
  "treatment": {
    "instructions": [
      {
        "type": "OUTPUT",
        "port": "CONTROLLER"
      }
    ]
  },
  "selector": {
    "criteria": [
      {
        "type": "ETH_TYPE",
        "ethType": "0x88cc"
      },
	  {
        "type": "ETH_DST",
        "mac": "00:00:11:00:00:01"
      },
      {
        "type": "ETH_SRC",
        "mac": "00:00:11:00:00:01"
      },
      {
        "type": "IN_PORT",
        "port": "1"
      },
      {
        "type": "IN_PHY_PORT",
        "port": "1"
      },
      {
        "type": "METADATA",
        "metadata": "0x1000"
      },
      {
        "type": "VLAN_VID",
        "vlanId": "1"
      },
      {
        "type": "VLAN_PCP",
        "priority": "1"
      },
      {
        "type": "INNER_VLAN_VID",
        "innerVlanId": "1"
      },
      {
        "type": "INNER_VLAN_PCP",
        "innerPriority": "1"
      },
      {
        "type": "IP_DSCP",
        "ipDscp": 1
      },
      {
        "type": "IP_ECN",
        "ipEcn": 1
      },
      {
        "type": "IP_PROTO",
        "protocol": 1
      },
      {
        "type": "IPV4_SRC",
        "ip": "10.1.1.0/24"
      },
      {
        "type": "IPV4_DST",
        "ip": "10.1.1.0/24"
      },
      {
        "type": "TCP_SRC",
        "tcpPort": 1
      },
      {
        "type": "TCP_DST",
        "tcpPort": 1
      },
      {
        "type": "UDP_SRC",
        "udpPort": 1
      },
      {
        "type": "UDP_DST",
        "udpPort": 1
      },
      {
        "type": "SCTP_SRC",
        "sctpPort": 1
      },
      {
        "type": "SCTP_DST",
        "sctpPort": 1
      },
      {
        "type": "ICMPV4_TYPE",
        "icmpType": "1"
      },
      {
        "type": "ICMPV4_CODE",
        "icmpCode": 1
      },
      {
        "type": "IPV6_SRC",
        "ip": "1111::2222/64"
      },
      {
        "type": "IPV6_DST",
        "ip": "1111::2222/64"
      },
      {
        "type": "IPV6_FLABEL",
        "flowlabel": 1
      },
      {
        "type": "ICMPV6_TYPE",
        "icmpv6Type": 1
      },
      {
        "type": "ICMPV6_CODE",
        "icmpv6Code": 1
      },
      {
        "type": "IPV6_ND_TARGET",
        "targetAddress": "1111::2222"
      },
      {
        "type": "IPV6_ND_SLL",
        "mac": "00:00:11:00:00:01"
      },
      {
        "type": "IPV6_ND_TLL",
        "mac": "00:00:11:00:00:01"
      },
      {
        "type": "MPLS_LABEL",
        "label": 1
      },
      {
        "type": "IPV6_EXTHDR",
        "exthdrFlags": 1
      },
      {
        "type": "OCH_SIGID",
        "lambda": 1
      },
      {
        "type": "GRID_TYPE",
        "gridType": DWDM
      },
      {
        "type": "CHANNEL_SPACING",
        "channelSpacing": 100
      },
      {
        "type": "SPACING_MULIPLIER",
        "spacingMultiplier": 4
      },
      {
        "type": "SLOT_GRANULARITY",
        "slotGranularity": 8
      },
      {
        "type": "OCH_SIGID",
        "ochSignalId": 1
      },
      {
        "type": "TUNNEL_ID",
        "tunnelId": 5
      },
      {
        "type": "OCH_SIGTYPE",
        "ochSignalType": 1
      },
      {
        "type": "ODU_SIGID",
        "oduSignalId": 1
        "tributaryPortNumber": 11
        "tributarySlotBitmap": bitmap
        "type": "ETH_TYPE",
        "tributarySlotLen": 1
      },
      {
        "type": "ODU_SIGTYPE",
        "oduSignalType": 4
      },
    ]
  }
}
```

## Key and field description

The following table describes the type and the value format of the fields.

{"name":"criteria\_description.xlsx","type":"xlsx","pageID":"8421445"}

**Loading**

# Flow rule instructions

## JSON Format

During a flow POST request to the ONOS REST APIs the passed JSON data can contain different objects in the instructions array . This is an example of a JSON document with all the possible instructions with type and subtype combinations. A combination of one or more of these instructions will work in a POST request.

```
"treatment": {
 "instructions": [
  {
    "type": "OUTPUT",
    "port": "CONTROLLER"
  },
  {
    "type": "TABLE",
    "tableId": 1
  },
  {
    "type": "GROUP",
    "groupId": 1
  },
  {
    "type": "METER",
    "meterId": 1
  },
  {
    "type": "QUEUE",
    "queueId": 1,
    "port": 2
  },
  {
  	"type": "L0MODIFICATION",
  	"subtype": "LAMBDA",
  	"lambda": 1
  },
  {
  	"type":"L0MODIFICATION",
  	"subtype":"OCH",
  	"gridType": "DWDM",
  	"channelSpacing": 1,
  	"spacingMultiplier": 1,
  	"slotGranularity": 1
  },
  {
  	"type":"L1MODIFICATION",
  	"subtype":"ODU_SIGID",
  	"oduSignalId":{
  		"tributaryPortNumber": 1,
  		"tributarySlotLength": 1,
  		"tributarySlotBitmap": <bitmap>
  	}
  },
  {
  	"type":"L2MODIFICATION",
  	"subtype":"VLAN_PUSH"
  },
  {	
  	"type":"L2MODIFICATION",
  	"subtype":"VLAN_ID",
  	"vlanId":200
  },
  {
  	"type":"L2MODIFICATION",
  	"subtype":"VLAN_PCP",
  	"vlanPcp":0
  },
  {
  	"type":"L2MODIFICATION",
  	"subtype":"ETH_SRC",
  	"mac":"00:00:00:00:01"
  }
  {
  	"type":"L2MODIFICATION",
  	"subtype":"ETH_DST",
  	"mac":"00:00:00:00:01"
  },
  {
  	"type":"L2MODIFICATION",
  	"subtype":"MPLS_LABEL",
  	"label":1
  },
  {
  	"type":"L2MODIFICATION",
  	"subtype":"MPLS_PUSH",
  	"ethernetType":1
  },
  {
  	"type":"L2MODIFICATION",
  	"subtype":"TUNNEL_ID",
  	"tunnelId":1
  },
  {
  	"type":"L3MODIFICATION",
  	"subtype":"IPV4_SRC",
  	"ip":"1.1.1.1"
  },
  {
  	"type":"L3MODIFICATION",
  	"subtype":"IPV4_DST",
  	"ip":"1.1.1.1"
  },
  {
  	"type":"L3MODIFICATION",
  	"subtype":"IPV6_SRC",
  	"ip":"1111::2222"
  },
  {
  	"type":"L3MODIFICATION",
  	"subtype":"IPV6_DST",
  	"ip":"1111::2222"
  },
  {
  	"type":"L3MODIFICATION",
  	"subtype":"IPV6_FLABEL",
  	"flowLabel":1
  },
  {
  	"type":"L4MODIFICATION",
  	"subtype":"TCP_SRC",
  	"tcpPort":1
  },
  {
  	"type":"L4MODIFICATION",
  	"subtype":"UDP_SRC",
  	"udpPort":1
  }
 ]
}
```
