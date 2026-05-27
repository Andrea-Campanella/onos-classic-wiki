# API: Performance Test Related API

Last Modified by: ![](../../../../assets/unknown-macro-3.png) Last Modified Date: ![](../../../../assets/unknown-macro-3.png)

## **Intent-related Metrics**

## 1. Install the metrics app by using either

    a. Include *"metrics"* in the *ONOS\_APP*configuration list for your ONOS cell **BEFORE**installing and starting the ONOS cluster:

```
export ONOS_APPS=drivers,openflow,metrics
```

    b. Activate the "metrics" app from the ONOS CLI while ONOS is running:

```
onos> app activate metrics
```

2. Perform the intent-related operation that should be measured. For example, install a single intent from the CLI to measure the intent installation latency:

```
onos> add-point-intent --ethSrc 11:11:11:11:11:11 --ethDst 11:11:11:22:22:22 of:0000000000000001/1 of:0000000000000002/1
```

3. Use the ONOS CLI to obtain the intent event metrics in human-readable format:

```
onos> intents-events-metrics
Intent Submitted Event Timestamp (ms from epoch)=1414607529207
Intent Submitted Events count=1 rate(events/sec) mean=0.000598 m1=0.000000 m5=0.000016 m15=0.000186
Intent Installed Event Timestamp (ms from epoch)=0
Intent Installed Events count=0 rate(events/sec) mean=0.000000 m1=0.000000 m5=0.000000 m15=0.000000
Intent Withdraw Requested Event Timestamp (ms from epoch)=0
Intent Withdraw Requested Events count=0 rate(events/sec) mean=0.000000 m1=0.000000 m5=0.000000 m15=0.000000
Intent Withdrawn Event Timestamp (ms from epoch)=0
Intent Withdrawn Events count=0 rate(events/sec) mean=0.000000 m1=0.000000 m5=0.000000 m15=0.000000
onos>
```

4. Use the ONOS CLI to obtain the intent event metrics in JSON format (NOTE: the output is formatted for readability):

```
onos> intents-events-metrics --json
```

**Intent event metrics (JSON)**

```
{
"intentInstalledRate": {
"count": 0,
"m15_rate": 0.0,
"m1_rate": 0.0,
"m5_rate": 0.0,
"mean_rate": 0.0,
"units": "events/second"
},
"intentInstalledTimestamp": {
"value": 0
},
"intentSubmittedRate": {
"count": 1,
"m15_rate": 0.00018520260981402803,
"m1_rate": 3.5506691362264177e-14,
"m5_rate": 1.543657444105269e-05,
"mean_rate": 0.0005956066011497849,
"units": "events/second"
},
"intentSubmittedTimestamp": {
"value": 1414607529207
},
"intentWithdrawRequestedRate": {
"count": 0,
"m15_rate": 0.0,
"m1_rate": 0.0,
"m5_rate": 0.0,
"mean_rate": 0.0,
"units": "events/second"
},
"intentWithdrawRequestedTimestamp": {
"value": 0
},
"intentWithdrawnRate": {
"count": 0,
"m15_rate": 0.0,
"m1_rate": 0.0,
"m5_rate": 0.0,
"mean_rate": 0.0,
"units": "events/second"
},
"intentWithdrawnTimestamp": {
"value": 0
}
}
```

Output description:

    a. For every intent-related event type we collect the event rate and the last event timestamp. In the above example, the intent events are:

1. SUBMITTED: intent was submitted for installation
2. INSTALLED: intent installation was completed
3. WITHDRAW\_REQUESTED: intent withdraw request was submitted - not supported yet
4. WITNDRAWN: intent withdraw was completed

    b. The event rate is measured in number of events per second:

1. "count": total number of events received so far
2. "mean\_rate": the mean rate of the events
3. "m1\_rate": the event rate for the last one minute
4. "m5\_rate": the event rate for the last five minutes
5. "m15\_rate": the event rate for the last fifteen minutes

    c. The last event timestamp is measured in system milliseconds since the epoch: 00:00:00 [Coordinated Universal Time](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) (UTC), Thursday, 1 January 1970. See <http://en.wikipedia.org/wiki/Unix_time+> for details.

