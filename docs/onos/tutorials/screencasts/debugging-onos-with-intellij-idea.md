# Debugging ONOS with IntelliJ IDEA

## .[YouTube Video](https://www.youtube.com/watch?v=UzWcI9KvP0g)

## Overview

This screencast will demonstrate how to debug ONOS and applications using the IntelliJ IDEA work-bench.

## Starting ONOS with debug option

Before debugging ONOS, we need to make sure that it has been launched with a debug option. For example, to debug ONOS run locally with `onos-karaf` command, we simply need to add the debug argument to the command line, e.g. `onos-karaf clean debug`.

Similarly, for production ONOS deployments installed from the tar.gz file, we need to add the debug parameter when starting ONOS by `bin/onos-service server debug`.

When debugging ONOS running the official docker container from DockerHub, run the container exposing the port 5005 and setting the following environment variable `JAVA_DEBUG_PORT="0.0.0.0:5005"`.   
E.g.,:

```
docker run -t -d -p 5005:5005 --env JAVA_DEBUG_PORT="0.0.0.0:5005" onosproject/onos debug
```

Installations deployed via the onos-install utility already include the debug option by default.

In our demonstration, we will use the locally run ONOS, so let’s start it.

## Attaching IntelliJ IDEA to the remote ONOS process

While ONOS is starting up, let’s switch to IntelliJ IDEA and from the *Run* menu, select *Edit Configurations…* Then, let’s add a new configuration by pressing the + sign and select the *Remote* configuration.

Since we’ll be debugging local ONOS, let’s name our configuration *Local* and let’s leave the default *Host* address as localhost. If we were debugging ONOS running on another machine we would simply specify the IP address or DNS name of that machine here.

Let’s press *OK* to apply the changes and to close the dialog. Note that the newly created debug configuration has been selected in the upper right hand corner.

Now all we need to do to attach the debugger to the ONOS process is to press the debug button. It’s the one with the bug icon. This will immediately open the Debug console with a message that IntelliJ has connected to the target virtual machine on localhost and on port 5005.

## Setting break-points

At this point, we are ready to start setting breakpoints in our code. To do that we simply need to click in the left-hand margin of the code editor. In our example, we will set some breakpoints in the *ApplicationCommand.java*, which is a CLI handler for the `onos:app` command.

Let’s open this file and let’s set a breakpoint on line 60.

## Customizing break-points

To customize a break-point we can simply right-click on it and then tailor its properties.

One useful customization is to change the break-point so that it suspends only the executing *Thread* rather than all threads in the VM. Because other threads are free to continue execution, you are less likely to disrupt normal processing paths, due to missed heart-beats or time-outs. Let’s do this for our break-point.

Another useful breakpoint functionality is the ability to break only when a certain condition is met. To turn a breakpoint into a conditional one, we just need to type a Java boolean expression into the Condition field. Let’s make our breakpoint conditional on the name of the application ending with the *“.fwd”* string.

## Logging break-points

Alternatively, we can turn a breakpoint into a logging one, which means that it will log a value of an expression, rather than suspend the program execution. Let’s try this out by setting another breakpoint on line 90 and then turn off the *Suspend* check-box. Doing that will reveal a number of logging options. We’ll chose to log our own message, which prints out a message with the value of the appId field. Note how the auto-completion works nicely here.

## Inspecting Variables

Now that we have some breakpoints, let’s invoke the onos:app command and let’s see what happens. First, let’s activate the proxy ARP application.

Note that the debug console contains the message from our logging breakpoint, but that the program execution has not been suspended.

Now, let’s activate the reactive forwarding application. Doing that will trigger our conditional breakpoint and the view will automatically switch to IntelliJ IDEA, with the active breakpoint line highlighted.

At this point, we can inspect variables and fields. Note how IntelliJ IDEA shows the values right in the editor, where the fields and variables are in use. You can find the full context in the *Variables* view of the *Debug* tool window.

## Evaluating Expressions

Note that besides viewing variables, you can also evaluate expressions. For example, we can invoke the *getApplications()* method on the object referenced by the service variable, which is currently in scope of the breakpoint.

## Changing Stack Frames

You can inspect values of fields and variables in stack frames other than the top-most one. For example, here we can switch to the fourth stack-frame to see the value of the arguments parameter. Examining the state in deeper stack-frames can be useful to understanding the broader context of the current breakpoint.

## Stepping through the code

After examining the situation, let’s say we are ready to move past this breakpoint. We can either step-over, step-in or simply continue the execution. Let’s step-into the manageApp method. To do that we can press F7 key, or click on the step-in icon.

Note how the *Variables* context was adjusted to reflect the changed scope and how the call-stack grew. Now let’s resume execution by pressing the play button or by pressing F9.

## Modifying internal state

Let’s activate the reactive forwarding application and let’s step-into the manageApp method again. Oh, I really meant to deactivate the reactive forwarding application since it has already been activated. That’s OK. We can easily remedy this by changing the value of an existing field or variable.

We’ll do that by right-clicking on the command field (or by pressing F2) and then changing value to *“deactivate”*. Stepping over the next few lines, using the F8 key, we can see that the code-path taken is one that reflects the changed value of the command field.

Now we will repeatedly step-in and step-over until we reach the *GossipApplicationStore* deactivate method.

We will evaluate the following expression to prove that our application has indeed been marked as deactivated and then we’ll resume the program execution by pressing F9.

## Conclusion

These were just a few tips on how to debug ONOS as a remote application with IntelliJ IDEA.

I hope you found this screencast useful. I encourage you to become closely familiar with your work-bench and its various shortcut keystrokes. It will make your debugging sessions far more efficient.

Have a great day… and I wish you productive debugging.
