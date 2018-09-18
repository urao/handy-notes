### Steps to create a VM

1. Copy ISO on to the host machine
2. Make sure you have enough DISK, RAM to create a VM, run the below command
```
virt-install --name vm1 --ram 24000 --disk path=/var/lib/libvirt/images/vm1.img,size=100 --vcpus 8 \
--os-type linux --os-variant ubuntu16.04 --network bridge=internet --network bridge=br2  --graphics none \  
--console pty,target_type=serial --location <ISO_File_Location> --extra-args 'console=ttyS0,115200n8 serial'
```
