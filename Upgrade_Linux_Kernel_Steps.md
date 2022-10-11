#### Below steps to upgrade linux kernel on Ubuntu 20.04 from 5.4.0-97-generic to 5.4.0-100-generic

1. Check current linux kernel version
```
uname -msr
```
2. Install new version of kernel
```
sudo apt-get install linux-image-5.4.0-100-generic -y
```
3. Check installed kernel versions
```
grep menuentry /boot/grub/grub.cfg
sudo dpkg -l | grep ii | grep linux-image-[0-9].*-generic
```
4. Purge old kernel version
```
sudo apt-get purge linux-image-5.4.0-97-generic
```
5. Reboot the machine 
```
su reboot
```
6. Check the kernel version
```
uname -msr
```
