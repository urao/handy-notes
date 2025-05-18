# KVM command to install vSRX

```
cp junos-vsrx3-x86-64-21.4R3.15.qcow2 /var/lib/libvirt/images/vsrx000.qcow2
virt-install --name vSRX000 --ram 4096 --cpu SandyBridge, --vcpus=2 --arch=x86_64 \
--disk path=/var/lib/libvirt/images/vsrx000.qcow2,size=16,device=disk,bus=ide,format=qcow2 \
--os-type linux --os-variant rhel7.0 --import --network=network:openshift4,model=virtio
```

```
cp junos-vsrx3-x86-64-21.4R3.15.qcow2 /var/lib/libvirt/images/vsrx001.qcow2
virt-install --name vSRX001 --ram 4096 --cpu SandyBridge, --vcpus=2 --arch=x86_64 \
--disk path=/var/lib/libvirt/images/vsrx001.qcow2,size=16,device=disk,bus=ide,format=qcow2 \
--os-type linux --os-variant rhel7.0 --import --network=network:openshift4,model=virtio --noautoconsole
```
