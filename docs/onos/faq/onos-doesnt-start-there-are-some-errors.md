# ONOS doesn't start there are some errors

root@[Host-001:/home/onos/onos-2.2.0/bin#](http://Host-001/home/onos/onos-2.2.0/bin) ./onos-service  
karaf: JAVA\_HOME not set; results may vary  
Jan 03, 2020 3:45:08 AM org.apache.karaf.main.lock.SimpleFileLock lock  
INFO: Trying to lock /home/onos/onos-2.2.0/apache-karaf-4.2.6/lock  
Jan 03, 2020 3:45:08 AM org.apache.karaf.main.lock.SimpleFileLock lock  
INFO: Lock acquired  
Jan 03, 2020 3:45:08 AM org.apache.karaf.main.Main$KarafLockCallback lockAcquired  
INFO: Lock acquired. Setting startlevel to 100  
2020-01-03 03:45:12,510 CM Configuration Updater (ManagedService Update: pid=[org.ops4j.pax.logging]) ERROR Unable to locate appender "AuditFile" for logger config "root"  
03:45:14.242 INFO [JettyFactoryImpl] No ALPN class available  
03:45:14.233 INFO [Activator] Deployment finished. Registering FeatureDeploymentListener  
03:45:14.281 INFO [JettyFactoryImpl] HTTP/2 not available, creating standard ServerConnector for Http  
03:45:14.548 INFO [JettyServerImpl] Pax Web available at [0.0.0.0]:[8181]  
03:45:15.943 INFO [FeaturesServiceImpl] The specified feature: 'service' version '4.2.6' is already installed  
03:45:15.949 INFO [FeaturesServiceImpl] The specified feature: 'framework' version '4.2.6' is already installed  
03:45:15.954 INFO [FeaturesServiceImpl] The specified feature: 'jaas' version '4.2.6' is already installed  
03:45:15.961 INFO [FeaturesServiceImpl] The specified feature: 'package' version '4.2.6' is already installed  
03:45:15.963 INFO [FeaturesServiceImpl] The specified feature: 'webconsole' version '4.2.6' is already installed  
03:45:15.970 INFO [FeaturesServiceImpl] The specified feature: 'feature' version '4.2.6' is already installed  
03:45:15.974 INFO [FeaturesServiceImpl] The specified feature: 'config' version '4.2.6' is already installed  
03:45:15.976 INFO [FeaturesServiceImpl] The specified feature: 'deployer' version '4.2.6' is already installed  
03:45:15.979 INFO [FeaturesServiceImpl] The specified feature: 'diagnostic' version '4.2.6' is already installed  
03:45:15.986 INFO [FeaturesServiceImpl] The specified feature: 'scr' version '4.2.6' is already installed  
03:45:15.990 INFO [FeaturesServiceImpl] The specified feature: 'shell' version '4.2.6' is already installed  
03:45:15.992 INFO [FeaturesServiceImpl] The specified feature: 'management' version '4.2.6' is already installed  
03:45:16.004 INFO [FeaturesServiceImpl] The specified feature: 'kar' version '4.2.6' is already installed  
03:45:16.007 INFO [FeaturesServiceImpl] The specified feature: 'log' version '4.2.6' is already installed  
03:45:16.009 INFO [FeaturesServiceImpl] The specified feature: 'war' version '4.2.6' is already installed  
03:45:16.011 INFO [FeaturesServiceImpl] The specified feature: 'ssh' version '4.2.6' is already installed  
03:45:16.014 INFO [FeaturesServiceImpl] The specified feature: 'eventadmin' version '4.2.6' is already installed  
03:45:16.021 INFO [FeaturesServiceImpl] The specified feature: 'system' version '4.2.6' is already installed  
03:45:16.024 INFO [FeaturesServiceImpl] The specified feature: 'instance' version '4.2.6' is already installed  
03:45:16.025 INFO [FeaturesServiceImpl] The specified feature: 'wrap' version '2.6.1' is already installed  
03:45:16.028 INFO [FeaturesServiceImpl] The specified feature: 'bundle' version '4.2.6' is already installed  
03:45:16.040 INFO [FeaturesServiceImpl] Adding features: service/[4.2.6,4.2.6],framework/[4.2.6,4.2.6],jaas/[4.2.6,4.2.6],package/[4.2.6,4.2.6],webconsole/[4.2.6,4.2.6],feature/[4.2.6,4.2.6],config/[4.2.6,4.2.6],deployer/[4.2.6,4.2.6],diagnostic/[4.2.6,4.2.6],scr/[4.2.6,4.2.6],shell/[4.2.6,4.2.6],management/[4.2.6,4.2.6],kar/[4.2.6,4.2.6],log/[4.2.6,4.2.6],war/[4.2.6,4.2.6],ssh/[4.2.6,4.2.6],eventadmin/[4.2.6,4.2.6],system/[4.2.6,4.2.6],instance/[4.2.6,4.2.6],wrap/[2.6.1,2.6.1],bundle/[4.2.6,4.2.6]  
03:45:19.185 INFO [FeaturesServiceImpl] No deployment change.  
03:45:19.262 INFO [FeaturesServiceImpl] Starting bundles:  
03:45:19.308 INFO [FeaturesServiceImpl] org.ops4j.pax.web.pax-web-deployer/7.2.10  
03:45:19.363 INFO [FeaturesServiceImpl] org.apache.karaf.log.core/4.2.6  
03:45:19.446 INFO [CommandExtension] Registering commands for bundle org.apache.karaf.log.core/4.2.6  
03:45:19.456 INFO [FeaturesServiceImpl] org.apache.karaf.config.core/4.2.6  
03:45:19.626 INFO [CommandExtension] Registering commands for bundle org.apache.karaf.config.core/4.2.6  
03:45:19.932 INFO [FeaturesServiceImpl] org.apache.aries.jmx.api/1.1.5  
03:45:19.945 INFO [FeaturesServiceImpl] org.apache.karaf.webconsole.console/4.2.6  
03:45:20.331 INFO [HttpServiceFactoryImpl] Binding bundle: [org.apache.karaf.webconsole.console [54]] to http service  
03:45:20.468 INFO [ServletContainerInitializerScanner] will add org.apache.jasper.servlet.JasperInitializer to ServletContainerInitializers  
03:45:20.475 INFO [ServletContainerInitializerScanner] Skipt org.apache.jasper.servlet.JasperInitializer, because specialized handler will be present  
03:45:20.479 INFO [ServletContainerInitializerScanner] will add org.eclipse.jetty.websocket.jsr356.server.deploy.WebSocketServerContainerInitializer to ServletContainerInitializers  
03:45:21.891 INFO [ServletContainerInitializerScanner] added ServletContainerInitializer: org.eclipse.jetty.websocket.jsr356.server.deploy.WebSocketServerContainerInitializer  
03:45:21.902 INFO [ServletContainerInitializerScanner] will add org.eclipse.jetty.websocket.server.NativeWebSocketServletContainerInitializer to ServletContainerInitializers  
03:45:21.905 INFO [ServletContainerInitializerScanner] added ServletContainerInitializer: org.eclipse.jetty.websocket.server.NativeWebSocketServletContainerInitializer  
03:45:22.050 INFO [HttpServiceContext] registering context DefaultHttpContext [bundle=org.apache.karaf.webconsole.console [54], contextID=custom], with context-name:  
03:45:22.112 INFO [HttpServiceContext] registering JasperInitializer  
03:45:22.185 INFO [WebSocketServerFactory] No DecoratedObjectFactory provided, using new org.eclipse.jetty.util.DecoratedObjectFactory[decorators=1]  
03:45:22.495 INFO [session] DefaultSessionIdManager workerName=node0  
03:45:22.497 INFO [session] No SessionScavenger set, using defaults  
03:45:22.501 INFO [session] node0 Scavenging every 600000ms  
03:45:22.589 INFO [ContextHandler] Started HttpServiceContext{httpContext=DefaultHttpContext [bundle=org.apache.karaf.webconsole.console [54], contextID=custom]}  
03:45:22.604 INFO [Server] jetty-9.4.18.v20190429; built: 2019-04-29T20:42:08.989Z; git: e1bc35120a6617ee3df052294e433f3a25ce7097; jvm 1.8.0\_232-8u232-b09-0ubuntu1~16.04.1-b09  
03:45:22.948 INFO [AbstractConnector] Started default@f8ea82c{HTTP/1.1,[http/1.1]}{0.0.0.0:8181}  
03:45:22.955 INFO [Server] Started @18933ms  
03:45:22.974 INFO [FeaturesServiceImpl] org.apache.felix.webconsole.plugins.memoryusage/1.0.10  
03:45:22.980 INFO [HttpServiceFactoryImpl] Unbinding bundle: [org.apache.karaf.webconsole.console [54]]  
03:45:22.998 INFO [memoryusage] Storing Memory Dumps in /home/onos/onos-2.2.0/apache-karaf-4.2.6/data/cache/bundle26/data/dumps  
03:45:23.000 INFO [ContextHandler] Stopped HttpServiceContext{httpContext=DefaultHttpContext [bundle=org.apache.karaf.webconsole.console [54], contextID=custom]}  
03:45:23.008 INFO [HttpServiceFactoryImpl] Binding bundle: [org.apache.karaf.webconsole.console [54]] to http service  
03:45:23.011 INFO [memoryusage] Setting Automatic Memory Dump Threshold to 0% for pools [Code Cache, Compressed Class Space, G1 Old Gen, Metaspace]  
03:45:23.025 INFO [memoryusage] Automatic Memory Dump cannot be set for pools [G1 Eden Space, G1 Survivor Space]  
03:45:23.027 INFO [memoryusage] Setting Automatic Memory Dump Interval to 21600 seconds  
03:45:23.056 INFO [ServletContainerInitializerScanner] will add org.apache.jasper.servlet.JasperInitializer to ServletContainerInitializers  
03:45:23.059 INFO [ServletContainerInitializerScanner] Skipt org.apache.jasper.servlet.JasperInitializer, because specialized handler will be present  
03:45:23.061 INFO [FeaturesServiceImpl] org.ops4j.pax.web.pax-web-descriptor/7.2.10  
03:45:23.066 INFO [ServletContainerInitializerScanner] will add org.eclipse.jetty.websocket.jsr356.server.deploy.WebSocketServerContainerInitializer to ServletContainerInitializers  
03:45:23.081 INFO [FeaturesServiceImpl] org.apache.karaf.http.core/4.2.6  
03:45:23.125 INFO [HttpServiceFactoryImpl] Binding bundle: [org.apache.karaf.http.core [37]] to http service  
03:45:23.198 INFO [CommandExtension] Registering commands for bundle org.apache.karaf.http.core/4.2.6  
03:45:23.211 INFO [FeaturesServiceImpl] org.apache.karaf.system.core/4.2.6  
03:45:23.285 INFO [CommandExtension] Registering commands for bundle org.apache.karaf.system.core/4.2.6  
03:45:23.298 INFO [FeaturesServiceImpl] org.apache.karaf.features.command/4.2.6  
03:45:23.388 INFO [CommandExtension] Registering commands for bundle org.apache.karaf.features.command/4.2.6  
03:45:23.441 INFO [FeaturesServiceImpl] org.apache.karaf.instance.core/4.2.6  
03:45:23.917 INFO [CommandExtension] Registering commands for bundle org.apache.karaf.instance.core/4.2.6  
03:45:23.927 INFO [FeaturesServiceImpl] org.apache.karaf.webconsole.gogo/4.2.6  
03:45:23.957 INFO [GogoPlugin] Gogo plugin activated  
03:45:23.969 INFO [FeaturesServiceImpl] org.apache.karaf.diagnostic.core/4.2.6  
03:45:24.015 INFO [CommandExtension] Registering commands for bundle org.apache.karaf.diagnostic.core/4.2.6  
03:45:24.019 INFO [FeaturesServiceImpl] org.apache.karaf.jaas.config/4.2.6  
03:45:24.105 INFO [FeaturesServiceImpl] org.apache.karaf.management.server/4.2.6  
03:45:24.135 INFO [ServletContainerInitializerScanner] added ServletContainerInitializer: org.eclipse.jetty.websocket.jsr356.server.deploy.WebSocketServerContainerInitializer  
03:45:24.138 INFO [ServletContainerInitializerScanner] will add org.eclipse.jetty.websocket.server.NativeWebSocketServletContainerInitializer to ServletContainerInitializers  
03:45:24.146 INFO [ServletContainerInitializerScanner] added ServletContainerInitializer: org.eclipse.jetty.websocket.server.NativeWebSocketServletContainerInitializer  
03:45:24.148 INFO [HttpServiceContext] registering context DefaultHttpContext [bundle=org.apache.karaf.webconsole.console [54], contextID=custom], with context-name:  
03:45:24.150 INFO [HttpServiceContext] registering JasperInitializer  
03:45:24.153 INFO [WebSocketServerFactory] No DecoratedObjectFactory provided, using new org.eclipse.jetty.util.DecoratedObjectFactory[decorators=1]  
03:45:24.199 INFO [ContextHandler] Started HttpServiceContext{httpContext=DefaultHttpContext [bundle=org.apache.karaf.webconsole.console [54], contextID=custom]}  
03:45:24.200 INFO [FeaturesServiceImpl] org.apache.karaf.scr.management/4.2.6  
03:45:24.226 INFO [memoryusage] Setting Automatic Memory Dump Threshold to 0% for pools [Code Cache, Compressed Class Space, G1 Old Gen, Metaspace]  
03:45:24.228 INFO [memoryusage] Automatic Memory Dump cannot be set for pools [G1 Eden Space, G1 Survivor Space]  
03:45:24.240 INFO [memoryusage] Setting Automatic Memory Dump Interval to 21600 seconds  
03:45:24.249 INFO [memoryusage] Storing Memory Dumps in /home/onos/onos-2.2.0/apache-karaf-4.2.6/data/cache/bundle26/data/dumps  
03:45:24.261 INFO [FeaturesServiceImpl] org.apache.karaf.jaas.modules/4.2.6  
03:45:24.348 INFO [FeaturesServiceImpl] org.apache.karaf.webconsole.instance/4.2.6  
03:45:24.383 INFO [InstancePlugin] Instance plugin activated  
03:45:24.401 INFO [CommandExtension] Registering commands for bundle org.apache.karaf.webconsole.instance/4.2.6  
03:45:24.411 INFO [FeaturesServiceImpl] org.ops4j.pax.url.war/2.6.1  
03:45:24.474 INFO [FeaturesServiceImpl] org.apache.felix.inventory/1.0.4  
03:45:24.606 INFO [ServiceComponentRuntimeMBeanImpl] Activating the Apache Karaf ServiceComponentRuntime MBean  
03:45:24.770 INFO [FeaturesServiceImpl] org.apache.felix.webconsole.plugins.ds/2.1.0  
03:45:24.853 INFO [FeaturesServiceImpl] org.apache.felix.webconsole.plugins.event/1.1.8  
03:45:24.895 INFO [ServiceComponentRuntimeMBeanImpl] Deactivating the Apache Karaf ServiceComponentRuntime MBean  
03:45:24.921 INFO [FeaturesServiceImpl] org.apache.sshd.core/1.7.0  
03:45:24.931 INFO [FeaturesServiceImpl] org.apache.karaf.web.core/4.2.6  
03:45:25.022 INFO [CommandExtension] Command registration delayed for bundle org.apache.karaf.web.core/4.2.6. Missing dependencies: [org.apache.karaf.web.WebContainerService]