5. Additional debug information. You can use the following ONOS CLI command to list the last 100 intent-related events:

```
onos> onos:intents-events
Event=IntentEvent{time=2014-10-29T11:32:09.205, type=SUBMITTED, subject=PointToPointIntent{id=0x1d285cdd, appId=DefaultApplicationId{id=3, name=org.onlab.onos.cli}, selector=DefaultTrafficSelector{criteria=[ETH_SRC{mac=11:11:11:11:11:11}, ETH_TYPE{ethType=800}, ETH_DST{mac=11:11:11:22:22:22}]}, treatment=DefaultTrafficTreatment{instructions=[]}, ingress=ConnectPoint{elementId=of:0000000000000001, portNumber=3}, egress=ConnectPoint{elementId=of:0000000000000002, portNumber=3}}}
Event=IntentEvent{time=2014-10-29T11:32:09.257, type=FAILED, subject=PointToPointIntent{id=0x1d285cdd, appId=DefaultApplicationId{id=3, name=org.onlab.onos.cli}, selector=DefaultTrafficSelector{criteria=[ETH_SRC{mac=11:11:11:11:11:11}, ETH_TYPE{ethType=800}, ETH_DST{mac=11:11:11:22:22:22}]}, treatment=DefaultTrafficTreatment{instructions=[]}, ingress=ConnectPoint{elementId=of:0000000000000001, portNumber=3}, egress=ConnectPoint{elementId=of:0000000000000002, portNumber=3}}}
onos>
```

## **Topology-related Metrics**

1. Install the metrics app by using either

    a. Include *"metrics"* in the *ONOS\_APP*configuration list for your ONOS cell **BEFORE**installing and starting the ONOS cluster:

```
export ONOS_APPS=drivers,openflow,metrics
```

    b. Activate the "metrics" app from the ONOS CLI while ONOS is running:

**ONOS metrics feature**

```
onos> app activate metrics
```

2. Perform the topology-related operation that should be measured. For example, disable a switch port with a link connecting that switch to another one.

3. Use the ONOS CLI to obtain the topology event metrics in human-readable format:

```
onos> topology-events-metrics
Topology Device Event Timestamp (ms from epoch)=1414611704399
Topology Device Events count=9 rate(events/sec) mean=0.028414 m1=0.003795 m5=0.012518 m15=0.007424
Topology Host Event Timestamp (ms from epoch)=0
Topology Host Events count=0 rate(events/sec) mean=0.000000 m1=0.000000 m5=0.000000 m15=0.000000
Topology Link Event Timestamp (ms from epoch)=1414611704399
Topology Link Events count=4 rate(events/sec) mean=0.012628 m1=0.003300 m5=0.006538 m15=0.003476
Topology Graph Event Timestamp (ms from epoch)=1414611704452
Topology Graph Events count=5 rate(events/sec) mean=0.015785 m1=0.001947 m5=0.006857 m15=0.004107
onos>
```

4. Use the ONOS CLI to obtain the topology event metrics in JSON format (NOTE: the output is formatted for readability):

```
onos> onos:topology-events-metrics --json
```

**ONOS topology events metrics (JSON)**

```
{
"topologyDeviceEventRate": {
"count": 9,
"m15_rate": 0.006145833414538993,
"m1_rate": 0.00022322652468927413,
"m5_rate": 0.007102863189830044,
"mean_rate": 0.018424109971361024,
"units": "events/second"
},
"topologyDeviceEventTimestamp": {
"value": 1414611704399
},
"topologyGraphEventRate": {
"count": 5,
"m15_rate": 0.0033997382707502822,
"m1_rate": 0.00011452856842741324,
"m5_rate": 0.003890745553440407,
"mean_rate": 0.01023557364606096,
"units": "events/second"
},
"topologyGraphEventTimestamp": {
"value": 1414611704452
},
"topologyHostEventRate": {
"count": 0,
"m15_rate": 0.0,
"m1_rate": 0.0,
"m5_rate": 0.0,
"mean_rate": 0.0,
"units": "events/second"
},
"topologyHostEventTimestamp": {
"value": 0
},
"topologyLinkEventRate": {
"count": 4,
"m15_rate": 0.0028776177797310907,
"m1_rate": 0.00019407346386151271,
"m5_rate": 0.0037097236045761767,
"mean_rate": 0.008188471872335748,
"units": "events/second"
},
"topologyLinkEventTimestamp": {
"value": 1414611704399
}
}
```

