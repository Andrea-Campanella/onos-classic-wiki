# How to log on external syslog servers

Different users expressed the exigence to log (specially in production environments) to external syslog servers.

By deafult, ONOS uses the log4j library to provide its logging functionality. Change its standard behavior is pretty easy: the user needs only to add an additional appender (a syslog appender) to a specific configuration file, which will overwrite the standard one provide with ONOS.

In this little howto it's assumed the following:

* A syslog server is configured and running, and it can accept connections from the ONOS server.
* ONOS has just been cloned from the ONOS repository and we're in the main onos directory (i.e. ~/onos).

Please, follow the steps below:

* Copy the default configuration file of log4j (provided with ONOS) inside the proper config folder

  ```
  $ cp ~/onos/tools/package/etc/org.ops4j.pax.logging.cfg ~/onos/tools/package/config/org.ops4j.pax.logging.cfg
  ```
* Edit the configuration file with the editor you prefer and modify it accordingly

  ```
  #
  #       http://www.apache.org/licenses/LICENSE-2.0
  #
  #    Unless required by applicable law or agreed to in writing, software
  #    distributed under the License is distributed on an "AS IS" BASIS,
  #    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  #    See the License for the specific language governing permissions and
  #    limitations under the License.
  #
  ################################################################################

  # Root logger
  log4j.rootLogger=INFO, out, syslog, osgi:*
  log4j.throwableRenderer=org.apache.log4j.OsgiThrowableRenderer

  # CONSOLE appender not used by default
  log4j.appender.stdout=org.apache.log4j.ConsoleAppender
  log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
  log4j.appender.stdout.layout.ConversionPattern=%d{ISO8601} | %-5.5p | %-16.16t | %-32.32c{1} | %X{bundle.id} - %X{bundle.name} - %X{bundle.version} | %m%n

  # Syslog appender
  log4j.appender.syslog=org.apache.log4j.net.SyslogAppender
  log4j.appender.syslog.layout=org.apache.log4j.PatternLayout
  log4j.appender.syslog.layout.ConversionPattern=%d{ISO8601} | %-5.5p | %-16.16t | %-32.32c{1} | %X{bundle.id} - %X{bundle.name} - %X{bundle.version} | %m%n
  log4j.appender.syslog.syslogHost=IP-OF-SYSLOG-SERVER
  log4J.appender.syslog.facility=KARAF
  log4j.appender.syslog.facilityPrinting=false

  # File appender
  log4j.appender.out=org.apache.log4j.RollingFileAppender
  log4j.appender.out.layout=org.apache.log4j.PatternLayout
  log4j.appender.out.layout.ConversionPattern=%d{ISO8601} | %-5.5p | %-16.16t | %-32.32c{1} | %X{bundle.id} - %X{bundle.name} - %X{bundle.version} | %m%n
  log4j.appender.out.file=${karaf.data}/log/karaf.log
  log4j.appender.out.append=true
  log4j.appender.out.maxFileSize=1MB
  log4j.appender.out.maxBackupIndex=10

  # Sift appender
  log4j.appender.sift=org.apache.log4j.sift.MDCSiftingAppender
  log4j.appender.sift.key=bundle.name
  log4j.appender.sift.default=karaf
  log4j.appender.sift.appender=org.apache.log4j.FileAppender
  log4j.appender.sift.appender.layout=org.apache.log4j.PatternLayout
  log4j.appender.sift.appender.layout.ConversionPattern=%d{ISO8601} | %-5.5p | %-16.16t | %-32.32c{1} | %m%n
  log4j.appender.sift.appender.file=${karaf.data}/log/$\\{bundle.name\\}.log
  log4j.appender.sift.appender.append=true
  ```
* Reconfigure the target ONOS nodes / deploy ONOS, as described in the users guide on the wiki.
