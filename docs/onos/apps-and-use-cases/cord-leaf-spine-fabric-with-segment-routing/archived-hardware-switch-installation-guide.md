# [Archived] Hardware Switch Installation Guide

Deprecated

This page is deprecated and may be removed in a near future.  
The new entry point of Trellis underlay fabric installation guide can be found at [Fabric Installation Guide](https://wiki.opencord.org/display/CORD/Fabric+Installation+Guide).

## Introduction

In this wiki page, we are going to show you how to setup the hardware switches for CORD Fabric.  
Here we focus on **Accton 6712 40G x 32** switches, which are the switches we use to build the CORD Pod in ON.Lab.  
Ideally, all hardware switches running OF-DPA pipeline should be compatible with the Fabric control logic (i.e. Segment Routing app on ONOS)

## Wire Up

Connect power cable, console port and management network.

## Install Open Networking Linux (ONL)

The switches are shipped with Open Networking Install Environment (ONIE) bootloader. After booting up, we should see the ONIE prompt from console.  
Here we assume that the management port on the switch already has Internet access. (via DHCP)  
In the console, type

```
At the ONIE prompt, we need to get and install ONL. Depending on the switch model you are using,
we need to use different installers from here:
http://opennetlinux.org/binaries/2016.01.04.21.46.18cc76084b3104961117aa8434599c8c67a9a276

For powerpc based 5710, use onl-18cc760-powerpc-all.2016.01.04.21.45.installer
For x86 based 5712 and 6712, use the onl-18cc760-amd64-all.2016.01.04.21.36.installer

ONIE:/ # wget <installer-url>
ONIE:/ # sh <installer-filename>
```

to fetch and install the latest ONL.

The switch will automatically reboot into ONL after installation. Default login credential of ONL is: **root/onl**

## Configure Management Interface

We might want to configure a fixed IP address for the management interface.  
First edit **/etc/network/interfaces** and configure **ma1**, which is the management interface.

```
auto ma1
iface ma1 inet static
address 10.128.10.128
netmask 255.255.0.0
gateway 10.128.0.1
dns-nameservers 192.168.1.1 8.8.8.8
```

Second, we need to make the configuration file persistent so we don't lose the configuration after rebooting the switch. **This step is required for every config file in the switch**.

```
# persist /etc/network/interfaces
# savepersist
```

## Install OF-DPA package

The OF-DPA package is a Debian package that includes the OF Agent.

You need this file for 6712s and 5712s which are both x86 based: ofdpa-i.12.1.1\_12.1.1+accton1.7-1\_amd64.deb

For 5710s use the powerpc debian package: ofdpa-i.12.1.1\_12.1.1+accton1.7-1\_powerpc.deb

Download from here:

<https://github.com/onfsdn/atrium-docs/tree/master/16A/ONOS/builds>

Please note: Only this version of OF-DPA will work for the fabric!

Copy the package to **/mnt/flash2** on the switch so it is persistent after rebooting.

```
$ scp ofdpa-i.12.1.1_12.1.1+accton1.7-1_amd64.deb 10.128.10.128:/mnt/flash2
```

Install the OF-DPA package. (Note that this is required every time after rebooting. I will show a trick later so it can be done automatically.)

```
# service ofdpa stop
# dpkg -i --force-overwrite /mnt/flash2/ofdpa-i.12.1.1_12.1.1+accton1.7-1_amd64.deb
```

## (Optional) Configure OF-DPA

By default, all 32 ports are running in 1x40G mode. The **/etc/accton/ofdpa.conf** need to be modified if we want to break out 1x40G into 4x10G.

```
port_mode_1=4x10g    # front port 1
```

Restart ofdpa service after modifying the config

```
# service ofdpa restart
# persist /etc/accton/ofdpa.conf
# savepersist 
```

## Run ONOS

Please follow the same instruction as described in [[Archived] Software Switch Installation Guide](archived-software-switch-installation-guide.md) ONOS section.

Host learning is not fully supported with OFDPA switches at this moment. Please refer to [Network Config Host Provider](../../guides/administrator-guide/configuring-onos/the-network-configuration-service/network-config-host-provider.md) and configure host manually. Detail: [CORD-86](https://jira.opencord.org/browse/CORD-86)

## Run Indigo OpenFlow Agent

Run Indigo OpenFlow Agent to connect the switch to controller(s)

```
# brcm-indigo-ofdpa-ofagent --dpid=0x0000000000000001 --controller=10.128.10.5 --controller=10.128.10.6 --controller=10.128.10.7
```

## (Optional) Useful Configurations

As mentioned, the OF-DPA package need to be installed every time switch is rebooted. We can add it into **/etc/rc.local** so it will be automatically installed

```
hostname fabric-spine1
dpkg -i --force-overwrite /mnt/flash2/ofdpa-i.12.1.1_12.1.1+accton1.7-1_amd64.deb
```

Save /etc/rc.local and make it persistent

```
# persist /etc/rc.local
# savepersist 
```

## Useful Commands

There are some useful commands under **/usr/bin/ofdpa-2.0-ea3/examples/**

```
client_cfg_purge
client_debugcomp
client_debuglvl
client_drivshell
client_event
client_flowtable_dump
client_grouptable_dump
client_oam_dump
client_port_table_dump
client_tunnel_dump
ofdpa_bridging.py
ofdpa_mplsl3vpn.py
ofdpa_mpls_lsr_ecmp.py
ofdpa_mpls_lsr.py
ofdpa_pktrx_setup.py
ofdpa_pktrxtx.py
OFDPA_python.py
ofdpa_routing.py
ofdpa_srcmac_learn.py
ofdpa_vxlan.py
```

## Debugging

Sometimes the switch fails to install OpenFlow rules because they are not compliant with the OFDPA requirements. In these cases you may want to run OFDPA in debug mode to get more insight on how to properly install the flow rules. To enable debugging mode type the following:

```
# service ofdpa stop
# KERNEL_MODS=/lib/modules/`uname -r`/ofdpa
# insmod $KERNEL_MODS/linux-kernel-bde.ko dmasize=32M maxpayload=128
# insmod $KERNEL_MODS/linux-user-bde.ko
# ofdpa -d4 -c1 -c2 -c3 -c4 -c5
```

Now, open a new terminal and enter the following:

```
# ./client_debugcomp -c 1
# ./client_debugcomp -c 2
# ./client_debugcomp -c 3
# ./client_debugcomp -c 4
# ./client_debuglvl 3
# brcm-indigo-ofdpa-ofagent ...
```

The above commands may fail if ofdpa has not been initialized yet. If that happens, wait 10-20 seconds and try it again.

After this, you should be able to see more comprehensible messages.

### Recovery from a faulty ONL install

If, for some reason, the ONL install process fails, you may be brought to the grub rescue prompt upon reboot. You may or may not find system files, or even basic grub rescue commands (i.e. 'help'). There are two options for returning to a (known working) ONIE prompt.

1. **Reinstaller** - Accton provides a ISO for reinstalling the firmware to factory default. This can be acquired from Accton by registering for their online support, and applying for it [here](http://www.edge-core.com/OnlineReg.asp).  
   Once you have the ISO, you can either use PXE or a live USB to boot the switch into the image.
2. **Manually boot to ONIE** - If the files are there, you can manually configure GRUB to load the necessary modules to boot back into ONIE.

   ```
   # This should be the partition on the ONIE partition on the AS6712. 
   # It might be hd1 or hd0. Change appropriately. 
   grub rescue> ls (hd0,gpt2)/
   ./ ../ lost+found/ onie/ grub/ grubenv

   # These instructions will load the kernel and ONIE initrd. 
   grub rescue> set prefix=(hd0,gpt2)/grub
   grub rescue> set root=(hd0,gpt2)
   grub rescue> insmod normal
   grub rescue> insmod linux
   grub rescue> ls /onie
   ./ ../ vmlinuz-3.2.35-onie initrd.img-3.2.35-onie tools/ grub/ grub.d/ config/

   # if the ",115200n8" is omitted, baud rate defaults to 9600.
   grub rescue> linux /onie/vmlinuz-3.2.35-onie console=tty0 console=ttyS1,115200n8
   grub rescue> initrd /onie/initrd.img-3.2.35-onie

   # The system will not boot into ONIE and you can recover or re-install from there. 
   grub rescue> boot
   ```

Once back at the ONIE prompt, you can try to install ONL by following the same steps again.
