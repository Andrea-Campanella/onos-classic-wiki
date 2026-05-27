# Increasing VM disk space

# Step 1: Increase the VMDK size

## Using Virtual Box

Unfortunately, Virtual Box cannot resize VMDKs, but it can resize VDI images. So, we will convert the disk to a VDI, and then increase its size.

1. Shut down the VM.
2. Find the location of the VMDK (e.g. /Users/<user>/VirtualBox VMs/<VM Name>/)

   ```
   $ cd "~/VirtualBox VMs/<VM Name>/"
   ```
3. Using VBoxManage to clone the image and resize it.

   ```
   $ VBoxManage clonehd <VMDK Name>.vmdk clone.vdi --format vdi
   $ VBoxManage modifyhd clone.vdi --resize 20480 #size in MB (20 GB)
   ```
4. Update VirtualBox to use the new image. This can be done using the command line, but it's easier to use the GUI. Select the VM and click the **Setting** button. Navigate to the storage tab, click on the old virtual disk, and then click on the small minus at the bottom to remove the drive. Then, click the little hard drive with the plus sign on the SCSI controller to add your new disk. Select choose existing disk, and then clone.vdi.

## Using VMWare

It is really easy to increase the size of a VMDK in VMWare. First, shut down the VM and open the **VM Settings Panel**. Click on the **Hard Disk** icon, and enter the new disk size.

# Step 2: Increase the Partition size

Some may consider the following "dangerous". However, you already have a backup of your virtual disk if you used the VirtualBox method above. If you want to be "safer", find a LiveCD or GParted ISO, and perform the following steps with /dev/sda1 unmounted.

But, without further ado:

1. Boot up your VM with the new or enlarged virtual disk.
2. Turn off swap

   ```
   $ sudo swapoff /dev/sda5
   $ sudo sed -i 's/\(^.*swap.*$\)/#\1/' /etc/fstab
   ```
3. Remove the swap partitions (/dev/sda5) and the extended partition (/dev/sda2), then resize (delete and recreate) the root partition (/dev/sda1)

   ```
   $ sudo fdisk /dev/sda
   Command: d
   Partition number: 5
   Command: d
   Partition number: 2
   Command: d
   Command: n
   Select: p
   Partition number: 1
   First sector: 2048
   Last sector: <enter to take default, which is the end of the disk>
   Command: w
   ```
4. The changes will not be taken into effect until reboot. We also want to do fsck on reboot.

   ```
   $ sudo touch /forcefsck
   $ sudo reboot
   ```

# Step 3: Increase the Filesystem size

All you need to do is run the following:

```
$ sudo resize2fs /dev/sda1
```

You can verify your hard work with:

```
$ df -h
```
