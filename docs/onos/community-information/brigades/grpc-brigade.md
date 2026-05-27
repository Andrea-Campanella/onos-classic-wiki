# gRPC brigade

## **What is gRPC?**

gRPC is a Google open-source project which provides efficient language-agnostic communication.  It utilizes two key technologies: protocol buffers to provide efficient serialization for transmission, and http/2 for asynchronous communication.  The result is highly efficient communication that enables off-platform applications to interact with ONOS with minimal cost.

**Links:**

[gRPC guide](http://www.grpc.io/docs/guides/)

[Protocol Buffer guide](https://developers.google.com/protocol-buffers/docs/overview) (NOTE: we will be using proto3)

[http/2 guide (RFC)](https://tools.ietf.org/html/rfc7540) (NOTE: only a basic understanding of http/2 is required to work on this)

[Design Document](https://docs.google.com/document/d/1CI-IqH4_Dr6nFz07LEww-KEDHmUJ30PikHPxe6_6gXg/edit?usp=sharing) (Currently draft)

[Meeting notes](https://drive.google.com/drive/folders/0B-pY39PjyMtHX1BpYU9lVE1jUkU?usp=sharing)

## **Weekly meeting:**

Weekly meeting time is Tuesday from 10am to 11am Korea Standard Time (Monday 6pm - 7pm Pacific Standard Time).

## **Mailing list**

Join the brigade for discussions on the gRPC mailing list at: <https://groups.google.com/a/onosproject.org/forum/#!forum/brigade-grpc>

## **Why gRPC?**

gRPC will enable more ONOS apps to be moved off-platform consuming fewer system resources and providing a degree of isolation to reduce the chances of a fault in an application effecting the system as a whole.

**Brigade Leads:**

[Aaron Kruglikov - Fujitsu](mailto:aaron@onlab.us)

[Jian Li - ONF](mailto:jian@opennetworking.org)

**Active Brigade Members:**

* [Jian Tian - ZTE Corporation](mailto:tian.jian@zte.com.cn)
* [Frank Wang - Inspur](mailto:wangpeihui@inspur.com)

**Inactive Brigade Members:**

* [Asif Raza - KISTI](mailto:asif@kisti.re.kr)
* [Shivani Vaidya - ONF](mailto:shivani@opennetworking.org)
* [Ke Zhiyong - ZTE Corporation](mailto:ke.zhiyong@zte.com.cn)
* [Wu Shaoyong - ZTE Corporation](mailto:wu.shaoyong@zte.com.cn)

**Brigade Status:**

Some service implemented, many models implemented.

**Brigade Members:**

We are seeking a group of 3 or 4 members.

****Contact the brigade:****

We have a google group which can be found [here](https://groups.google.com/a/onosproject.org/forum/#!forum/brigade-grpc).

We also have a slack channel within ONOS slack.

**Scope:**

**Short Term:**

* Support gRPC as a northbound interface.
* Create handcrafted message types to provide access to system services (similar to the current REST API's but with improved performance via HTTP/2 multiplexing and improved encoding efficiency).
* Create thorough test suites.

**Long Term:**

* Create language packs for other languages to enable use of more complicated models (i.e. topology)
* Add support for automatic code generation from ONOS service API's.
* Explore the possibility of enabling gRPC for East/West communication.

**How to get involved:**

Contact Jian at [jian@opennetworking.org](mailto:jian@opennetworking.org) (please include "gRPC" in the subject).
