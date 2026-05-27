# Backup/Restore Tutorial

Much of the state in an ONOS cluster is stored on disk in the ONOS data directories. Often times, users want a way to migrate, update, or upgrade a node without losing its state. ONOS provides two scripts to help aid in that process:

## Backing up a node

Prior to backing up a node, ensure the ONOS instance has been shutdown. To backup the persistent state of a node, users can use the `onos-backup` script packaged in the ONOS distribution. This script is a simple helper that creates a tarball containing all the node's persistent state. Simply run `onos-backup`, and by default the script will create an `onos-data.tar.gz` file outside the root ONOS directory.

```
export ONOS_HOME=~/onos
onos-backup
```

Note: prior to calling the onos-backup script, you may need to ensure your `$ONOS_HOME` environment variable is set.

## Restoring a node from backup

To restore the state of a node, ONOS provides the `onos-restore` script. This script takes a tarball created by the `onos-backup` script described above and unpacks it to the appropriate ONOS data directories. Once a node's state has been restored, it can be restarted with the same state.

```
onos-restore ~/onos-data.tar.gz
```

## Caveats

The backup and restore mechanisms provided with ONOS can be useful for restoring the state of an existing node or performing an offline upgrade of a node. ONOS guarantees that the persistent state of a version n node will be compatible with version n+1 nodes (until semantic versioning is implemented). However, there are some caveats to keep in mind when using this feature. Most notably, in order for an ONOS controller node to be migrated between hosts - backed up on one host and restored on another - the cluster should be configured with named nodes. Many ONOS configurations substitute the host IP as a node name in the cluster configuration. However, nodes can also be identified by arbitrary unique names. It is recommended that ONOS cluster nodes be configured with unique names rather than simple IP addresses if the backup/restore feature will be used to migrate a node between hosts.
