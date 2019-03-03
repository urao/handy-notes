## OVS Commands CHEATSHEET

1.) Configure ovs-vswitchd configuration
```
ovs-vsctl show
ovs-vsctl list-br
ovs-vsctl list-ports <bridge-name>
ovs-vsctl list interface
ovs-vsctl add-br <bridge-name>
ovs-vsctl add-port <bridge-name> <interface>
ovs-vsctl add-port <bridge-name> <interface> tag=<VLAN number>
``` 
2.) Debugging commands, when there is no traffic flow after
    linking an interface (eth3) to an OVS bridge (bridge1)
```
ovs-vsctl show
ovs-vsctl list-ports bridge1
ovs-ofctl dump-ports-desc bridge1
ovs-ofctl dump-flows bridge1
cat /proc/sys/net/ipv4/ip_forward, check this value is configured to 1
restart network services
ovs-ofctl dump-ports-desc bridge1
```
