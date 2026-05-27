# PCEP Protocol

### Team

| **Name** | **Organization** | **Email** |
| --- | --- | --- |
| Patrick Liu | Huawei Technologies | [Partick.Liu@huawei.com](mailto:Partick.Liu@huawei.com) |
| Suresh B R | Huawei Technologies | [Suresh.B.R@huawei.com](mailto:Suresh.B.R@huawei.com) |
| Mahesh Poojary | Huawei Technologies | [mahesh.poojary@huawei.com](mailto:mahesh.poojary@huawei.com) |
| Phaneendra Manda | Huawei Technologies | [phaneendra.manda@huawei.com](mailto:phaneendra.manda@huawei.com) |
| Bharat Saraswal | Huawei Technologies | [bharat.saraswal@huawei.com](mailto:bharat.saraswal@huawei.com) |
| Priyanka B | Huawei Technologies | [priyanka.b@huawei.com](mailto:priyanka.b@huawei.com) |
| Rajakumar Gootla | Huawei Technologies | [rajakumarg@huawei.com](mailto:priyanka.b@huawei.com) |

### Overview

This project adds Path Computation Element Protocol (PCEP) as a southbound plugin in ONOS.

### Proposed work

Add PCEP South Bound Interface (SBI) for MPLS TE tunnel management which will implement TunnelProvider API to support initiating, updating and releasing of PCE initiated tunnels using PCE communication protocol. The implementation will also support learning of existing active tunnels which are on the network.

Implement PCEP protocol handler, which acts as a server to listen on PCEP port 4189 to establish and manage session with PCCs. A channel handler will be created for each PCEP session to maintain the state machine and state of each PCC.

Implement PCEP message handler, which will encode and decode PCEP messages between ONOS PCEP SBI and PCC. Currently the messages supported are Open, KeepAlive, PCInitiate, PCUpd, PCRpt, PCLabelUpd, LSRpt, PCLRResv, PCErr and Close.

Implementation supports state synchronization with PCC reporting reporting LSPs’ state to PCEP protocol handler running on ONOS immediately after session established. These report messages are notified to PCEP Tunnel Provider via message listener which in turn will inform the ONOS Core about the existing tunnels in the network. The Report message can also be the result of PCE initiated messages for creating, updating or releasing tunnels. In this case PCEP Tunnel Provider will invoke the respective API to notify ONOS Core about the result of create or update or release tunnels. All communication between PCEP provider and ONOS Core uses Provider Service interface.

### Pcep Tunnel Provider API

The below API are implemented for tunnel provider in PCEP SBI

#### SetupTunnel API

Arguments: Tunnel, Path

Return Value: None

Details: This API is responsible for setting up a tunnel on the device. It gets the tunnel parameters from the input parameters Tunnel and Path. The API implementation builds the PCInitiate protocol message from the input parameters. The ingress and egress are taken from src and dst members of Tunnel class. The ingress is considered as source for the tunnel and PCInitiate message is sent to ingress device for which a session is already established with the PCEP protocol handler. The explicit route object is built from the link parameter in the input Path class. The API implementation will take care of generating unique ID for sending the message to PCC and mapping the response from PCC. Finally the response is given to ONOS core using PCEP tunnel provider service.

#### UpdateTunnel API

Arguments: Tunnel, Path

Return Value: None

Details: This API is responsible for modifying an existing tunnel on the device. It gets the tunnel parameters from the input parameters Tunnel and Path. The API implementation builds the PCUpd protocol message from the input parameters. To send a PCUpd message the ingress device should have a tunnel which is already created and the PCE must be the owner of this tunnel. The ingress and egress for the tunnel are taken from src and dst of Tunnel class. The ingress is considered as source for the tunnel and PCUpd message is sent to ingress device for which a session is already established with the PCEP protocol handler. The explicit route object is built from link parameter in the Path class. The API implementation will take care of generating unique ID for sending the message to PCC and mapping the response from PCC. Finally the response is given to ONOS core using PCEP tunnel provider service.

#### ReleaseTunnel API

Arguments: Tunnel

Return Value: None

Details: This API is responsible for deleting an existing tunnel on the device. It gets the tunnel parameters from the input parameter Tunnel. The API implementation builds the PCInitiate protocol message from the input parameters. To send a PCInitiate message with delete flag set, the ingress device should have a tunnel which is already created and the PCE must be the owner of this tunnel. The tunnel id, ingress and egress for the tunnel are taken from tunnel id, src and dst of Tunnel class. The ingress is considered as source for the tunnel and PCInitiate message is sent to ingress device for which a session is already established with the PCEP protocol handler. The API implementation will take care of generating unique ID for sending the message to PCC and mapping the response from PCC. Finally the response is given to ONOS core using PCEP tunnel provider service.

### Messages Supported

#### Open Message

    Open message is used to establish a PCEP session between PCEP peers.  This carries various session characteristics like keep alive time, dead time and capability.

##### Supported TLVs

        Gmpls-capability TLV

        Stateful-Pce-capability TLV

        Pcecc capability TLV

#### KeepAlive Message

    Keep alive message used to keep the session active and also in response to open messages while session establishment to acknowledge Open messages and session characteristics are acceptable.

##### Supported TLVs

        Not Applicable

#### PCInitiate Message

    Setup Tunnel API will build the PCInitiate message to setup a tunnel at the PCC. The objects supported in PCInitiate message are

