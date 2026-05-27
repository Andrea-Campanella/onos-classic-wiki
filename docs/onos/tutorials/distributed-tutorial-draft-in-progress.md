# Distributed Tutorial [DRAFT IN PROGRESS]

ONOS …  Tutorials and Walkthroughs

Distributed ONOS Tutorial

Created by Ali "The Bomb" Al-Shabibi, last modified by Thomas Vachuska on Mar 11, 2016

**Welcome to the Distributed ONOS Tutorial**.

In this tutorial, you will learn to write a distributed ONOS application. The application you will be writing is called BYON (Build Your Own Network). This tutorial will teach you how to implement an ONOS service, an ONOS store, and how to use parts of the CLI and Northbound API. (smile)

(Here are some slides that can be used to accompany the tutorial: [Slides](https://docs.google.com/presentation/d/1sKmbCmndgGlWE4lqZxb8FmR_1so7Ul4ELb80sWV2qck/edit#slide=id.p))

# Introduction

## Pre-requisites

You will need a computer with at least 2GB of RAM and at least 5GB of free hard disk space. A faster processor or solid-state drive will speed up the virtual machine boot time, and a larger screen will help to manage multiple terminal windows.

The computer can run Windows, Mac OS X, or Linux – all work fine with VirtualBox, the only software requirement.

To install VirtualBox, you will need administrative access to the machine. More information on VirtualBox installation and setup can be found at the [ONOS from Scratch Tutorial](onos-from-scratch.md).

The tutorial instructions require prior knowledge of SDN in general, and OpenFlow and Mininet in particular. So please first complete the [OpenFlow tutorial](http://archive.openflow.org/wk/index.php/OpenFlow_Tutorial) and the [Mininet walkthrough](http://mininet.org/walkthrough/). Also being familiar with [Apache Karaf](http://karaf.apache.org/) would be helpful although not entirely required.

## Stuck? Found a bug? Questions?

Email [us](mailto:onos-discuss@googlegroups.com) if you’re stuck, think you’ve found a bug, or just want to send some feedback. Please have a look at the [guidelines](../community-information/mailing-lists.md) to learn how to efficiently submit a bug report.

# Set up your environment

## Install required software

You will need to acquire two files: a [VirtualBox](https://www.virtualbox.org/) installer and the latest Tutorial VM from the [Download packages and tutorial VMs](../../redirect-pages-not-in-main-menu/download-packages-and-tutorial-vms.md) page (under Tutorials).

After you have downloaded VirtualBox, install it, then go to the next section to verify that the VM is working on your system.
