# TestON Drivers

# Component Drivers

Component drivers connect and provide interfaces to various components in the OpenFlow/SDN topology.

The three main methods of a component driver are connect, disconnect, and execute. While writing a custom driver, overriding an existing component method may be used in favor of writing a new method that contains similar logic.

The [Mininet driver](https://github.com/opennetworkinglab/ONLabTest/blob/master/TestON/drivers/common/cli/emulator/mininetclidriver.py) may be used as a reference to writing a custom driver.

In this example, the Mininet driver inherits from the abstract Emulator driver which inherits from the CLI driver. The Mininet driver reuses the execute and disconnect API from the CLI driver. The connect API is the only API that is redefined.

```
class MininetCliDriver( Emulator ):

        def __init__( self ):
            super( MininetCliDriver, self ).__init__()
            self.handle = self

        def connect( self, user_name, ip_address, pwd, options ):
            self.handle = super( MininetCliDriver, self ).connect( user_name, ip_address, pwd )
```

Here the connect will call the inherited connect() method from CLI driver (via Emulator class).

Driver specific methods/functions can be specified using the simple execute command in [mininetclidriver](https://github.com/opennetworkinglab/ONLabTest/blob/master/TestON/drivers/common/cli/emulator/mininetclidriver.py).

```
 def pingall( self, timeout=300 ):
        """
           Verifies the reachability of the hosts using pingall command.
           Optional parameter timeout allows you to specify how long to
           wait for pingall to complete
           Returns:
           main.TRUE if pingall completes with no pings dropped
           otherwise main.FALSE"""
        if self.handle:
            main.log.info(
                self.name +
                ": Checking reachabilty to the hosts using pingall" )
            try:
                response = self.execute(
                    cmd="pingall",
                    prompt="mininet>",
                    timeout=int( timeout ) )
```

# 

# Cluster Driver

The cluster driver combines the CLI, REST, and Bench components as a cluster.  This allows the use of a function or variable from another driver without the need to specify that specific driver.  For example,

```
main.Cluster.active( 0 ).devices()
```

can be used instead of

```
main.ONOScli1.devices()
```

and keeps the same context as the former. This can be helpful in tests where the number of ONOS nodes is not static throughout the test.

However, if the function name is similar across more than one driver, the driver name will need to be specified.  For example, in

```
main.Cluster.active( 0 ).CLI.sendline( "roles" )
```

"CLI" must be specified to avoid ambiguity.

# Creating A Driver

* Create .py file under "/drivers/common/cli/.." . In this example, the driver is placed under cli > emulator(folderpath) hierarchy. If the user wishes to create a driver that is integrated with an API library, then the same can be created under api-emulator (folder path). The driver should be placed in the same folder as the inherited driver.
* The class name must be the same as the driver name. Naming convention for the module name is lower case letters. Naming convention for the class name is CamelCase. In the test .topo file specify the component driver as 'type' = 'DriverName'.
* Create a function in the new driver class "connect" with a suitable return type. It will facilitate the connection for component or remote host used for driver.
* Create more functions/api in DriverName class with suitable defined parameters.

**NOTE:** More documentation for writing drivers will be added in the future.

## Stuck? Found a bug? Questions?

Email [us](mailto:onos-test@googlegroups.com) if you’re stuck, think you’ve found a bug, or just want to send some feedback. Please have a look at the [guidelines](https://wiki.onosproject.org/display/ONOS/ONOS+Mailing+Lists) to learn how to efficiently submit a bug report.
