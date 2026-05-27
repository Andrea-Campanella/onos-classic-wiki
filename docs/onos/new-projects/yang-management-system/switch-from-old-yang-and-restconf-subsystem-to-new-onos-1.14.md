# Switch from old Yang and Restconf subsystem to new (ONOS 1.14)

New Yang model and Restconf system may requires putting **namespace** or **module name** to the value if the value is an **identity** or an element which belongs to a specific namespace or module

For example, the fpc agent model defines two identity **zmq-dpn-control-protocol** and **p4-dpn-control-protocol**:

**fpc.yang**

```
module fpc {
    yang-version 1;
    namespace "urn:onos:params:xml:ns:yang:fpc";
    prefix "fpc";

    import ietf-dmm-fpcagent { prefix fpcagent; }
    import ietf-dmm-fpcbase { prefix fpcbase; }
    import ietf-inet-types { prefix inet; }
    import ietf-dmm-fpc-pmip { prefix fpc-pmip; }
    import ietf-dmm-threegpp { prefix threegpp; }

    revision "2015-01-05" {
        description "Initial revision of fpc model";
    }

    // New DPN Type
    identity zmq-dpn-control-protocol {
      base "fpcbase:fpc-dpn-control-protocol";
    }

    identity p4-dpn-control-protocol {
      base "fpcbase:fpc-dpn-control-protocol";
    }

    typedef membership-match-type {
      type enumeration {
        enum eq { value 0; }
        enum super { value 1; }
        enum psuper { value 2; }
        enum sub { value 3; }

// Ignore rest of definitions.........
```

With old version of Yang and Restconf system. We can send an HTTP POST with follow format and URL:

**Old HTTP POST**

```
{
    "dpns": [
        {
            "dpn-id": 'my-dpn',
            "dpn-name": "site1-anchor1",
            "dpn-groups": [
                "foo"
            ],
            "node-id": "nodemy-dpn",
            "network-id": "networkmy-dpn",
            "control-protocol": "zmq-dpn-control-protocol",
            "abstract": false
		}
	]
}

http://localhost:8181/onos/restconf/data/ietf-dmm-fpcagent:tenants/tenant=default/fpc-topology
```

This works well with old Yang and Restconf subsystem.

However, after upgrading to new subsystem, the serializer requires more strict checking. It requires to add namespace or module name to the value if the value uses identity or something belongs to a specific namespace or module.

For example:

**New HTTP POST**

```
{
    "dpns": [
        {
            "dpn-id": 'my-dpn',
            "dpn-name": "site1-anchor1",
            "dpn-groups": [
                "foo"
            ],
            "node-id": "nodemy-dpn",
            "network-id": "networkmy-dpn",
            "control-protocol": "urn:onos:params:xml:ns:yang:fpc:zmq-dpn-control-protocol",
            "abstract": false
		}
	]
}

http://localhost:8181/onos/restconf/data/ietf-dmm-fpcagent:tenants/tenant=default/fpc-topology
```
