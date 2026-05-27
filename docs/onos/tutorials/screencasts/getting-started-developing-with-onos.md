# Getting started developing with ONOS

## [YouTube Video](https://www.youtube.com/watch?v=wEMVmbsNyS4)

## Overview

In this brief screencast, we will demonstrate how to check-out the ONOS codebase and how to build it. We will also show you how to tailor your shell environment to get access to a number of shell tools, aliases and other conveniences that aim to make working with ONOS very easy.

This demonstration assumes that your development environment has the required tool chain installed already. You can find this information - and more - on the ONOS wiki under the Developer Guide section.

## Checking out the code

Let us start with checking out the ONOS code. We are opting to check-out the code directly under our home directory, but you can choose an alternate location if you wish. Once the code has been checked out, we will change our working directory to the `onos` directory.

Before we build, let’s source in the ONOS developer bash profile. While strictly not required, I would highly recommend doing this, because it will augment your environment with path configuration and with various shell aliases and shortcuts that make working with ONOS a breeze.

Modify Bash profile

Once the code has been checked out, we are ready to build it. However, before we do that, let’s modify our bash profile to import the ONOS developer bash profile. While this is not strictly required, I would highly recommend doing this, because it will augment your  environment with path configuration and with various shell aliases and shortcuts that make working with ONOS a breeze. Depending on what OS you are using for development, you should make your changes in either *.bash\_profile* or *.bash\_aliases* file. Since we are on OS/X, we will edit our *.bash\_profile* file. We will first export *ONOS\_ROOT* environment variable to point to the root of ONOS source tree and then we will source-in the ONOS developer profile.

After saving the changes, we will source-in our new profile and we are now ready to build and package ONOS.

## Building ONOS via Buck (ONOS Versions Older than 1.14)

ONOS is built with Buck, which is a build tool developed by Facebook and which supports highly parallel and incremental builds. To build ONOS, we simply need to run the `buck build onos` command as follows. Please note that presently, ONOS is built using a custom version of Buck that contains a number of enhancements that will be upstreamed to the official version over time. When building the code-base for the first time, the buck program and ONOS build plugins will be automatically downloaded and installed before starting the build.

As you can see, the buck build command will download any required third-party dependencies, compile and assemble all JAR bundles and finally produce a distributable `onos.tar.gz` file that can be used for installation.

If you are invoking Buck for the very first time, the build may take a few minutes to complete. Of course, the subsequent builds will be much faster since Buck will build only the modules that have changed or those that are affected by an upstream change. Note that unlike Maven or Make, which both use timestamps, Buck uses SHA hashes to determine whether sources have changed relative to the compiled artifacts.

## Modify Bash Profile

While we are waiting for the build to complete, let’s update our own bash profile to source the ONOS developer profile for all new shell session. Depending on what OS you are using for development, you should make your changes in either `.bash_profile` or `.bash_aliases` file.

## Executing Unit Tests

To execute ONOS tests, simply run `buck test` command. Note that this will run all unit tests, integration tests as well as Checkstyle code validation. As with the build steps, Buck will only execute tests for modules impacted by code changes upstream along the dependency graph.

## Running ONOS Locally

ONOS has been architected to run in a distributed configuration where multiple instances cooperate as a single cluster. However, there are times during the development when using a single ONOS instance is perfectly sufficient. This includes development of southbound providers, CLI, REST API and GUI among others.

Running ONOS locally is as easy as typing the following command: `buck run onos-local`

This will create a local ONOS installation in the user’s temp directory and start the ONOS server in the background, while displaying the ONOS log file in the foreground.

Once running, you can connect to the ONOS GUI by typing `onos-gui localhost` or by opening the browser directly to this URL. Note that the default credentials are user `onos` and password `rocks`.To connect to the ONOS command-line console, we can simply type `onos localhost`.

 Pressing `Ctrl-C` in the window showing the ONOS log monitor will unceremoniously stop the ONOS server as you can see by the CLI and GUI both being immediately disconnected.

## Importing ONOS Code into IDE

To import the ONOS project into IntelliJ IDEA, you can use Buck to generate the required project files via `buck project` command and after that, you can simply open the `onos` source directory from IntelliJ. Afterwards, you may need to set the project Java language level to 1.8.

 Hopefully, you have found this screencast useful. Have a great day… and happy coding!

## Building ONOS via Bazel (ONOS 1.14 or higher)

Newer versions of ONOS are build using Bazel, note that it as far as 2020 this may only work in the ubuntu desktop versions, and this is a simplified version on how to build and run ONOS using Bazel.

Use wget to get the latest version of Bazel (you can use other versions of bazel and other informations at [this](https://www.bazel.build/) link)

$ wget <https://github.com/bazelbuild/bazelisk/releases/download/v1.4.0/bazelisk-linux-amd64>

Install Bazel with the appropriate permissions

$ chmod +x bazelisk-linux-amd64  
$ sudo mv bazelisk-linux-amd64 /usr/local/bin/bazel

Check if Bazel was installed by verifying its version  
$ bazel version

Clone ONOS project using git in the home directory

$ git clone <https://gerrit.onosproject.org/onos>

Set ONOS root folder

$ export ONOS\_ROOT=~/onos

$ source $ONOS\_ROOT/tools/dev/bash\_profile

Move to ONOS main folder using ONOS\_ROOT

$ cd $ONOS\_ROOT

Use Bazel to build ONOS

$ bazel build onos

You can use bazel the test ONOS installation using the following command

$ bazel query 'tests(//...)' | xargs bazel test

Now you can Run ONOS using the following command

$ bazel run onos-local -- clean debug

ONOS should run with no problem but if you want more information you can check [this](../../guides/developer-guide/development-environment-setup/using-an-ide-with-onos-1.14-or-higher-bazel-build.md) link for more information on how to use Bazel.
