#!/usr/bin/env bash
# Tested on Ubuntu 16.04.2

set -eux

EXITCODE=0

function install_on_ubuntu () {
   echo "Installing VNC pkgs on Ubuntu"
   sudo apt-get install --no-install-recommends ubuntu-desktop gnome-panel gnome-settings-daemon -y
   sudo apt-get install --no-install-recommends metacity nautilus gnome-terminal gnome-core -y
   sudo apt-get install vnc4server -y
   echo -e "Done !!!! \n\n"
}

function install_on_centos () {
   echo "Installing VNC pkgs on Centos"
   echo -e "Done !!!! \n\n"
}

if [ -f /etc/lsb-release ]; then
   install_on_ubuntu 
elif [ -f /etc/redhat-release ]; then
   install_on_centos 
else
   echo "Unsupported OS for now !!!"
   EXITCODE=1
fi

exit $EXITCODE
