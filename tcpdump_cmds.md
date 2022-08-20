### Useful commands
```
tcpdump -i em0 "icmp[0] == 8"
tcpdump -i eth0 "icmp6 && ip6[40] == 128"
tcpdump -i eth0 -vv ip6
tcpdump -i eth1 port not 22 and host 10.1.1.1
tcpdump -i br-ctlplane -vvv -s 1500 'port 67 or port 68'
tcpdump  -evni eth1 "tcp and port 5269" -A
tcpdump -ni eth0 udp port 4789 -c 10
sudo tcpdump -ni vlan151 -e icmp6
sudo tcpdump -eni vnet1 udp
tcpdump -vnei ens3f1 "udp and port 4789"
tcpdump -vnei ens3f1 proto gre
tcpdump -nnei eth0 -vvv
sudo tcpdump -i en0 -s 0 -A 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504F5354' << capture GET/POST messages
```
