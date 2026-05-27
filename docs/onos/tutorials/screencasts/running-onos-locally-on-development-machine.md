# Running ONOS locally on development machine

## [YouTube Video](https://www.youtube.com/watch?v=B9PlKvTqjKQ)

## Overview

ONOS has been architected to run in a distributed configuration where multiple instances cooperate as a single cluster. However, there are times during the development when using a single ONOS instance is perfectly sufficient. This includes development of southbound providers, CLI, REST API and GUI among others.

In these cases, it can be much simpler to run ONOS directly on the development machine, using Karaf ‘*regular*’ mode which runs Karaf in the foreground.

In this screencast, which assumes you have your ONOS development environment already setup, we will show you exactly how this can be done.

## Selecting network adapter

First thing we need to do, is to identify the network adapter that will be used by ONOS for its cluster operation. Yes, even though there is really no cluster, this is required at this time. This step may be obsoleted in the near future.

In our demonstration we will choose the IP address that belongs to the *en0* adapter.

After selecting the IP address we will set the *ONOS\_IP* environment variable with that address.

## Setting up Apache Karaf for ONOS

To allow running ONOS directly on the development machine, ONOS toolbox comes with *onos-karaf* command, which makes sure that Apache Karaf is installed and properly configured to run ONOS before starting it.

So, after building ONOS using *onos-build*, which we have already done, we can run ONOS by simply invoking '*onos-karaf clean*'.

Please note that this tool is purposefully designed for development machines and is not intended to be used for production environments. It accepts the same arguments as does the original karaf command.

## ONOS console & log

Since ONOS runs in foreground Karaf, we will see the ONOS prompt very shortly, even while ONOS continues to startup. As developers, we may want to monitor the ONOS log file, which is located in the Karaf *data/log* directory.

We will do so by creating a new shell window and typing '*tl'* (for tail log) at the prompt. This will immediately start continuous monitoring of the log tail. There we can see various subsystems and components starting up and reporting on their progress.

## Filtering and searching the log

To filter the log monitor to show only select log entries, you can use the ‘tlo’ command with an extended regular expression pattern. By default, ‘*tlo*’ filters by *org.onosproject*|*org.onlab*.

## Using the ONOS console

From the ONOS console, we can access not only all of the Apache Karaf commands, but also a suite of commands for interacting with ONOS functionality. To get a list of available ONOS commands and a brief description of their purpose, simply type in ‘*help onos*’.

Note that the console support command and argument completion, so by simply typing onos and pressing tab, we can see the list of available ONOS commands.

For example, we can request a brief summary of the ONOS model, by typing summary. This will present us with an overview information specifying ONOS version, how many devices, links or hosts there are and similar high-level information.

To stop ONOS, simply type *halt* or press *Ctrl-D* key.

## Build & start

As with all other frequently used ONOS commands, onos-karaf has a shortcut alias called ‘*ok*’. This allows one to build and then immediately configure and run ONOS using the

‘*ob && ok clean*’ abbreviation.

## Conclusion

I hope you found this screencast informative. Have a great day... and happy coding!
