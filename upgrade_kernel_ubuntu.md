### Steps to upgrade kinux kernel on Ubuntu 20.04


1. Check current version
```
uname -msr
```
2. Upgrade the new kernel version
```
sudo apt-get install linux-image-5.4.0-100-generic -y
```
3. Remove the old version
```
apt-get purge linux-image-5.4.0-97-generic
```
