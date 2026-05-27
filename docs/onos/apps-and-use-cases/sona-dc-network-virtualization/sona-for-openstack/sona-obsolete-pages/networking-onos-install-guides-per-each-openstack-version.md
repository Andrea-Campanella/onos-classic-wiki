# networking-onos install guides per each OpenStack version

# Neutron, OpenStack, networking-onos dependency package comparison

| python package | neutron (stable/newton) | Upper constraint (stable/newton) | neutron (stable/ocata) | Upper constraint (stable/ocata) | networking-onos (master) |
| --- | --- | --- | --- | --- | --- |
| pbr | >=1.6 | ===1.10.0 | >=1.8 | ===1.10.0 | !=2.1.0,>=2.0.0 |
| Babel |  | ===2.3.4 |  | ===2.3.4 | !=2.4.0,>=2.3.4 |
| stevedore | >=1.17.1 | ===1.17.1 | >=1.17.1 | ===1.20.0 | >=1.16.0 |
| debtcollector | >=1.2.0 | ===1.8.0 | >=1.2.0 | ===1.11.0 | >=1.2.0 |
| neutron-lib | >=0.4.0 | ===0.4.0 | >=1.1.0 | ===1.1.0 | >=1.3.0 (>= 1.1.0 works well) |
| oslo.config | >=3.14.0 | ===3.17.1 | !=3.18.0,>=3.14.0 | ===3.22.0 | >=3.22.0 |
| oslo.db | !=4.13.1,!=4.13.2,>=4.10.0 | ===4.13.5 | >=4.15.0 | ===4.17.0 | >=4.19.0 |
| oslo.log | >=1.14.0 | ===3.16.0 | >=3.11.0 | ===3.20.1 | >=3.22.0 |
| oslo.i18n | >=2.1.0 | ===3.9.0 | >=2.1.0 | ===3.12.0 | >=2.1.0 |
| oslo.serialization | >=1.10.0 | ===2.13.0 | >=1.10.0 | ===2.16.0 | >=1.10.0 |
| oslo.utils | >=3.16.0 | ===3.16.0 | >=3.18.0 | ===3.22.0 | >=3.20.0 |
| oslo.context | >=2.9.0 | ===2.9.0 | >=2.9.0 | ===2.12.1 | >=2.12.0 |
| oslo.policy | >=1.9.0 | ===1.14.0 | >=1.17.0 | ===1.18.0 | >=1.17.0 |
| oslo.concurrency | >=3.8.0 | ===3.14.0 | >=3.8.0 | ===3.18.0 | >=3.8.0 |
| oslo.messaging | >=5.2.0 | ===5.10.1 | >=5.14.0 | ===5.17.1 | >=5.19.0 |
| oslo.middleware | >=3.0.0 | ===3.19.1 | >=3.0.0 | ===3.23.1 | >=3.10.0 |

# How to install networking-onos in each OpenStack version

### stable/newton

* neutron-lib version for networking-onos needs to be >= 1.1.0, and other packages can be installed following the OpenStack upper constraints.
* When DevStack is used to install OpenStack, AFTER install of networking-onos, neutron-lib version needs to be fixed to 1.1.0 in requirements/upper-constraint.txt file before the execution of stack.sh.
* When using package install, after Neutron is installed, please install networking-onos without any dependencies using setup.py, and then upgrade neutron-lib to 1.1.0 with keeping the versions of libraries as listed above in the table.

**Recommended way**

After installing Neutron server in any method, please install networking-onos using 'setup.py install' as usual. Then, update neutron-lib as below.

|  |
| --- |
| `$ git clone https:``//github``.com``/openstack/requirements``.git -b stable``/newton` `$``sed` `-i -e``'s/neutron-lib===0.4.0/neutron-lib===1.1.0/g'` `requirements``/upper-constraints``.txt` `$``sudo` `pip``install` `-c requirements``/upper-constraints``.txt neutron-lib` |

### stable/ocata

* upper constraint versions of Neutron and OpenStack work for networking-onos (however, please note that the versions written in the requirements.txt are different).
* When using DevStack, install networking-onos using 'setup.py install' without any dependencies.
* When using package install, after installing Neutron server, install networking-onos using 'setup.py install' without dependencies.

# Reference

[1] Neutron package version information <https://github.com/openstack/neutron/blob/stable/newton/requirements.txt>

[2] networking-onos package version information <https://github.com/openstack/networking-onos/blob/master/test-requirements.txt>

[3] OpenStack Global package version information <https://github.com/openstack/requirements/blob/stable/newton/upper-constraints.txt>

Please note that this information is contributed by Hyunsun Moon.
