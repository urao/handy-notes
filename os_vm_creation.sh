#!/bin/env bash
set -e

source .op/bin/activate
source /etc/kolla/kolla-toolbox/admin-openrc.sh
echo "VN name: $1"
VN_NAME=$1
NET_ID=`openstack network list | grep ${VN_NAME} | awk -F '|' '{print $2}' | tr -d ' '`
echo "VN UUID: $NET_ID"

echo "Boot cirros VM with net-id: $NET_ID and name: $2"
nova boot --image cirros --flavor small --nic net-id=$NET_ID $2
sleep 10s

openstack server list
