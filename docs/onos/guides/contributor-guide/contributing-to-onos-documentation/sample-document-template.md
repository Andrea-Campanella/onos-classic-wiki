# Sample Document Template

This is a sample template implementing some of the basic styling used on the ONOS wiki. This page is meant to be viewed from the editor so that someone trying to write a page can see the macros and settings that they use. From the editor, double click on any macro to see its settings.

The Table of Contents (ToC) macro is placed near the beginning of the page. It is set to *MaxLevel=3*, meaning only section headings formatted with up to Heading 3 are included in it.

## Overview

Major sections are started off with a header formatted with **Heading 2** sizing. Subsections will use higher heading levels (Heading 3, Heading 4, and so on)

### Like this subsection.

Notice how the subsection title of **Heading 3** sizing shows up indented under 'Overview' in the ToC.

#### And this sub-subsection in Heading 4

Also note how the higher heading sizes aren't captured by the ToC macro, as it has been limited to Heading 3.

### CLI content

Content copied/pasted from a CLI, or bits of code, are added in **Code Block**s set to *language=text* (Syntax highlighting set to 'Plain Text' in the setting dropdown) if syntax highlighting isn't desired.

```
$ sudo -s
# pwd
/usr/home/wiki
#
```

For large blocks of code, the Code Block can be made collapsible by checking the 'Collapsible' field in its setting, which adds a dropdown that can be clicked to display the full contents:

Expand source

```
$ ifconfig
vtnet0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=80028<VLAN_MTU,JUMBO_MTU,LINKSTATE>
        ether 8a:19:c8:1c:cf:32
        inet 192.168.64.15 netmask 0xffffff00 broadcast 192.168.64.255 
        nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
        media: Ethernet 10Gbase-T <full-duplex>
        status: active
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> metric 0 mtu 16384
        options=600003<RXCSUM,TXCSUM,RXCSUM_IPV6,TXCSUM_IPV6>
        inet6 ::1 prefixlen 128 
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x2 
        inet 127.0.0.1 netmask 0xff000000 
        nd6 options=21<PERFORMNUD,AUTO_LINKLOCAL>
epair0a: flags=8842<BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=8<VLAN_MTU>
        ether 02:ff:20:00:03:0a
        nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
        media: Ethernet 10Gbase-T (10Gbase-T <full-duplex>)
        status: active
epair0b: flags=8842<BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=8<VLAN_MTU>
        ether 02:ff:70:00:04:0b
        nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
        media: Ethernet 10Gbase-T (10Gbase-T <full-duplex>)
        status: active
epair1a: flags=8842<BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=8<VLAN_MTU>
        ether 02:ff:20:00:05:0a
        nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
        media: Ethernet 10Gbase-T (10Gbase-T <full-duplex>)
        status: active
epair1b: flags=8842<BROADCAST,RUNNING,SIMPLEX,MULTICAST> metric 0 mtu 1500
        options=8<VLAN_MTU>
        ether 02:ff:70:00:06:0b
        nd6 options=29<PERFORMNUD,IFDISABLED,AUTO_LINKLOCAL>
        media: Ethernet 10Gbase-T (10Gbase-T <full-duplex>)
        status: active
bridge0: flags=8802<BROADCAST,SIMPLEX,MULTICAST> metric 0 mtu 1500
        ether 02:3b:ec:08:6d:00
        nd6 options=9<PERFORMNUD,IFDISABLED>
        id 00:00:00:00:00:00 priority 32768 hellotime 2 fwddelay 15
        maxage 20 holdcnt 6 proto rstp maxaddr 2000 timeout 1200
        root id 00:00:00:00:00:00 priority 0 ifcost 0 port 0
```

### Images

Images can be added from **Insert more Content** (the '+') **> Image**.

![](https://upload.wikimedia.org/wikipedia/commons/f/fb/Phalacrocorax-auritus-007.jpg)

A larger image or figure's size is also usually adjusted to about 650px wide by entering a custom size. The settings can be accessed by clicking on the image after it's added.

### Lists

The list macro is probably the easiest to use if each item is a single line of text. If images, macros, or multiple lines are involved, it can get finicky (e.g. start numbering again from 1). Some tips are:

1. Add a line. Hitting **enter** creates a new bullet or numbered entry.
2. If another line is needed under the same number, hit **shift+enter**   
   to get to the   
   next line to prevent it from being numbered or bulleted.
3. Repeating **shift+enter** will continue adding newlines under the current bullet or number.  
     
   Macros and images added under a newline created by **shift+enter** will also be indented.  

   ![](https://upload.wikimedia.org/wikipedia/commons/f/fb/Phalacrocorax-auritus-007.jpg)

   1. **shift** by itself will indent the list. The same technique with **shift+enter** works for indented portions of a list, with a matching level of indentation.

      ```
      $ printf '%s\n' $((1+2))
      3
      ```
4. The list implicitly ends when **enter** is hit twice.

### Footer

Any links back to the parent, previous, or next page in the guide book are added as a footer with centered links, between two **Horizontal Rule**lines, as below:

---

[Return to: Contributing to ONOS Documentation](../contributing-to-onos-documentation.md)

---
