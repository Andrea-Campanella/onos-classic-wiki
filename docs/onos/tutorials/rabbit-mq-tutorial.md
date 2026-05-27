# Rabbit MQ Tutorial

Work-in-progress. Completed page will be linked into the [Tutorials](../tutorials.md) page.

## **Overview**

ONOS Rabbit MQ application will be capture and parse the ONOS events and notifications. There by converting the below listed events into appropriate json schema and publish them on to MQ server. The interested ONOS and external applications can consume the published json messages.

## **MQ Supported ONOS event types**

* + Device Event  
    Describes infrastructure device event.
  + Port Event  
    Describes infrastructure port event.
  + Link Event  
    Describes infrastructure link event.
  + Topology Event  
    Describes network topology event.
  + Packet Event  
    Describes inbound packet received with raw payload.

## **MQ Client & Server Configuration**

        To configure Rabbit MQ event notification from ONOS the following components needs to be configured:

* + ### Rabbit MQ Server (External to ONOS)

    1. The latest release of RabbitMQ server can be available at <https://www.rabbitmq.com/download.html>  
    2. Please refer the server documentation at [administrator's guide](https://www.rabbitmq.com/admin-guide.html)  
    3. You can access the user-management with `rabbitmqctl` and use the command:

    ```
    rabbitmqctl add_vhost <vhost>
    rabbitmqctl add_user <username> <password>
    rabbitmqctl set_permissions -p <vhost> <username> ".*" ".*" ".*"
    rabbitmqctl set_user_tags <username> management
    ```

    4. Please refer the /resources/rabbitmq.properties file for sample mq properties.

* + ### ONOS Rabbit MQ App

Before proceeding to the following steps, see “wiki: Installing and Running ONOS” and “” for make it ready to run ONOS.

* Build package

  ```
  $ cd ~/onos/apps/rabbitmq
  $ mci
  ```

* + Run ONOS

    ```
    $ ok clean
    ```

* + Install bundle

    ```
    $ export OC1=<ONOS running ipAddress>
    $ onos-app $OC1 install ~/apps/rabbitmq/target/onos-app-rabbitmq-1.7.0-SNAPSHOT.oar
    ```

* + Activate rabbitmq app

    ```
    $ app activate org.onosproject.rabbitmq
    ```

* + ### Rabbit MQ Client (External to ONOS)

    Please follow below steps to setup MQ consumer application.  
    1. Extract below attached message-consumer-app.tar.gz  
    2. Refer MQConstants.java for sample MQ server consumer configuration.  
    3. Build and generate the jar using command :- mvn clean install  
    4. Run the consumer application using command :- java -jar MessageConsumer-jar-with-dependencies.jar  
    5. The consumed messages from the MQ server will be displayed on console.  
    [message-consumer-app.tar.gz](../../assets/message-consumer-app.tar.gz)

## **MQ ONOS event json attributes, definitions and structures**

For example device event message structure as below

```
{
"switch_id": "of:0000000000000001",
"infra_device_name": "SWITCH",
"event_type": "DEVICE_EVENT",
"sub_event_type": "DEVICE_UPDATED",
"hwVersion": "Open vSwitch",
"mfr": "Nicira, Inc.",
"serial": "None",
"sw_version": "2.5.0",
"chassis_id": 1,
"occurrence_time": "Tue Aug 23 15:40:59 IST 2016"
}
```

Please refer below attached document for complete set of json message structures, attributes and their definitions,

[mq\_message\_definition\_&\_structures.docx](../../assets/mq_message_definition__structures.docx)

## **What next?**

Enhance this application to support more ONOS events and publish them on to MQ server.
