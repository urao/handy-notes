#!/usr/bin/env bash
# Tested on centos 7.4 and Ubuntu 16.04.2

set -e

EXITCODE=0

function create_bond_on_ubuntu () {
   apt install -y lshw ifenslave
   echo "Creating bond interfaces on Ubuntu"
   if lsmod | grep bond; then
      echo "Bonding module already loaded"
   else
      echo "Bonding module is not loaded"
      sudo modprobe bonding
   fi
   echo "loop" >> /etc/modules
   echo "lp" >> /etc/modules
   echo "rtc" >> /etc/modules
   echo "bonding" >> /etc/modules
   echo
   echo "Updating interfaces file"
   echo
   cat << EOF > /etc/network/interfaces
auto $1
iface $1 inet manual
    bond-master $3
    bond-primary $1

auto $2
iface $2 inet manual
    bond-master $3

auto $3
iface $3 inet static
    address $4
    netmask $4
    bond-mode 4
    bond-miimon 100
    bond-slaves none
EOF
   echo "Creation of the interface configuration files is done!!"
   echo
   echo "Bring up interfaces now!"
   sudo ifconfig $1 down && ifconfig $2 down && ifconfig $3 down
   sudo ifconfig $1 up && ifconfig $2 up && ifconfig $3 up
   echo -e "Output of ifconfig \n"
   ifconfig
   echo -e "Done !!!! \n\n"
}

function create_bond_on_centos () {
   yum install -y lshw pciutils net-tools
   echo "Creating bond interfaces on centos"
   sudo lsmod | grep bonding >& /dev/null
   if lsmod | grep bond; then
      echo "Bonding module already loaded"
   else
      echo "Bonding module is not loaded"
      sudo modprobe --first-time bonding
   fi
   echo "bonding" > /etc/modules-load.d/bonding.conf

   echo
   echo "Creating interface $1 file"
   echo
   cat << EOF > /etc/sysconfig/network-scripts/ifcfg-$1
TYPE=Ethernet
BOOTPROTO=none
NAME=$1
DEVICE=$1
ONBOOT=yes
MASTER=$3
SLAVE=yes
NM_CONTROLLED=no
EOF
   echo "Creating interface $2 file"
   echo
   cat << EOF > /etc/sysconfig/network-scripts/ifcfg-$2
TYPE=Ethernet
BOOTPROTO=none
NAME=$2
DEVICE=$2
ONBOOT=yes
MASTER=$3
SLAVE=yes
NM_CONTROLLED=no
EOF
   echo "Creating bond interface $3 file"
   echo
   cat << EOF > /etc/sysconfig/network-scripts/ifcfg-$3
DEVICE=$3
NAME=$3
TYPE=Bond
BONDING_MASTER=yes
IPADDR=$bondIp
PREFIX=$bondSubnet
ONBOOT=yes
BOOTPROTO=none
BONDING_OPTS="mode=4 miimon=100"
NM_CONTROLLED=no
EOF
   echo "Creation of the interface configuration files is done!!"
   echo
   echo "Bring up interfaces now!"
   sudo ifdown $1 && ifdown $2 && ifdown $3
   sudo ifup $1 && ifup $2 && ifup $3
   echo -e "Output of ip a \n"
   ip a
   echo -e "Done !!!! \n\n"
}

echo "User input for the interfaces which are part of bond interface"
echo "Bond interface name and IP Address"
read -p 'Interface 0: ' intf1
read -p 'Interface 1: ' intf2
read -p 'Bond interface name: ' bondIntfName
read -p 'Bond interface IP Address: ' bondIp
read -p 'Bond interface SubNetMask: ' bondSubnet

if [ -f /etc/lsb-release ]; then
   create_bond_on_ubuntu $intf1 $intf2 $bondIntfName $bondIp $bondSubnet
elif [ -f /etc/redhat-release ]; then
   create_bond_on_centos $intf1 $intf2 $bondIntfName $bondIp $bondSubnet
else
   echo "Unsupported OS for now !!!"
   EXITCODE=1
fi

exit $EXITCODE
