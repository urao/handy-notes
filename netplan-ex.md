### Netplan configuration example
```
network:
    version: 2
    ethernets:
        ens3:
            addresses: 
                - 192.168.122.201/24
            gateway4: 192.168.122.1
            nameservers:
                addresses: [192.168.122.1]
        ens8: {}

    vlans:
        vlan.101:
            id: 101
            link: ens8
            addresses: [192.168.101.1/24]
        vlan.102:
            id: 102
            link: ens8
            addresses: [192.168.102.1/24]
```
