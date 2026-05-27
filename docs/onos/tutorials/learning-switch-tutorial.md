# Learning Switch Tutorial

## **Introduction**

This tutorial will help you create a learning switch for ONOS by transforming pseudocode into functional code.

## **Getting Started**

Make sure you have ONOS installed, up, and running on a separate terminal. You can minimize that one. For instructions on how to download ONOS look at this [link](../../getting-onos-2130151.md). 

Move into the learningSwitch directory from the onos directory on your computer. If you are using terminal it's

$ cd LearningSwitch  (while in ONOS)

Then you can either use this command when inside the directory 

$ mvn clean install 

or download [home brew](http://brew.sh/) and use the command

$ brew maven

to download maven.

On a second terminal window if you want, you can start with a slightly more complex topology:

$ sudo mn --topo tree,3,3 --controller remote,[your IP address] --mac

After getting the topology up and running open up a web browser and type in:

<http://localhost:8181/onos/ui/>

it should take you to a login, (username: onos password: rocks). You should be able to see your topology on the screen.

Write your code in your favorite editor, by importing the LearningSwitch directory into it. I suggest using IntelliJ and [here's](https://wiki.onosproject.org/display/ONOS/Importing+ONOS+projects+into+IntelliJ+IDEA) a tutorial and screencast on how to import it. The code has documentation to help you, another useful resource is the [ONOS api](http://api.onosproject.org/1.6.0-rc2/).

## **Running Your Code**

In the LearningSwitch directory run mvn clean install after every code change then put in:

$ onos-app localhost reinstall! target/[artifact Id]-[version number].oar

The artifact Id can be found on the pom.xml file, same with the version number. When I inputted mine it was: onos-app localhost reinstall! target/learningSwitch-1.0.oar

If you change the topology, you have to re-run/restart ONOS.

 Remember to uncomment the actLikeSwitch method call and comment the actLikeHub method call. Also remember after installing your application, to delete or stop the reactive forwarding application. To test if your switch is working send a couple pings through. You could also use iperf to see the bandwidth between the hosts. It should be considerably faster in comparison to actLikeHub. Additionally, Wireshark is a useful resource to use, for debugging. If you want more help debugging on IntelliJ look at [this screencast.](https://www.youtube.com/watch?v=UzWcI9KvP0g)

## **Learning Switch APP on ONOS 2.4.0**

On ONOS 2.4.0 the Learning Switch folder can be found under the onos directory apps folder, if you are using terminals it's

$ cd apps/learning-switch  (while in ONOS)

This will give you access to the Learning Switch APP folder and you can find two java files under src/main/java/org/onosproject/learningswitch: LearningSwtichTutorial.java, which contains a empty model, and LearningSwtichSolution.java which is a filled example for a working Learning Switch.

You can learn how to create and deploy an ONOS Application at [this](screencasts/creating-and-deploying-an-onos-application.md) link.

## **Happy Coding!**
