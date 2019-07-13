### Useful commands
```
tcpdump -i em0 "icmp[0] == 8"
tcpdump -i eth0 "icmp6 && ip6[40] == 128"
tcpdump -i eth0 -vv ip6
tcpdump -i eth1 port not 22 and host 10.1.1.1
tcpdump -i br-ctlplane -vvv -s 1500 'port 67 or port 68'
```
