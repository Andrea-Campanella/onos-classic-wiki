# Using an IDE with ONOS 1.14 or higher (Bazel build)

## IDE Setup

The project does not enforce the use of a specific IDE, but rather suggest the use of IntelliJ IDEA community edition which is free.

The following examples and documentation focus on IntelliJ IDEA. For other IDEs, developers should consult the documentation for the IDE of choice for specific configuration steps. 

To get the best development experience for ONOS, the team suggests using **IntelliJ 2019.3.4** with the **Bazel plugin installed**.

You can find and download IntelliJ versions here: <https://www.jetbrains.com/idea/download/previous.html>

If you have no idea where to start, [here are some instructions on how to install IntelliJ.](http://www.hildeberto.com/2014/09/installing-intellij-idea-on-mac-and-ubuntu.html)

## Bazel plugin Installation

After having downloaded and installed IntelliJ, ONOS requires the Bazel plugin to be installed.

1. Go into ***IntelliJ IDEA > Preferences > Plugins*** and search for **Bazel**
2. Click on **Install**
3. Wait for download and installation
4. Restart IntelliJ

More information on how to install the Bazel plugin can be found here: <https://ij.bazel.build/docs/bazel-plugin.html>

Using more recent versions of IntelliJ

**IMPORTANT!** After a new version of IntelliJ is released, you might need to wait a few weeks since a compatible version of the Bazel plugin is released as well. Before updating IntelliJ or choosing to download a newer version, check the version requirements for the Bazel plugin: <https://plugins.jetbrains.com/plugin/8609-bazel>. Alternatively, if you can't wait using the latest shiny features of IntelliJ, you might try building the Bazel plugin yourself without waiting for an official release: <https://github.com/bazelbuild/intellij>

## Importing the ONOS source

Assuming you have [obtained the source code already](getting-the-onos-core-source-code-using-git-and-gerrit.md) and Installed the Bazel plugin form the previous section, the following steps can be followed to import ONOS into IntelliJ:

1. To import the ONOS project, simply open IntelliJ and select ***Import Bazel Project*** from the welcome screen if it's your first time using Intellij. Otherwise select ***File > Import Bazel Project**.*
2. The next window asks you for the ***Bazel Workspace***, click on the three dots (*...*) on the right, **navigate to the ONOS folder and select it**, the path should appear in the widows' box. Press ***Next**.*
3. The next window asks you to ***Select a project view.*** Here you need to select a **.bazelproject file**, **see the next section to create one**, then press ***Next**.*
4. Select***Finish*** to import the ONOS project.

More information on how to import a Bazel project can be found here: <https://ij.bazel.build/docs/import-project.html>

## Creating a .bazelproject file

ONOS is not shipped with an existing .bazelproject file, for this reason, we will need to create one. This file defines which part of the source tree IntelliJ needs to be aware of and how. When importing a project in IntelliJ, you can choose the option ***Create from scratch***, which will generate a generic configuration that looks like this:

**.bazelproject**

```
workspace_type: java
java_language_level: 8 # or 11 if you are building ONOS version 2.2 or higher

directories:
  .

targets:
  //...
```

Essentially, here we tell IntelliJ to **import ALL directories and ALL Bazel targets** (`//...`). Since ONOS is quite a big project, **importing all targets for the first time can take more than 20 minutes depending on your configuration**. Unfortunately, this .bazelproject configuration will make the IDE build and import many targets that are not needed for development (such as OSGi and test coverage artifacts).

### Generate a minimal .bazelproject file (recommended)

To reduce the number of imported targets and**to speed up the import process** we have created a tool to auto-generate a minimal .bazelproject file for ONOS that imports only the targets needed for Java development. To auto-generate a .bazelproject file **when importing ONOS for the first time in IntelliJ**:

1. Auto-generate a temporary project file:

   ```
   cd onos/tools/dev/bin/
   ./onos-gen-bazel-project > /tmp/onos_bazelproject
   ```
2. In the ***Select Project View***window when importing the project in IntelliJ, select ***Copy external*** and insert the location of the generated file: `/tmp/onos_bazelproject`

With this option, **it should take around 10 minutes to import the project for the first time**.

### Update an existing .bazelproject file

This tool creates a project file that imports the relevant targets available in ONOS at the time the tool is executed. If you create a new app/library in ONOS, or if you check out a different branch with different targets, you might want to update your existing .bazelproject file to reflect the changes:

```
cd onos/tools/dev/bin/
./onos-gen-bazel-project > $ONOS_ROOT/.ijwb/.bazelproject
```

This will replace the project file previosuly created during the import process.

To load the new .bazelproject file and re-sync your project, in the top menu select ***Bazel > Sync > Sync project with BUILD*** files. **It should take only a few seconds to re-sync the project after the first import.**

## Import Troubleshooting

If your import fails with the error ***Error:Cannot run program "bazel" (in directory ): error=2, No such file or directory,****it means*IntelliJ did not properly pick-up the locationof the Bazel binary andwe need to change it.

1. Go into ***Intellij IDEA > Preferences > Bazel Settings***
2. Under ***Bazel Binary Location*** click on the three dots (*...*) on the right and select the location you installed Bazel in ( e.g. **/usr/local/bin/bazel**). You can also type the Bazel path.
3. Re-start the import process by re-syncing the project, in the top menu select ***Bazel > Sync > Sync project with BUILD files***

More information on this error can be found here: <https://github.com/bazelbuild/intellij/issues/230>

## Importing the settings

While the project is being processed, we can go ahead and import the recommended IntelliJ settings. We do this by selecting *File… Import Settings…* and then navigating to the ONOS*tools/dev* directory and selecting the *idea-settings.jar* file. We can complete the process by pressing the *OK* button.

These settings have the JDK home setup for OS X (`/Library/Java/JavaVirtualMachines/<JDK-VERSION>/Contents/Home`). For Linux, select  *File... Project Structure...* *SDKs...* then edit the JDK home path for to be `/usr/lib/jvm/<JDK-VERSION>`. If IntelliJ is throwing errors such as "cannot resolve symbol string", the JDK home is likely incorrect.

If IntelliJ is throwing errors like "The package 'org.onosproject.cluster' is not exported by the bundle dependencies," go to *IntelliJ IDEA*->*Preferences*. On the sidebar, under the *Editor* dropdown section, select *Inspections*. From there, search *OSGi* and under the OSGi dropdown, uncheck *Package accessibility* inspections and press *OK*.

## Importing the Copyright header

Since ONOS is licensed under Apache 2 license, we need to make sure that all source files are properly decorated with the Apache 2 license header file.

To configure IntelliJ appropriately, we will locate the *header.txt* file under ONOS *tools/dev* directory and copy its contents. Then, from IntelliJ preferences, we will select Copyright section and add a new new copyright profile. We will call this profile ONOS and paste in the previously copied header text.

Then we will make sure that the newly created ONOS copyright profile is the default and we are done.

## Next Steps

The [ONOS Screencasts](../../../tutorials/screencasts/importing-onos-projects-into-intellij-idea-old.md) page provides helpful videos on importing, debugging, and developing ONOS with IntelliJ.
