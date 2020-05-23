```
ansible localhost -m setup
ansible all -i inventory/demo.ini -m ping
scp -6 root@\[ffee:40b::10\]:/home/stack/images/overcloud-full.qcow2 .
%!python -mjson.tool
ip -6 neighbor show
tailf /var/log/nova/nova-scheduler.log | grep  "not match requested node"
sudo sysctl –p /etc/sysctl.conf
```

Shorten encryption to fix SSH connectivity issues
```
ssh -o MACs=hmac-sha2-256 root@192.168.10.5
```
```
SSH to all the hosts and execute a specific command:
for i in `cat hosts` ; do echo $i; ssh -l root -oStrictHostKeyChecking=no $i "sudo journalctl -t kernel | grep vrouter"; done
```
