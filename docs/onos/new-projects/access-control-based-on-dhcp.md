# Access Control Based on DHCP

**Team**

|  |  |  |
| --- | --- | --- |
| **Name** | **Organisation** | **Email** |
| Vincent CATROS | IRT b<>com | [vincent.catros@b-com.com](mailto:vincent.catros@b-com.com) |
| Riwal KERHERVE | IRT b<>com | [riwal.kerherve@b-com.com](mailto:riwal.kerherve@b-com.com) |
| Alexis MUNYANDEKWE | IRT b<>com | [alexis.munyandekwe@b-com.com](mailto:alexis.munyandekwe@b-com.com) |

**Overview**

The proposed ONOS application provides access control based on DHCP.

TR-101 issued by the BBF specifies BNG’s DHCP functionalities in particular regarding option 82. This option is used for customer identification purpose. A DHCP ACK could then be considered as an access authorization.

The proposed application will control customer ports access based on DHCP snooping. Each customer port will be set by default to “restricted” state. In that state only DHCP traffic is allowed. Based on DHCP snooping, when the DHCP server grants access to a customer through DHCP ACK, the relevant customer port is switched to “granted” state. In that state the customer’s traffic is fully allowed. The port/customer will be switched back to the restricted state either upon DHCP NAK or end of lease.

**Framework**

 C1          ONOS Controller  
       \                /  
         \             /  
 C2--- OpenFlow Switch----------DHCP server  
        /  
      /  
  Cn
