# SONA Troubleshooting

## VM creation error: Unable to add port "tapxxx" to OVS bridge br-int: Operation not permitted

```
.....
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31]     rv = execute(f, *args, **kwargs)
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31]   File "/usr/local/lib/python2.7/dist-packages/eventlet/tpool.py", line 122, in execute
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31]     six.reraise(c, e, tb)
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31]   File "/usr/local/lib/python2.7/dist-packages/eventlet/tpool.py", line 80, in tworker
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31]     rv = meth(*args, **kwargs)
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31]   File "/usr/local/lib/python2.7/dist-packages/libvirt.py", line 900, in createWithFlags
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31]     if ret == -1: raise libvirtError ('virDomainCreateWithFlags() failed', dom=self)
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31] libvirtError: Unable to add port tap47188ecf-b2 to OVS bridge br-int: Operation not permitted
2015-12-08 08:08:23.924 TRACE nova.compute.manager [instance: 9c3f2a76-9ff6-4b47-81ad-8812ae0aad31]
```

If you upgraded or manually installed OVS, this can be caused by libvirtd fails to find `ovs-vsctl` or refers to the stale version of the binary. Try to cleanup the existing OVS and install it again. [This guide](https://github.com/mininet/mininet/wiki/Installing-new-version-of-Open-vSwitch) works very well for me (don't forget to change the version in the guide to 2.3.0 or later).

## Authentication failure due to Keystone version 2.0 is not supported

SONA version lower than ONOS 1.10 does not support Keystone 3.0. Refer to the following link to enable Keystone 2.0 in OpenStack.

<https://ask.openstack.org/en/question/93199/how-to-enable-keystone-v2-on-mitaka/>
