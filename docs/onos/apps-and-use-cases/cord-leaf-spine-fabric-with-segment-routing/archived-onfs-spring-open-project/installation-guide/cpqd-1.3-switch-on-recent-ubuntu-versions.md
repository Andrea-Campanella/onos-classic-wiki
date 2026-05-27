# CPqD 1.3 switch on recent Ubuntu versions

You only need to follow the instructions on this page, if the compilation of the CPqD software switch failed when following the [Installation Guide](../installation-guide.md).

This page was originally created by Jonathan Hart - many thanks!

The CPqD 1.3 software switch cannot be compiled out of the box on recent versions of Ubuntu (>= 13.10 I believe).

In fact, the issue is not with the switch code itself but the netbee library it depends on which also needs to be compiled. The library cannot be compiled if your bison version is greater than 2.5. Unfortunately, since Ubuntu 13.10 the lowest available bison version is greater than 2.5, so the compilation doesn't work.

For more information, see the github issues here:  
<https://github.com/CPqD/ofsoftswitch13/issues/113><https://github.com/CPqD/ofsoftswitch13/issues/56> 

So, somehow you have to get an old version of bison on your system. There are multiple ways to do this, but I've detailed the approach I used below.

First, use the mininet script to download and try to install the ofsoftswitch13. The compile should fail at some point:

|  |
| --- |
| `mininet/util/install.sh -3f` |

Now we need to downgrade our bison version so that we can finish compiling the code. Add the sources from an old version of ubuntu to your apt sources. I created a file called `raring.list` in`/etc/apt/sources.list.d/` containing:

|  |
| --- |
| `deb http:``//old-releases.ubuntu.com/ubuntu/ raring main restricted`  `deb-src http:``//old-releases.ubuntu.com/ubuntu/ raring main restricted` |

Now update your apt cache and install the old version of bison:

|  |
| --- |
| `sudo apt-get update`  `sudo apt-get remove bison libbison-dev`  `sudo apt-get install bison=``2``:``2.5``.dfsg-3ubuntu1 libbison-dev=``2``:``2.5``.dfsg-3ubuntu1` |

Double-check you have bison 2.5 installed:

|  |
| --- |
| `jono``@ubuntu``:~$ bison --version`  `bison (GNU Bison)``2.5`  `Written by Robert Corbett and Richard Stallman.`  `...` |

The mininet install script should have placed the netbee source in your home directory. I'm assuming the directory is ~/nbeesrc-jan-10-2013, but you can adapt if it's different. We'll go there and finish compiling it (credit to the mininet install script):

|  |
| --- |
| `export NBEESRC=~/nbeesrc-jan-``10``-``2013`  `cd ${NBEESRC}/src`  `make clean`  `cmake .`  `make`  `sudo cp ${NBEESRC}/bin/libn*.so /usr/local/lib`  `sudo ldconfig`  `sudo cp -R ${NBEESRC}/include/ /usr/` |

Now netbee is installed on the system and you can go ahead and compile the CPqD software switch. Hopefully the mininet script has already cloned the repo for you at ~/ofsoftswitch13:

|  |
| --- |
| `cd ~/ofsoftswitch13`  `./boot.sh`  `./configure`  `make`  `sudo make install` |

Done.

|  |
| --- |
| `jono``@ubuntu``:~$ dpctl --version`  `dpctl``1.3``.``0` `compiled Jul``30` `2014` `22``:``20``:``00` |

Optional: if you care, you can upgrade bison back to the latest version. You may also want to remove the raring.list file you created earlier so there's no chance of accidentally installing old software.

|  |
| --- |
| `sudo apt-get install bison` |
