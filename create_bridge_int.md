### Run below commands to create bridge interface
### Tested on Ubuntu 24.04

# Install packages
```
sudo apt-get install bridge-utils net-tools -y
```

# Update netplan configuration file as below
```
root@kvm-ubuntu:~# cat /etc/netplan/01-netcfg.yaml
network:
  ethernets:
    eno8303:
      dhcp4: false
      dhcp6: false
  # add configuration for bridge interface
  bridges:
    br0:
      interfaces: [eno8303]
      dhcp4: false
      addresses: [192.168.122.169/24]
      routes:
        - to: default
          via: 192.168.122.1
      nameservers:
        addresses: [8.8.8.8]
      dhcp6: false
  version: 2
```

# Apply netplan
```
sudo netplan apply
```

# Check the bridge
```
brctl show
```
