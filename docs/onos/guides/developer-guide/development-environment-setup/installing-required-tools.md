# Installing required tools

# Hardware

At least 16 GB of RAM is required to build ONOS with Bazel

# Operating System

ONOS development and deployment is only supported on Linux and Mac OS Operating systems for x86\_64 architectures.

# Python2 and Python3

Both Python2 and Python3 are required for some build tools

**Install Python**

```
sudo apt install python
sudo apt install python3
sudo apt install python-pip python-dev python-setuptools
sudo apt install python3-pip python3-dev python3-setuptools

pip3 install --upgrade pip
pip3 install selenium
```

# Git and git-review

Git and git-review will be used to pull and push code from/to the ONOS repository, so they need to be installed. To streamline the code review process, it is highly recommended that contributors install *`git-review`*

**Install git and git-review**

```
sudo apt-get install git
sudo apt-get install git-review
```

git-review on Mac

For more info about git-review refer to [this link](http://www.mediawiki.org/wiki/Gerrit/git-review)

If you're using a Mac, you may need to manually upgrade the `git-review` package dependency. (git-review [bug#1337701](https://bugs.launchpad.net/git-review/+bug/1337701))

```
$ sudo pip install --upgrade setuptools  
$ sudo pip install --upgrade git-review
```

# Install Bazelisk

ONOS is a large project comprising of multiple relatively independent modules that lend themselves to be built in parallel, resulting in much faster. This is why the project chose to build via [Bazel](https://bazel.build/).

[Bazelisk](https://github.com/bazelbuild/bazelisk) is a tool that manages multiple versions of Bazel. Different versions of ONOS have been verified on different versions of Bazel (as defined in their **.bazelversion** file). Using Bazel will ensure that you will build against the version of Bazel suitable for the release you are building on.

Developers should install Bazelisk([1.4.0](https://github.com/bazelbuild/bazelisk/releases) or greater at the time of writing) before they can build the project themselves.

Bazelisk should be downloaded and installed as a drop in replacement for the "bazel" command. It is recommended *not* to download Bazel directly yourself - let Bazelisk get the right version for you!

On **Linux** use

```
$ wget https://github.com/bazelbuild/bazelisk/releases/download/v1.4.0/bazelisk-linux-amd64
$ chmod +x bazelisk-linux-amd64
$ sudo mv bazelisk-linux-amd64 /usr/local/bin/bazel
$ cd ~/onos
$ bazel version
```

Alternatively, on **macOS**, Bazelisk can be installed via the [Brew](https://brew.sh) package manager:

```
$ brew install bazelisk
$ ln -s $(which bazelisk) /usr/local/bin/bazel # Create symlink to use as a drop-in replacement to the bazel command
$ cd ~/onos
$ bazel version
```

Calling "bazel version" causes Bazelisk to download Bazel and runs the "version" command on it. Bazelisk acts transparently and any command line arguments will be passed straight through to Bazel.

> Behind the scenes, Bazelisk caches downloaded Bazel versions in ~/.cache/bazelisk/
>
> Versions of Bazel can be preloaded using
>
> $USE\_BAZEL\_VERSION=1.2.1 bazel version