##### SRP Object

        The SRP (Stateful PCE request parameters) object set the unique identifier for mapping   request/response between PCEP and PCC.

###### Supported TLV’s

            Symbolic path name TLV

##### LSP Object

        The LSP contains a set of fields used to specify the target LSP, the operation to be performed on the LSP and LSP delegation. It also contains a flag indicating to a PCE that the LSP state synchronization in progress.

###### Supported TLVs

            LSP identifiers TLV (IPV4)

            Symbolic path name TLV

            LSP Error code TLV

            RSVP Error Spec TLV

##### END POINTS Object

        The END POINTS object used to specify the source and destination IP addresses of the tunnel.

###### Supported TLVs

           None.

##### ERO Object

        Explicit route objects contain list of variable length SubObjects.

###### Supported SubObjects

          IPv4 Prefix

          IPv6 Prefix

          Autonomous System number

          SR-ERO SubObject

          Path Key SubObject

##### BANDWIDTH Object

        This object used to specify the requested bandwidth for a TE LSP.

#### PCUpd Message

    Update Tunnel API will build the PCUpd message to update a tunnel at the PCC. The objects supported in PCUpd message are

##### SRP Object

        The SRP (Stateful PCE request parameters) object set the unique identifier for mapping request/response between PCEP and PCC.

###### Supported TLVs

          Symbolic path name TLV

##### LSP Object

        The LSP contains a set of fields used to specify the target LSP, the operation to be performed on the LSP and LSP delegation. It also contains a flag indicating to a PCE that the LSP state synchronization in progress.

###### Supported TLVs

            LSP identifiers TLV (IPV4)

            Symbolic path name TLV

            LSP Error code TLV

            RSVP Error Spec TLV

##### ERO Object

        Explicit route objects contain list of variable length SubObjects.

###### Supported SubObjects

          IPv4 Prefix

          IPv6 Prefix

          Autonomous System number

          SR-ERO SubObject

          Path Key SubObject

##### BANDWIDTH Object

        This object used to specify the requested bandwidth for a TE LSP.

#### PCRpt message

    Report message is sent by PCC in response to PCInitiate/PCUpd messages. Report message is also sent for synchronizing LSP state DB between PCC and PCE immediately after the session establishment. The objects supported in PCRpt message are

##### SRP Object

        The SRP (Stateful PCE request parameters) object set the unique identifier for mapping   request/response between PCEP and PCC. SRP object is optional in report messages sent for LSP state synchronization.

###### Supported TLV’s

            Symbolic path name TLV

##### LSP Object

        The LSP contains a set of fields used to specify the target LSP, the operation to be performed on the LSP and LSP delegation. It contains a S flag when true indicates to a PCE that the LSP state synchronization in progress.

###### Supported TLV’s

            LSP identifiers TLV (IPV4)

            Symbolic path name TLV

            LSP Error code TLV

            RSVP Error Spec TLV

##### RRO Object

        Record route objects contain list of variable length SubObjects.

###### Supported SubObjects

          IPv4 SubObject

          IPv6 SubObject

          Label SubObject

##### BANDWIDTH Object

        This object used to report the bandwidth for an existing TE LSP.

#### PCLabelUpd message

    This message is sent by PCE to PCC to download the label or update the label map. The same message is also used to clean the label entry. The objects supported are

##### SRP Object

        The SRP (Stateful PCE request parameters) object set the unique identifier for mapping   request/response between PCEP and PCC. SRP object is optional in report messages sent for LSP state synchronization.

###### Supported TLVs

            Symbolic path name TLV

##### LABEL Object

    The LABEL object used to specify the label information and must be carried within   PCLabelUpd message.

###### Supported TLVs

        NexthopIPv4address Tlv

        NexthopUnnumberedIPv4ID Tlv

##### FEC Object

        The FEC object is used to specify FEC information. The types of FEC objects supported are

        IPv4 Node ID

        IPv6 Node ID

        IPv4 Adjacency

        IPv6 Adjacency

#### LSRpt message

    This message is sent by PCC to PCE to report any changes in the TEDB. The objects supported in LS Report are

##### LS Object

        LS Object contains a set of fields used to specify target TE node or link. It also contains a flag indicating to a PCE that the TED synchronization in progress.

###### Supported TLVs

            Routing Universe TLV

            Local Node Descriptors TLV

            Remote Node Descriptors TLV

            Node Descriptors TLV

            Link Descriptors TLV

            Node Attributes TLV

            Link Attributes TLV

#### PCLRResv message

    This message is bidirectional between PCC and PCE. This message is sent by PCC to PCE for the reservation of label range. This message is sent by PCE to PCC to sent reserved label range for the network. The objects supported in this message are

##### SRP Object

        The SRP (Stateful PCE request parameters) object set the unique identifier for mapping   request/response between PCEP and PCC. SRP object is optional in report messages sent for LSP state synchronization.

###### Supported TLVs

            Symbolic path name TLV

##### Label Range Object

        This object carries label range information based on the label type.

#### PCErr message

    This message is sent by either PCC or PCE in several situations like, when a protocol error condition is met, when a request is not compliant with PCEP specification, policy violation, unexpected message etc. The objects supported in this message are

##### PCEP Error Object

        This object is carried in PCErr message to notify PCEP error

##### Open Object

        When the parameters in open message are not accepted, then PCErr message is sent to PCEP peer with Open object.
