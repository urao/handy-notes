from scapy.all import *
from time import sleep
import sys


# How to use it
# Ex. send 20 packets to 192.168.10.1
# <script_name>.py 192.168.10.1 20

dst_ip = sys.argv[1]
count = int(sys.argv[2])
src_ip = "192.168.10.55"
malformed_packet = IP(src=src_ip, dst=dst_ip, ihl=2, version=3)/ICMP()
send(malformed_packet, count=count, inter=10)
