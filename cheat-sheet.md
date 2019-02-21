### Useful commands
```
openstack flavor create --public small --id auto --ram 4096 --disk 40 --vcpus 2
openstack flavor create --public m1.tiny --id auto --ram 512 --disk 10 --vcpus 1
openstack image create ugolden-img --public --container-format bare --disk-format qcow2 --file golden-vm.qcow2
openstack image create sriov-img --public --container-format bare --disk-format qcow2 --file sriov-latest.qcow2
```
