### Steps to create pool-storage if you are running out of space in /

1) Following steps ran on Centos 7
``` 
mkdir -p /home/images
chown root:root /home/images
virsh pool-define-as home_images --type dir --target /home/images/
virsh pool-start home_images
virsh pool-list
virsh pool-autostart home_images
ln -s /home/images /var/lib/libvirt/images
```
