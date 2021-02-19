## Steps to send UDP traffic between between linux machines

1. Install `nc` tool 
2. On Centos, using command `yum install nc -y`
3. Run the command on server, `nc -u -l 9999`
4. On the client `server, nc -u <server_ipaddress> 9999`
5. Send send traffic.
6. Check the connection using command `netstat | grep 9999`
