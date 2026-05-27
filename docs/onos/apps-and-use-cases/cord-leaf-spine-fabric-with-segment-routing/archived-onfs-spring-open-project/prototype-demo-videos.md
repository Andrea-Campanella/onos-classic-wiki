# Prototype & Demo Videos

## Part 1: Segment Routing Prototype

In the first part of this demonstration, we set the stage for the following videos by describing the Segment-Routing prototype. We use the controller CLI to access router information such as configuration, statistics and flow table entries in the IP, MPLS, ACL and Group Tables.

## Part 2: Tracing a Segment Routed Ping

In the second part of this demonstration, we trace a ping through the Segment Routed data-plane. We use the controller CLI to show the flows that get ‘matched-on’ as the packets traverse the network, using ECMP shortest paths, Node-Segment IDs (globally significant labels) and Penultimate Hop Popping (PHP).

## Part 3: Recovering from Failures

In the third part of the demonstration of the Segment Routing prototype, we show how the system recovers from link failures.

## Part 4: Creating Segment Routed Tunnels and Applying Policies

In the fourth part of this SR demo, we show how the network operator can create loose-hop SR tunnels, and then apply policies that direct specific traffic flows into those tunnels, thereby overriding the default routing behavior.

## Part 5: Fine Grained Traffic Steering with Segment Routing

In the fifth part of this SR demo, we show how the network operator can perform fine-grained traffic steering by creating strict-hop Segment Routed tunnels, and using Adjacency Segment IDs (locally significant labels) to select one of several outgoing interfaces in a router.

## Part 6: Load Balancing on Non-ECMP Paths

In a Segment Routed network, by default the traffic takes the ECMP shortest path to the destination. In the sixth part of this SR demo, we show how the network operator can load-balance traffic on Non-ECMP paths by using Adjacency Segment IDs configured on multiple outgoing interfaces.

## Part 7: Segment Stitching of SR Tunnels

In the seventh part of this demo, we show a unique feature we have developed which we call ‘Segment Stitching’. Some SR tunnels may require deep-label stacks (for example more than 3 labels deep) to be imposed on packets at the ingress Segment Router. Merchant Silicon ASICs often have limitations on the number of labels that can be pushed on to outgoing packets. In this prototype, the controller overcomes this limitation ‘under-the-hood’, by stitching parts of the tunnel (label-stack) together at  appropriate stitch-points in the network.

## Part 8: Dell Segment Router

In the final part of this demo, we show many of the same features we have shown in the previous videos, except this time we show them working on Dell 4810 Open Networking Switches.
