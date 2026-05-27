# Distributed Primitives

# Overview

ONOS offers a core set of primitives for managing distributed state. The goal behind is to make distributed state management and coordination simple and easily accessible to application developers. These primitives cater to different use cases by providing high availability, durability and a choice of two consistency modes: strong and eventual. All these primitives are designed with correctness, usability and performance at scale as key considerations.

Applications can create different instances of these primitives for managing their state.

# EventuallyConsistentMap

An [eventually consistent](http://en.wikipedia.org/wiki/Eventual_consistency) map provides weaker consistency guarantees in return for superior read/write performance. All reads are performed on local state and all writes update local state first and subsequently propagate updates to other replicas in the background. Users can configure this map with a ClockService that will be used to time stamp various update events. The timestamps are used to ensure each replica applies updates to local state in the correct order. The map fixes replicas that get out of sync (due to lost updates) via a light weight background process known as anti-entropy. This ensures that the system state across all replicas eventually converges to the correct state.

An eventually consistent map fully replicates all its state. That means each node in the cluster will have a full copy of the map contents. The state is stored in memory on each node and that means a full cluster restart will result in data loss. In Cardinal, we will be introducing an option to persist data to disk so that it can survive a full cluster restart.

# ConsistentMap

Applications that require stronger consistency guarantees can use the ConsistentMap primitive. ConsistentMap supports java.util.concurrent.ConcurrentMap style conditional update operations and it ensures that all operations for any given key (in the map) are serialized for strong consistency. The underlying protocol that lets us achieve this is [Raft](http://en.wikipedia.org/wiki/Raft_%28computer_science%29). Furthermore, the entire key space (for the map) is partitioned so as to ensure good scale out characteristic. i.e. each key in the ConsistentMap maps to a single partition or shard. Consistency of each shard is maintained via a separate Raft consensus cluster. This ensures that operations on keys mapped to different partitions can proceed independently. In a N node cluster, by default we create N shards. The responsibility for each shard lies with 3 different nodes thereby ensuring shard availability even if one of its nodes fails.

# LeadershipService

ONOS has a service to facilitate leader election for arbitrary topics. The service ensures that at any given point in time a single controller node acts as a leader for a given topic. The LeadershipService can at any given point in time facilitate leader election for multiple topics and likewise each controller node can simultaneously be in the leadership race for multiple topics.

# DistributedSet

As the name suggests this is a data structure that provides set semantics in a distributed context.

# DistributedQueue

Provides a distributed FIFO queue abstraction with support for non-blocking dequeue operations via long polling.

# AtomicCounter

This is similar to [AtomicLong](http://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/AtomicLong.html) but in a distributed setting. It is useful for vending globally unique counter values.

# AtomicValue

A distributed version of [AtomicReference](http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/atomic/AtomicReference.html).

# LogicalClockService

This service is useful for assigning globally ordered time stamps to various events. This will be useful for ordering events in a distributed setting.

# ClusterCommunicationService

This service is more basic in its functionality and lets a controller instance communicate with others by making RPCs. A controller can register handlers that get invoked when messages of certain type are received. The service supports various cluster wide communication primitives such as: unicast, multicast and broadcast

# ClusterService

This service can be used to discover other nodes in the cluster and their current state (alive or dead)
