# Sample PortStatistics Application tutorial based on template application tutorial

When a new developer set-out to write a SDN app in ODL, the learning curve is way too steep. Even though ONOS also follows [maven archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html) , ONOS developers had made things simpler by providing a wrapper called onos-create-app.

I will let you glean-through the [Template Application Tutorial](../template-application-tutorial.md) to setup the skeleton app. Once you are done, continue reading through.

#### Scope of our application

Let us now create a simple application to get the Port Statistics of all the ports from all the devices ( possibly openflow devices ) that are attached to the controller.

So what exactly we mean about port statistics?? Well, it is basically the amount of packet, bytes that are sent to / recieved from a given port from a given device.

ONOS also maintain another special version of statistics known as Port Delta Statistics which actually provides the delta between 2 given probe intervals.

#### How to get our data from controller ?

ONOS exposes different services to poke into and get data. One such service is DeviceService. This particular service abstracts the south bound device irrespective of the south bound interface that is connected with.

So let us use this service to get the list of devices first. But before that, we need to get a reference of the interface class.

**Listing 1**

```
@Reference(cardinality = ReferenceCardinality.MANDATORY_UNARY)
 protected DeviceService deviceService;
 
  Iterable<Device> devices = deviceService.getDevices();
  List<PortStatistics> portStatisticsList = deviceService.getPortDeltaStatistics(d.id());
                for (PortDeltaStatistics portdeltastat : portStatisticsList) {
                	 if(portdeltastat != null)
                    		log.info("portdeltastat bytes recieved" + portdeltastat.bytesReceived());
                	else
                    		log.info("Unable to read portDeltaStats");
                }
```

While this rudimentary, why not let us monitor every port of every device in autonomous way? Sounds good right??

All we need now is a worker for us to work in independant fashion. Well the solution is `TimerTask`. So let us create a new class `portStatsReaderTask` extending `TimerTask` and fire an independant task operation as follows.

But before that, let us look how our `portStatsReaderTask` might look.

**Listing 2**

```
public class portStatsReaderTask {

    class Task extends TimerTask {

        public Device getDevice() {
            return device;
        }
        public DeviceService getDeviceService() {
            return deviceService;
        }
        public long getDelay() {
            return delay;
        }

        @Override
        public void run() {
            while (!isExit()) {
                log.info("####### Into run() ");
                List<PortStatistics> portStatisticsList = getDeviceService().getPortDeltaStatistics(getDevice().id());
                for (PortStatistics portStats : portStatisticsList) {
                    log.info("########## port is " + portStats.port());
                    if (portStats.port() == getPort()) {
                        log.info("Port " + port + "has recieved " + portStats.bytesReceived() + "bytes");
                        try {
                            Thread.sleep((getDelay() * 1000));
                            break;
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }
        }
    }

    public void schedule() {
        this.getTimer().schedule(new Task(), 0, 1000);
    }
--snip--
```

Hope you get the implementation. `portStatsReaderTask` contains an *inner class* named `Task`that extends `TimerTask`. This is necessary if we want to use `portStatsReaderTask` as a self contained component ( you will get more clarity in the place where we really use this class ).

The `run()` & `schedule()` are really the heart & nerve of this whole logic. For the sake of this blog, I didn’t make the full source available. I shall provide a link to github source at the end of this post.

Having defined our worker, let us give some work to the worker.

## `activate()` & `deactivate` function :

The `AppComponent` class provides `activate()` & `deactivate()` functions which marks the start & end of every ONOS app’s lifecycle. So we are going to place our logic in `activate()` function.

**Listing 3**

```
@Activate
    protected void activate() {

        log.info("Started");
        Iterable<Device> devices = deviceService.getDevices();
        
        List<PortStatistics> portStatisticsList = deviceService.getPortDeltaStatistics(d.id());
                for (PortStatistics portStats : portStatisticsList) {
                    try {
                        int port = portStats.port();
                        log.info("#### Creating object for " + port);
                        portStatsReaderTask task = new portStatsReaderTask();
                        task.setDelay(3);
                        task.setExit(false);
                        task.setLog(log);
                        task.setPort(port);
                        task.setDeviceService(deviceService);
                        task.setDevice(d);
                        map.put(port, task);
                        task.schedule();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
      }
```

First every device, we get `List<PortStatistics>` objects. And for every element in list, we prepare a map of `PortStatistics` with `port number` and spawn a new `portStatsReaderTask`for every element in list. Now you can understand the reason for create a wrapper as explained above.

Note:

```
As per ONOS's openflow driver (provider/of/device/impl/OpenFlowDeviceProvider.java), the polling frequency is set to 5 seconds.

Hence you might need to understand that the B/W measurement depends on this 5 seconds polling intervals.
```

```
If incase you are trying to match the B/W data with external observer data ( like iperf for example ),
```

```
you might need to fix the probing interval of that observer as well to 5 seconds.
```

#### Just before saying Cya…

I hope this post would have provided you enough inputs on getting started with your ONOS app development. The idea is to provide a complete walk-through of a simple app and I hope I did justice to that intent. Feel free to fire in any questions / comments / clarifications and I would be happy to help.

Cya!!!

Source : <http://kspviswa.github.io/creating-an-app-ONOS.html>
