### Useful YUM packages to be installed on Centos

#### Install KVM packages
```
yum install net-tools -y
yum install qemu-kvm libvirt libvirt-python libguestfs-tools virt-install -y
yum install -y qemu-kvm qemu-img virt-manager libvirt libvirt-python libvirt-client virt-install virt-viewer
yum install epel-release -y
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm
yum groupinstall 'Development Tools' SDL kernel-devel kernel-headers dkms -y
systemctl enable libvirtd
systemctl start libvirtd
```
