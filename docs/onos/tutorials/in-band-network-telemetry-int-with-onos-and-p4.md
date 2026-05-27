# In-band Network Telemetry (INT) with ONOS and P4

The page outlines instructions to achieve INT through ONOS and P4.

# Material

For the details of the demonstration, please see followings:

1. [Abstract](https://p4.org/assets/P4WS_2018/11_INT-XDP_Abstract.pdf)
2. [Demo slide](https://p4.org/assets/P4WS_2018/11_Jonghwan_Hyun_INT-XDP.pdf)
3. [Demo poster](https://docs.google.com/presentation/d/1ygeJs0p1Rg5b7hiVtCqT9gOggAJMb8y9N00DNfzWJeI/edit?usp=sharing)
4. [Demo video](https://youtu.be/ZXRef0IhXGM)

# Requirements

* Ubuntu 18.04 with kernel version >= v4.14
* Python 2.7, python-pip, mininet, InfluxDB, Grafana

# Provision emulator VM

### Install p4tools

```
$ onos-setup-p4-dev
```

### Install BPFCollector

* Install pre-built **bcc** package from <https://github.com/iovisor/bcc>
* Clone BPFCollector repo. (See [BPFCollector](https://gitlab.com/tunv_ebpf/BPFCollector) for details.)

  ```
  $ git clone https://gitlab.com/tunv_ebpf/BPFCollector.git
  $ cd BPFCollector
  $ git checkout -t origin/spec_1.0
  ```

* Enable JIT for eBPF to make BPFCollector run faster

  ```
  $ sudo sysctl net/core/bpf_jit_enable=1
  ```

* Install Cython to run the InfluxDB Client with better performance

  ```
  $ pip install Cython
  ```

* Add virtual interfaces for collector

  ```
  $ sudo ip link add veth_1 type veth peer name veth_2 
  $ sudo ip link set dev veth_1 up 
  $ sudo ip link set dev veth_2 up 
  ```

### Modify Mininet topology script

* Modify the file *$ONOS\_ROOT/tools/test/topos/bmv2-demo.py*
  + Look for this line:

    ```
    from mininet.link import TCLink
    ```
  + Change the line as follows:

    ```
    from mininet.link import TCLink, Intf
    ```
  + Look for this line:

    ```
    net.build()
    ```
  + Below this line, add the followings:

    ```
    collectorIntf = Intf( 'veth_1', node=net.nameToNode[ "s12" ] )
    ```

# How to run

* Run ONOS

  ```
  $ ONOS_APPS=drivers.bmv2,proxyarp,lldpprovider,hostprovider,fwd bazel run onos-local -- clean
  ```

* Launch Mininet

  ```
  $ sudo -E $ONOS_ROOT/tools/test/topos/bmv2-demo.py --onos-ip=127.0.0.1 --pipeconf-id=org.onosproject.pipelines.int
  ```

* Launch the collector

  ```
  $ sudo systemctl start influxdb
  $ sudo python BPFCollector/InDBClient.py veth_2
  ```

* Activate In-band telemetry control application

  ```
  $ onos-app localhost activate org.onosproject.inbandtelemetry
  ```

  You may see the following WARN log right after activating the INT control application.

  ```
  2019-02-15T11:23:30,143 | WARN  | onos-shared-scheduled-onos-pool-executor-2 | SimpleIntManager                 | 231 - org.onosproject.onos-apps-inbandtelemetry-impl - 2.1.0.SNAPSHOT | Missing INT config, aborting programming of INT device device:bmv2:s22
  ```

  It will be disappeared when you add collector configuration.

  **Please note that the INT monitoring works only after the collector configuration is done.**

* Add mirroring configuration on the switch for telemetry report

  ```
  $ simple_switch_CLI --thrift-port `cat /tmp/bmv2-s12-thrift-port` 
  RuntimeCmd: mirroring_add 500 5 
  (500: REPORT_MIRROR_SESSION_ID defined in int_definitions.p4) 
  (5: port number to send mirrored packet, in this case veth_1)
  ```

* Add collector configuration
  + Connect to ONOS web interface (<http://localhost:8181/onos/ui/>)
  + Open "In-band Telemetry Control" in the menu
  + Type **127.0.0.1** to "IPv4 address" field and **54321** to "port" field in "INT Collector Configuration" section
  + Clink "Apply Configuration" button
* Add IntIntent to specify traffic to monitor
  + Open "In-band Telemetry Control" in the ONOS GUI menu
  + Fill in "Source IP address", "Destination IP address", "Source port", "Destination port" and "Protocol" field
    - Source and Destination IP address fields accepts IP address with mask (e.g., 10.0.0.0/24)
    - Source and Destination port number requires exact port number
    - Protocol supports either TCP or UDP
    - Any field remained empty, except Protocol field, means wildcard.
  + Choose metadata to collect
    - **Switch Id** and **Egress timestamp** must be chosen so as to make the collector to work properly.
    - "Egress Port Tx Utilization" are not supported in current version of BMv2 software switch yet.
  + Click "Apply Watchlist Rule" button below the metadata to deploy INT Intent.
  + Created INT Intent will be appeared in the table below.
* Generate some traffic to monitor

  ```
  mininet> h11 iperf -c h22 -u -t 10000
  ```

* Connect Grafana to see the collected data at <http://localhost:3000>
