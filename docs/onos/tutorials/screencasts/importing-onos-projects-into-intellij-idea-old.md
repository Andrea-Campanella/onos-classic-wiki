# Importing ONOS projects into IntelliJ IDEA (old)

> This page is out of date and applied to releases before 1.14 - for up to date instructions see [Using an IDE with ONOS 1.14 or higher (Bazel build)](../../guides/developer-guide/development-environment-setup/using-an-ide-with-onos-1.14-or-higher-bazel-build.md)
>
> The Youtube Video has been removed

## Overview

In this screencast we will show you how easy it is to import ONOS code into the IntelliJ IDE. This demonstration assumes that the ONOS code has already been checked out and preferably also built using the *onos-build* command.

## Importing the project

To import the ONOS project, simply open IntelliJ IDEA and select: *File… New… Project from Existing Sources*

If you are starting IDEA for the very first time and don’t have any existing projects, you can alternatively select: *Import Project…* from the initial options.

When presented with a file selection dialog, you should navigate to the top of the ONOS source tree and select the root *pom.xml* file. This will initiate the project import wizard.

On the first screen we only need to check Sources and Documentation and then press *Next*.

Select *Next* to bypass the Maven profiles.

Make sure that the *org.onosproject:onos* Maven project is selected and press *Next*.

After this select the JDK 8. If selecting JDK for the very first time, you may need to press the + sign to locate the JDK home directory. Press *Next* and then *Finish*.

At this point IntelliJ will complete the import process by building the project and indexing the source files.

## Importing the settings

While the project is being processed, we can go ahead and import the recommended IDEA settings. We do this by selecting *File… Import Settings…* and then navigating to the ONOS *tools/dev* directory and selecting the *idea-settings.jar* file. We can complete the process by pressing the *OK* button.

## Importing the Copyright header

Since ONOS is licensed under Apache 2 license, we need to make sure that all source files are properly decorated with the Apache 2 license header file.

To configure IntelliJ appropriately, we will locate the *header.txt* file under ONOS *tools/dev* directory and copy its contents. Then, from IntelliJ preferences, we will select Copyright section and add a new new copyright profile. We will call this profile ONOS and paste in the previously copied header text.

Then we will make sure that the newly created ONOS copyright profile is the default and we are done.

## Navigating the source tree

At this point, the ONOS project should be fully processed and we are free to navigate and search the codebase.

Pressing *Command-N* or double-tapping the *Shift* key, we can bring up the search window where we can type our search term.

Let’s search for *Device*. When the *Device.java* file is open, we can see that it is an interface. Clicking on the down-arrow next to the interface declaration will open the list of implementations. We will select *DefaultDevice* to open this particular implementation source.

Right clicking on the *DefaultDevice* implementation we can select various options, including *Diagrams...* where we can select *Show Diagram…* to reveal the UML of the class hierarchy for the *DefaultDevice* class.

## Executing unit tests

Most IDEs allow developers to execute unit tests directly from the work-bench. IntelliJ is among them. There are many different ways to do this. For example, right-clicking on a section of the source tree, will execute all unit tests contained within.

## Conclusion

This was just a quick overview of how to import the ONOS source code into the IntelliJ IDE. I hope you found this useful and I look forward to seeing your contributions to the codebase.

Have a great day… and happy coding!
