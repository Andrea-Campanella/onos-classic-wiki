# Optical Information Model

WIP

Work in progress

# ONOS Topology Information model

[![](https://docs.google.com/drawings/d/1A00RfI3S3BUQD8Dlr-4ywtU0OAyADEme7_cff4QFt6w/pub?w=960&h=720)](https://docs.google.com/drawings/d/1A00RfI3S3BUQD8Dlr-4ywtU0OAyADEme7_cff4QFt6w/edit?usp=sharing)

Topology information model elements, relevant to transport network, consist of Device, Port, and Link.

* Device represents network infrastructure devices, such as (Packet) switch, ROADM, etc.
* Port represents a port on a Device.
* Link represents the connectivity between two Port objects.

Each elements has fixed basic attributes common across variant of its kind. (e.g., Port's portspeed)    
Additional information about elements can also be added as String-String annotations by each Provider.    
This mechanism should be used to add relatively read-heavy information specific to certain technology or domain.

## Two representations of Port

There are two representations of an optical Port.

* Storage format (DefaultPort),   
  which is a format ONOS distributed core, etc. will deal with for state distribution etc.
* Application friendly format (e.g., OchPort),   
  which is an instance generated on the fly, by translating additional attributes stored as Annotations on storage format port.

In order to retrieve Port in application friendly format, the Device to which the port is attached, must be equipped with *OpticalDevice* behaviour.

**optical-driver.xml**

```
    <driver name="linc-oe" extends="default"
            manufacturer="FlowForwarding.org" hwVersion="Unknown"
            swVersion="LINC(-OE)? OpenFlow Software Switch 1.1">
        <behaviour api="org.onosproject.openflow.controller.driver.OpenFlowSwitchDriver"
                   impl="org.onosproject.driver.optical.handshaker.OfOpticalSwitchImplLinc13"/>
        <behaviour api="org.onosproject.net.behaviour.LambdaQuery"
                   impl="org.onosproject.driver.optical.query.LincOELambdaQuery"/>
        <behaviour api="org.onosproject.net.optical.OpticalDevice"
                   impl="org.onosproject.net.optical.DefaultOpticalDevice"/>
    </driver>
```

When a Device implements *OpticalDevice* Behaviour, you can decorate the *DeviceService* by *OpticalDeviceServiceView#opticalView(DeviceService)*

so that *Port* returned through the decorated *DeviceService* API will return *Port*s in application friendly format. (e.g., *OchPort*, etc.)

See following excerpt from *OpticalPortsListCommand.java* as an usage example.

At the beginning *DeviceService* is decorated

DeviceService service = opticalView(get(DeviceService.class));

and the *Port*s returned by decorated service is now an instance of application friendly format.

**Example: excerpt from OpticalPortListCommand.java** Expand source

```
import static org.onosproject.net.optical.device.OpticalDeviceServiceView.opticalView;
...
 
        DeviceService service = opticalView(get(DeviceService.class));
 
        List<Port> ports = new ArrayList<>(service.getPorts(device.id()));

        for (Port port : ports) {
            if (!isIncluded(port)) {
                continue;
            }

            String portName = port.number().toString();
            String portIsEnabled = port.isEnabled() ? "enabled" : "disabled";
            String portType = port.type().toString().toLowerCase();

            switch (port.type()) {
                case OCH:
                    if (port instanceof OchPort) {
                        OchPort och = (OchPort) port;
                        print(FMT_OCH, portName, portIsEnabled, portType,
                              och.signalType().toString(),
                              och.isTunable() ? "yes" : "no",
                              annotations(och.unhandledAnnotations()));
                       break;
                    }

                    print("WARN: OchPort but not on OpticalDevice or ill-formed");
                    print(FMT, portName, portIsEnabled, portType, port.portSpeed(), annotations(port.annotations()));
                    break;

                case ODUCLT:
                    if (port instanceof OduCltPort) {
                        OduCltPort oduCltPort = (OduCltPort) port;
                        print(FMT_ODUCLT_OTU, portName, portIsEnabled, portType,
                              oduCltPort.signalType().toString(),
                              annotations(oduCltPort.unhandledAnnotations()));
                        break;
                    }

                    print("WARN: OduCltPort but not on OpticalDevice or ill-formed");
                    print(FMT, portName, portIsEnabled, portType, port.portSpeed(), annotations(port.annotations()));
                    break;

                case OMS:
                    if (port instanceof OmsPort) {
                        OmsPort oms = (OmsPort) port;
                        print(FMT_OMS, portName, portIsEnabled, portType,
                              oms.minFrequency().asHz() / Frequency.ofGHz(1).asHz(),
                              oms.maxFrequency().asHz() / Frequency.ofGHz(1).asHz(),
                              oms.grid().asHz() / Frequency.ofGHz(1).asHz(),
                              oms.totalChannels(),
                              annotations(oms.unhandledAnnotations()));
                        break;
                    }

                    print("WARN: OmsPort but not on OpticalDevice or ill-formed");
                    print(FMT, portName, portIsEnabled, portType, port.portSpeed(), annotations(port.annotations()));
                    break;

                case OTU:

                    if (port instanceof OtuPort) {

                        OtuPort otuPort = (OtuPort) port;
                        print(FMT_ODUCLT_OTU, portName, portIsEnabled, portType,
                              otuPort.signalType().toString(),
                              annotations(otuPort.unhandledAnnotations()));
                        break;
                    }

                    print("WARN: OtuPort but not on OpticalDevice or ill-formed");
                    print(FMT, portName, portIsEnabled, portType, port.portSpeed(), annotations(port.annotations()));
                    break;

                default:
                    // do not print non-optical ports
                    break;
            }
        }
```

# Packet-Optical multi-layer Intent representation

Packet-Optical multi-layer path setup via Intents are expressed in a model like below.

[![](https://docs.google.com/drawings/d/1naKcd7oZTkOor5nH_oTO99MyfmZN0OzuusIRGGvpyNw/pub?w=960&h=720)](https://docs.google.com/drawings/d/1naKcd7oZTkOor5nH_oTO99MyfmZN0OzuusIRGGvpyNw/edit?usp=sharing)

Blue circular Device is the packet-layer device and red octagon Device represent optical Devices.

Initially, packet-layer Link, represented by solid blue lines, between packet-layer Device does not exist in the ONOS topology.    
Once Optical Intent is installed, packet-layer connectivity will be established between s5-s6, which will show up as a link between packet-layer side of cross-connect links.

See [Optical Intents](optical-intents.md) and [Optical Path Provisioner](optical-path-provisioner.md) for more details.

# Optical Device/Port Information Model

Optical Device and it's ports are modelled as Device object with additional attributes carrying optical specific characteristics.

* OduCLt port

+ Representation of ODU client port (Optical channel Data Unit).

* Och port

+ Representation of OCh port (Optical Channel)

* OMS port

  + Representation of OMS port (Optical Multiplexing Section)
* OTU port

  + Representation OTU port (Optical channel Transport Unit)

# Example representation of optical devices in Optical Information model

## Vertically Integrated ROADM model

Following is vertically integrated ROADM used in the Packet-Optical demo at ONS2015, represented using ONOS optical information model.

[![](https://docs.google.com/drawings/d/1aUor0nKVdYO0W5ikpXNESWW4yOFpsyCiY0Y80I6H1aA/pub?w=944&h=491)](https://docs.google.com/drawings/d/1aUor0nKVdYO0W5ikpXNESWW4yOFpsyCiY0Y80I6H1aA/edit?usp=sharing)

## Disaggregated ROADM model

Following is disaggregated ROADM used in the E-CORD/OpenROADM demo at ONS2016/OFC2016,   
represented using ONOS optical information model.

[![](https://docs.google.com/drawings/d/10Pu0baNeqT3DVL35nLtwB-bkVe_RNwdmyQtNS48PiYw/pub?w=941&h=570)](https://docs.google.com/drawings/d/10Pu0baNeqT3DVL35nLtwB-bkVe_RNwdmyQtNS48PiYw/edit?usp=sharing)
