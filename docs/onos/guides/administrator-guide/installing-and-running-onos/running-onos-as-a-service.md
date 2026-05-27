# Running ONOS as a service

Sometimes it’s useful to run ONOS as a service, particularly in production environments. This is where things get more complicated and specialized, depending on the operating system you’re running. This section describes how to configure ONOS to run as a service on typical Linux distributions.

When ONOS runs as a service, the OS will start it automatically as part of the boot process. On `systemd` and `upstart`-based systems, it should also automatically be restarted if it crashes. Once the service configuration files have been installed, you can typically start, stop, and check the status of ONOS using the `service` command.

**Please not that this guide has different commands for different systems (i.e. Ubuntu, Debian, etc.) ensure you are running the correct command for your version, have fun.**

## Install the service files

**Mandatory step for all OSes**

```
sudo cp /opt/onos/init/onos.initd /etc/init.d/onos
```

**Additional step for Ubuntu 12 (and older Debian systems)**

```
sudo update-rc.d onos defaults
```

Note that on other, older, systems that use the `/etc/init.d/` scripts but do not included the `update-rc.d` command you may need to manually create symbolic links in the appropriate `rcX.d/` directories as desired, if you wish ONOS to start automatically.

**Additional step for Upstart based systems (i.e. Ubuntu 14)**

```
sudo cp /opt/onos/init/onos.conf /etc/init/onos.conf
```

**Additional steps for Systemd based systems (i.e. Ubuntu 16, CentOS 7+)**

```
sudo cp /opt/onos/init/onos.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable onos
```

## Configure ONOS Options

The ONOS services read configuration options from `/opt/onos/options`. If you have created an ONOS user (e.g. `sdn`), you should set `ONOS_USER` in `/opt/onos/options` to the user you wish ONOS to run as.

You can also specify `ONOS_APPS` as a default set of applications to activate.

**sample /opt/onos/options file**

```
ONOS_USER=sdn
# Optional: add any apps here that you wish to activate by default
ONOS_APPS=
```

Note that `ONOS_APPS` is an optional way of specifying default apps to activate on a node, but you can also activate apps dynamically across the entire ONOS cluster using the ONOS CLI, as described in [Managing ONOS applications](../configuring-onos/managing-onos-applications.md).

## Start, stop, or check the status of the ONOS service

**Additional steps for Upstart based systems (i.e. Ubuntu 14)**

```
sudo service onos {start|stop|status}
```

**Additional steps for Systemd based systems (i.e. Ubuntu 16, CentOS 7+)**

```
sudo systemctl {start|stop|status|restart} onos.service
```
