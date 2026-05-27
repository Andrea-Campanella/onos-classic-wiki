# OFAgent Tracer how-to

This section describes findings about options for enabling filtering of logs per specific OFAgent tenant (OFAgent logs) or virtual network (vnet logs). Refence: [Apache Karaf Container 3.x - Documentation](http://karaf.apache.org/manual/latest-3.0.x/#_log)

### Summary of Karaf capabilities and steps useful for filtering logs per virtual network and per OFAgent tenant:

* `log:display` is Apache Karaf (not ONOS) CLI command
* Apache Karaf has Unix like shell and Apache Karaf CLI commands (aka aliases) can be created on the fly using Apache Karaf shell or in script $ONOS\_INSTALL\_DIR/apache-karaf-3.0.8/etc/org.ops4j.pax.logging.cfg. Script is executed at the beginning of each session.  (see subsection [4.5 Using the console](http://karaf.apache.org/manual/latest-3.0.x/#_using_the_console))
* Apache Karaf can be configured to write specifically formatted log entries in separate files (i. e. files different from default ${ONOS\_INSTALL\_DIR}/apache-karaf-3.0.8/data/log/karaf.log (see subsection [4.7 Log/4.7.2 Commands](http://karaf.apache.org/manual/latest-3.0.x/#_commands_2)). **Important note:** the only option to make ONOS write logs to separate files is to enable SIFT appender (example is in Apache Karaf log service configuration file).

  ### Examples of Apache Karaf logging service configuration:

  **Appender and logger for several packages**

  ```
  log4j.appender.vnet=org.apache.log4j.RollingFileAppender
  log4j.appender.vnet.maxFileSize=10KB
  log4j.appender.vnet.maxBackupIndex=10
  log4j.appender.vnet.file=${karaf.data}/log/vnet.log
  log4j.appender.vnet.layout=org.apache.log4j.PatternLayout
  log4j.appender.vnet.layout.ConversionPattern=VNET_LOGS | %d | %-5.5p | [%24F:%t:%L] - %m%n
  log4j.appender.vnet.appender.append=false

  log4j.logger.org.onosproject.incubator.net.virtual=TRACE, vnet
  log4j.additivity.org.onosproject.incubator.net.virtual=false

  log4j.logger.org.onosproject.incubator.store.virtual=DEBUG, vnet
  log4j.additivity.org.onosproject.incubator.store.virtual=false

  log4j.logger.org.onosproject.cli.net.vnet=INFO, vnet
  ```

  ### Examples of Apache Karaf shell configuration:

  ```
  onos>filter_vnet_logs = { log:display | grep "VNET_LOGS" | grep "$1" }
  onos>filter_vnet_logs <vnet_id>
  onos>filter_ofagent_logs <tenant_id>
  onos>filter_ofagent_logs = { log:display | grep "OFAGENT_LOGS" | grep "$1" }
  ```
