## Execute below commands to create network in KVM env using root permissions

### Create a new network, called net1-network.xml
```
<network>
    <name>net1-network</name>
    <forward mode="bridge" />
    <bridge name="br1" />
</network>
```

```
virsh net-list --all
virsh net-edit default
virsh net-define net1-network.xml
virsh net-start net1-network
virsh net-autostart net1-network
virsh net-list --all
```
