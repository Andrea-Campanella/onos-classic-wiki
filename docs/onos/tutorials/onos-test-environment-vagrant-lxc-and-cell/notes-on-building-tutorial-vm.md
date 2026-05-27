# Notes on building tutorial VM

This describes the steps and requirements to build the tutorial VM containing Mininet, three LXC containers used as ONOS target machines and tutorials: basic, sdnip, optical and distributed.

# Software Requirements

Host OS: Ubuntu Xenial

Software Packages:

1. Virtualbox
2. Vagrant with plugins vagrant-disksize

# Procedures

Check out the master branch:

`$ git clone https:``//gerrit.onosproject.org/onos`

Please run below commands to build the tutorial VM:

`$ cd $ONOS_ROOT/tools/dev/vagrant`  
`$ vagrant up tutorialvm`