Output description:

    a. For every topology-related event type we collect the event rate and the last event timestamp. In the above example, the topology events are:

1. Device Event: A device (e.g., a switch, including its ports) was added, updated or removed
2. Host Event: A host was added, updated or removed
3. Link Event: A link was added, updated or removed
4. Topology Graph Event: The topology graph was updated because of some graph-related events (device or link event)

    b. The event rate is measured in number of events per second:

1. "count": total number of events received so far
2. "mean\_rate": the mean rate of the events
3. "m1\_rate": the event rate for the last one minute
4. "m5\_rate": the event rate for the last five minutes
5. "m15\_rate": the event rate for the last fifteen minutes

    c. The last event timestamp is measured in system milliseconds since the epoch: 00:00:00 [Coordinated Universal Time](http://en.wikipedia.org/wiki/Coordinated_Universal_Time) (UTC), Thursday, 1 January 1970. See <http://en.wikipedia.org/wiki/Unix_time+> for details.

5. Additional debug information. You can use the following ONOS CLI command to list the last 100 topology-related events:

**ONOS CLI topology events**

```
onos> topology-events
Event=DeviceEvent{time=2014-10-29T12:41:44.335, type=PORT_UPDATED, subject=DefaultDevice{id=of:0000000000000001, type=SWITCH, manufacturer=Nicira, Inc., hwVersion=Open vSwitch, swVersion=2.0.2, serialNumber=None}, port=DefaultPort{element=of:0000000000000001, number=3, isEnabled=false}}
Event=DeviceEvent{time=2014-10-29T12:41:44.346, type=PORT_UPDATED, subject=DefaultDevice{id=of:0000000000000002, type=SWITCH, manufacturer=Nicira, Inc., hwVersion=Open vSwitch, swVersion=2.0.2, serialNumber=None}, port=DefaultPort{element=of:0000000000000002, number=3, isEnabled=false}}
Event=LinkEvent{time=2014-10-29T12:41:44.360, type=LINK_REMOVED, subject=DefaultLink{src=ConnectPoint{elementId=of:0000000000000001, portNumber=3}, dst=ConnectPoint{elementId=of:0000000000000002, portNumber=3}, type=DIRECT}}
Event=LinkEvent{time=2014-10-29T12:41:44.389, type=LINK_REMOVED, subject=DefaultLink{src=ConnectPoint{elementId=of:0000000000000002, portNumber=3}, dst=ConnectPoint{elementId=of:0000000000000001, portNumber=3}, type=DIRECT}}
Event=TopologyEvent{time=2014-10-29T12:41:44.450, type=TOPOLOGY_CHANGED, subject=DefaultTopology{time=10468535518752, clusters=2, devices=2, links=0, pathCount=0}}
Reason=LinkEvent{time=2014-10-29T12:41:44.360, type=LINK_REMOVED, subject=DefaultLink{src=ConnectPoint{elementId=of:0000000000000001, portNumber=3}, dst=ConnectPoint{elementId=of:0000000000000002, portNumber=3}, type=DIRECT}}
Reason=LinkEvent{time=2014-10-29T12:41:44.389, type=LINK_REMOVED, subject=DefaultLink{src=ConnectPoint{elementId=of:0000000000000002, portNumber=3}, dst=ConnectPoint{elementId=of:0000000000000001, portNumber=3}, type=DIRECT}}
onos>
```
