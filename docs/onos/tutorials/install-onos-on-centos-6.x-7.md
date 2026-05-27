# Install ONOS on CentOS 6.X, 7

I noticed that many people expressed the exigence to install ONOS on CentOS 6.X, 7 based systems, since it's very common to find these types of systems in production environments. Even if this distribution is not officially supported at the moment I though it would be a good idea to come up with a way to use that.

Nothing complicated. Since ONOS is based on Java, which by definition can run on heterogeneous systems, it's just a matter of figuring out the right dependencies.

I came up with this little tutorial, that hopefully should quickly guide the users over the process.

**Important note:** The tutorial is based on the following assumptions:

* The process described below will focus on the requirements to both compile and run (as a target machine) ONOS. The final deployment procedure is then totally similar to the one described for Ubuntu in the main user guide.
* You've just installed a brand new CentOS box and have logged in for the first time.

### The basics: setup the network card, the hostname

First let's configure the network card.

```
$ ip link set eth0 up
$ vi /etc/sysconfig/network-scripts/ifcfg-eth0           # Replace "ON_BOOT = no" with "ON_BOOT = yes"
$ service network restart
```

Then let's set the hostname editing /etc/hostname and /etc/hosts.

```
$ vi /etc/sysconfig/network          # Check that the host name is correct
$ vi /etc/hosts
```

### Install dependencies

For **dependencies**, you can just use yum.

```
$ yum -y install vim openssh-server openssh-clients wget git xz gcc gcc-c++
```

Now we'll install Java8 on CentOS.

```
$ wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.rpm"

$ yum -y localinstall jdk-8u151-linux-x64.rpm
```

The **yum** command manages the the dependences, that's why we use it instead of **rpm**.

If check your version you should see something like that.

```
$ java -version
java version "1.8.0_151"
Java(TM) SE Runtime Environment (build 1.8.0_151-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)
```

If no you may have OpenJDK installed by default on your system.

```
$ java -version
openjdk version "1.8.0_151"
OpenJDK Runtime Environment (build 1.8.0_151-b12)
OpenJDK 64-Bit Server VM (build 25.151-b12, mixed mode)
```

It's normal, to use the right version you must manage the symbolic links with the command **alternatives**, it will automatically create symbolic links with the version of your choice.

```
$ sudo alternatives --config java

There are 3 programs which provide 'java'.

Sélection    Commande
----------------------------------------------
*  1           java-1.8.0-openjdk.x86_64 (/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.151-1.b12.el7_4.x86_64/jre/bin/java)
   2           java-1.7.0-openjdk.x86_64 (/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.161-2.6.12.0.el7_4.x86_64/jre/bin/java)
 + 3           /usr/java/jdk1.8.0_151/jre/bin/java
Enter to keep the current selection[+], or type selection number:3
```

Now you are using Oracle Java8.

For **maven** I followed this guide instead: <http://preilly.me/2013/05/10/how-to-install-maven-on-centos/>

We need to manually install a dependency called **ncurses**, compiling the package.This is how you should do it. If you see some errors at the end of the procedure, don't worry about it. It's a known issue of the package, that won't anyway hurt the functionality provided.

```
$ wget http://blog.starcklin.com/files/dpkg_1.17.6.tar.xz
$ tar -xf dpkg_1.17.6.tar.xz
$ cd dpkg-1.17.6
$ sudo yum install ncurses-devel ncurses
$ ./configure
$ make
$ cd utils
$ sudo make install
```

Let's **configure ssh.**

```
$ chkconfig sshd on
$ ssh-keygen -t rsa
```

### Configure IPtables and SELinux (CentOS 6.X)

IPtables and SELinux are enforced by default on CentOS. In this section I briefly show how to disable both, in order to don't deal with them. It's then up to the user to apply her/his specific configuration later on in a production environment.

**Deactivate IPtables**

```
$ sudo iptables -F
$ sudo service iptables save
$ sudo chkconfig iptables off
$ sudo chkconfig ip6tables off
```

**Deactivate SELinux**

```
$ echo 0 >/selinux/enforce
$ vi /etc/selinux/config  # replace "SELINUX=enforcing" to "SELINUX=disabled"
```

### Configure Firewalld and SELinux (Centos 7)

CentOS 7 is using a new firewall interface, **Firewalld**. As for Centos 6.X system we disable them.

**Deactivate Firewalld**

```
$ sudo systemctl stop firewalld
$ sudo systemctl disabled firewalld
```

**Deactivate SELinux**

```
$ sudo setenforce 0
$ vi /etc/selinux/config  # replace "SELINUX=enforcing" to "SELINUX=disabled"
```

### Configure an admin user

In order to use ONOS, we need to add a dedicated user, who must be sudoer (without the need of typing the password).

```
$ sudo adduser admin
$ sudo visudo  # add the following line at the END of the file: admin ALL=(ALL) NOPASSWD:ALL
               # Modify also the line From: "Defaults requiretty” to "Defaults !requiretty"
```

From this point we will continue as the admin user. If we did things correctly, we shouldn't be asked for the password.

```
$ sudo su admin
```

### Create needed directories:

```
$ mkdir -p ~/Downloads
$ mkdir -p ~/Applications
```

### Configure Git:

```
$ sudo git config --global http.sslverify false
```

### Install ONOS

At this point you can download/deploy on this machine ONOS, as described in the main user guide.

---
