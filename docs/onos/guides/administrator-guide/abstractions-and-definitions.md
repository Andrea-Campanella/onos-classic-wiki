# Abstractions and definitions

![](https://docs.google.com/a/onlab.us/drawings/d/sIct5djP0PgBFekZbDfYjrw/image?w=378&h=322&rev=98&ac=1)Platforms like ONOS can be deployed in a variety of different ways, using different technologies, applications, custom scripts, on top of different OSes. The goal of the suggested installation steps (and of this guide) is not to provide low level details about specific platforms or technologies, outside ONOS. You may find more specific walkthroughs (i.e. for Docker, Vagrant, Puppet, ...) elsewhere.

Being able to operate the same software on different operating systems is not a trivial task. The ONOS community is committed to make this happen in the smoothest way possible. As a result, the installation process and the guide isn't tied too closely to a specific OS, with some exceptions (like which commands to use to start services). Keeping this in mind, you should be aware that the ONOS core team has chosen **Ubuntu 16.04 LTS** for development. Using Ubuntu should make your deployment process easier, and might increase your chances to find useful replies using the community tools (i.e. other pages in the wiki, or mailing lists).

For the reasons explained above, the guide will use the following abstractions and terminology (represented in the picture):

* **Target machine**: a machine (physical, virtual, container, ...) where ONOS runs. ONOS can be deployed and managed on a target machine either locally (from the machine itself), or from a remote machine, called management machine. At least one target machine is needed to install and run ONOS.
* **Management machine**: an optional machine (physical, virtual, container, ...) meant for operators, used to deploy and manage ONOS from a single position on one or more target machines. The management machine is optional.
* **Cluster**: a set of target machines working together as a distributed system. This allows ONOS to spread the load, being able to better scale and improve performances.
