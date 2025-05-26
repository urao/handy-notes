
## virt-install commands

```
virt-install --name ricvm --ram 32768 \
--vcpus=14 --arch=x86_64 --disk path=/home/images/ricvm.qcow2,size=150,bus=virtio,format=qcow2 \
--os-variant ubuntu22.04 --cdrom=/home/images//ubuntu-20.04.6-live-server-amd64.iso  \
--network=network:default,model=virtio --noautoconsole
```

```
virt-install --name jmastervm --ram 32768 --vcpus=8 --arch=x86_64 \
--disk path=/home/images/jmastervm.qcow2,size=150,format=qcow2 --os-variant rocky8.6 \
--cdrom=/home/images/Rocky-8.6-x86_64-minimal.iso --network=network:default,model=virtio --noautoconsole
```

```
virt-install --name vSRX001 --ram 4096 --cpu SandyBridge, --vcpus=2 --arch=x86_64 \
--disk path=/var/lib/libvirt/images/img_vSRX_00.qcow2,size=16,device=disk,bus=ide,format=qcow2 \
--os-type linux --os-variant rhel7 --import --network=network:mgmt-net,model=virtio \
--network=network:testport1,model=virtio --network=network:testport2,model=virtio \
--network=network:hsl-net,model=virtio --noautoconsole
```

```
virt-install --import --name jworker1vm --ram 16384 --vcpus=4 --arch=x86_64 \
--disk path=/home/images/jworker1vm.qcow2,size=180,bus=virtio,format=qcow2 \
--os-variant rocky8.6 --network=network:default,model=virtio --noautoconsole
```

```
virt-install --name vSRX001 --ram 4096 --cpu SandyBridge, --vcpus=2 \
--arch=x86_64 --disk path=/var/lib/libvirt/images/img_vSRX_00.qcow2,size=16,device=disk,bus=ide,format=qcow2 \
--os-type linux --os-variant rhel7 --import --network=network:mgmt-net,model=virtio \
--network=network:testport1,model=virtio --network=network:testport2,model=virtio \
--network=network:hsl-net,model=virtio --network=network:bpport1,model=virtio \
--network=network:bpport2,model=virtio --network=network:internet-net,model=virtio --noautoconsole
```
