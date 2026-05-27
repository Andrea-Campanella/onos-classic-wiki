# Installation

Welcome to TestON tutorial!

## Overview

TestON runs on Linux platform. TestON requires a proper ONOS installation in order to work, see [ONOS Tutorial](../../../tutorials.md) for more information.

By completing this tutorial, you will understand how to:

* Install TestON.
* Create appropriate files to run test on TestON.
* Create and run TestON script.
* Create a TestON driver.

**NOTE**: If you are having trouble running TestON, visit [TestON FAQs](teston-faqs.md) for additional information, or [email us](mailto:onos-discuss@googlegroups.com) if you're stuck.

## Configuring Linux to run TestON

### Requirements:

1. A Linux 2.6.26 or greater kernel compiled with network namespace support enabled (see INSTALL for additional information.)
2. Python 2.6 or higher.

Install python package configObj:

```
$ sudo pip install configObj
```

### **Prerequisites:**

* [Properly installed ONOS](#).
* Dependencies - ONOS, Python packages, Pox, [Mininet](https://github.com/mininet/mininet), STS, etc.
* Prior knowledge of ONOS and Mininet
* Two or more VMs running Ubuntu Server
* [Passwordless SSH login](http://www.linuxproblem.org/art_9.html)

## Installation

Clone the TestON from https://gerrit.onosproject.org/OnosSystemTest: 

```
git clone https://gerrit.onosproject.org/OnosSystemTest
```

Run the install.sh script:

```
cd OnosSystemTest/TestON/
./install.sh
```

Having installation problem? visit [TestON FAQ](teston-faqs.md) for more information.

## Exploring further

Now that you finish installing TestON, you can now create your test cases. Find out how you can create your own tests in [test files section](https://wiki.onosproject.org/x/iI8g) [of the tutorial.](https://wiki.onosproject.org/display/ONOS/Test+Files)

# Stuck? Found a bug? Questions?

Email [us](mailto:onos-discuss@googlegroups.com) if you’re stuck, think you’ve found a bug, or just want to send some feedback. Please have a look at the [guidelines](https://wiki.onosproject.org/display/ONOS/ONOS+Mailing+Lists) to learn how to efficiently submit a bug report.
