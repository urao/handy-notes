## Steps to create an image from OpenStack instance
1) openstack server list
2) openstack server stop <instance_name>
3) nova image-create --poll <instance_name> <instance_name_snapshot>
4) glance image-download --file <image_name>.qcow2 <UUID_of_snapshot>
5) Get UUID_of_snapshot using \"glance image-list\"
