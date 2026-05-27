# Command Line Interface Role-Based Access

ONOS CLI uses the Apache Karaf command-console shell and therefore uses the same means to configure the role-based access as Apache Karaf uses. This configuration is divided into two areas.

1. configuration of roles required by each command (or a usage variant)
2. configuration of roles granted to the user group

Both of these can be configured within the ONOS Apache Karaf directory `<onos-install-dir>/apache-karaf-3.0.8/etc/`.

### Configuring Roles Required By Commands

The roles required for each CLI command (or even command variant) are configured in the file `org.apache.karaf.command.acl.onos.cfg.` The default assignments of `viewer` and `admin` roles have been done on the basis of whether the command is read-only or whether it actually causes changes to the system. Here's an excerpt of this file:

```
...
allocations = viewer
annotate-device = admin
annotate-link = admin
annotate-port = admin
app = admin
app-ids = viewer
apps = viewer
balance-masters = admin
...
```

As new CLI commands or usage variants are added, this file will be updated to properly reflect the required role. Deployments may chose to modify this file to change the default role assignments according to their needs to either further constrain or relax access requirements. Note, that such changes need to be made on all the nodes of the ONOS cluster. ONOS presently does not provide any mechanism to synchronize these changes across the cluster.

### Configuring Roles Granted to User Groups

The default authentication scheme relies on `users.properties` and/or `keys.properties` files in the Apache Karaf `etc` directory. These files hold the user/password/group and user/key/group assignments, respectively. They also hold definitions of groups to which users are assigned. The group definitions are in terms of the roles that have been granted to the group members.

This is what the default users.properfiles file looks like:

```
karaf = karaf,_g_:admingroup
onos = rocks,_g_:admingroup
guest = guest,_g_:guestgroup
_g_\:admingroup = group,admin,manager,viewer,webconsole
_g_\:guestgroup = group,viewer
```

It defines three users: `karaf`, `onos`, `guest` and two groups `_g_:admingroup` and \_`g_:guestgroup`. The `_g_:admingroup` has been granted roles `admin`, `manager`, `viewer` and `webconsole`, whereas the \_`g_:guestgroup` has been granted only the `viewer` role. Therefore, users that belong to the former group, will be able to execute both the commands that require the `admin` role and those that require `viewer` role, whereas those users that belong to the latter group can execute only those commands requiring the `viewer` role, but not those that demand the `admin` role.

Similar group definitions and assignments can be performed in the `keys.properties` file as shown in the following example:

```
#karaf=AAAAB3NzaC1kc3MAAACBAP1/U4EddRIpUt9KnC7s5Of2EbdSPO9EAMMeP4C2USZpRV1AIlH7WT2NWPq/xfW6MPbLm1Vs14E7gB00b/JmYLdrmVClpJ+f6AR7ECLCT7up1/63xhv4O1fnxqimFQ8E+4P208UewwI1VBNaFpEy9nXzrith1yrv8iIDGZ3RSAHHAAAAFQCXYFCPFSMLzLKSuYKi64QL8Fgc9QAAAIEA9+GghdabPd7LvKtcNrhXuXmUr7v6OuqC+VdMCz0HgmdRWVeOutRZT+ZxBxCBgLRJFnEj6EwoFhO3zwkyjMim4TwWeotUfI0o4KOuHiuzpnWRbqN/C/ohNWLx+2J6ASQ7zKTxvqhRkImog9/hWuWfBpKLZl6Ae1UlZAFMO/7PSSoAAACBAKKSU2PFl/qOLxIwmBZPPIcJshVe7bVUpFvyl3BbJDow8rXfskl8wO63OzP/qLmcJM0+JbcRU/53JjTuyk31drV2qxhIOsLDC9dGCWj47Y7TyhPdXh/0dthTRBy6bqGtRPxGa7gJov1xm/UuYYXPIUR/3x9MAZvZ5xvE0kYXO+rx,_g_:admingroup
_g_\:admingroup = group,admin,manager,viewer,webconsole
_g_\:guestgroup = group,viewer
onos=WsRCPGNA4zYdqNj2z4vbYNESCfo65q0sVGml47zbwR6MBTt6jeiy...ak5newZ6vf6CZ+ztj+V8V,_g_:admingroup
guest=1aasudhasd98123.....ajkhasdjahda8q1wekajshdjkahdjkashd19e1231akjdasdadadadad,_g_:guestgroup
```

Note that changes to these files must be made on each node in the ONOS cluster as ONOS currently does not offer a way to synchronize these configurations throughout the cluster.

Also note that two convenience tools `onos-user-password` and `onos-user-key` have been provided to alter these files, but those tools currently work only for users that belong to the `_g_:admingroup`. To make custom group definitions and user assignments, direct edits to the files will be needed.
