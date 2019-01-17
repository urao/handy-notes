#!/usr/bin/env python
# Tested on Centos 7.4, works without changes for creating RHEL VMs
# Bring you run this script, install KVM packages using script
# https://github.com/urao/docker-k8s-project/blob/master/install_kvm.sh

import sys
import subprocess
import argparse
import shlex
import os


class BuildVM(object):

    def __init__(self, options):
        self.opt = options


    def create(self):
        """
        Create a new VM
        """
        f=open("create.log", mode='w')
        vm_name = str(self.opt.vm_name)+".qcow2"

        command = 'export LIBGUESTFS_BACKEND=direct'
        execute(command, f, ignore_errors=False)

        command = 'qemu-img create -f qcow2 -o preallocation=metadata'
        command += " " + vm_name + " "+ str(self.opt.vm_size)
        execute(command, f, ignore_errors=False)

        command = 'virt-resize --expand /dev/sda1'
        command += " " + str(self.opt.qcow2_file)+ " "+ vm_name
        execute(command, f, ignore_errors=False)

        command = 'virt-customize -a'
        command += " " + vm_name + " " + '--hostname' + " "+str(self.opt.vm_name)
        command += " " + '--timezone America/Los_Angeles --run-command \'xfs_growfs /\' --root-password'
        command += " " + 'password:' + str(self.opt.vm_passwd) 
        command += " " + '--run-command \'sed -i "s/PasswordAuthentication no/PasswordAuthentication yes/g"'
        command += " " + '/etc/ssh/sshd_config\' --run-command \'systemctl enable sshd\' --run-command \'yum remove -y cloud-init\' --selinux-relabel' 
        execute(command, f, ignore_errors=False)

        command = 'mv '
        command += vm_name
        command += " " + '/var/lib/libvirt/images/'
        execute(command, f, ignore_errors=False)

        command = 'virt-install'
        command += " " + '--name' + " "+str(self.opt.vm_name)
        command += " " + '--ram' + " "+str(self.opt.vm_mem)
        command += " " + '--vcpus' + " "+str(self.opt.vm_cpus)
        command += " " + '--os-variant rhel7'
        command += " " + '--disk ' + '/var/lib/libvirt/images/'+vm_name 
        command += " " + '--network network=default,model=virtio'
        command += " " + '--virt-type kvm --import --graphics vnc --serial pty --noautoconsole' 
        command += " " + '--console pty,target_type=virtio'
        execute(command, f, ignore_errors=False)

        command = 'virsh domifaddr '+str(self.opt.vm_name)
        res = execute(command, f, ignore_errors=False)
        print 'IP address of the VM: '
        print res
        f.close()

    def delete(self):
        """
        Delete a VM
        """
        f=open("delete.log", mode='w')
        command = 'virsh destroy '+str(self.opt.vm_name)
        execute(command, f, ignore_errors=False)
        command = 'virsh undefine '+str(self.opt.vm_name)
        execute(command, f, ignore_errors=False)
        command = 'rm -rf /var/lib/libvirt/images/'+vm_name
        execute(command, f, ignore_errors=False)
        f.close()



# Utility functions
def cmd_exists(cmd):
    return subprocess.call("type "+ cmd, shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def execute(cmd, output, ignore_errors=False):

    pipe = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, close_fds=True)
    data = ""
    for line in pipe.stdout:
        output.write(line)
        output.flush()
        data += line

    rc = pipe.wait()
    cwd = os.getcwd()
    if rc and not ignore_errors:
        print 'Error : Working directory : %s' % (cwd)
        print 'Error : Failed to execute command: %s\n%s' %(cmd, data)
        sys.exit(1)
    return data.strip()

def parse_options(args):

    parser = argparse.ArgumentParser(description='Create OR Delete a VM on KVM host')

    parser.add_argument('-i', '--image', nargs='?', dest='qcow2_file',
                        help='QCOW2 file location.')

    parser.add_argument('-s', '--size', nargs='?', dest='vm_size',
                        help='Disk size of the VM.')

    parser.add_argument('-n', '--name', nargs='?', dest='vm_name',
                        help='Name of the VM.')

    parser.add_argument('-p', '--passwd', nargs='?', dest='vm_passwd',
                        help='Root password of the VM.')

    parser.add_argument('-c', '--vcpus', nargs='?', dest='vm_cpus',
                        help='vCPUs of the VM.')

    parser.add_argument('-r', '--ram', nargs='?', dest='vm_mem',
                        help='Memory of the VM.')

    subparsers = parser.add_subparsers(title='BuildVM Commands',
                                      description='Select one action',
                                      dest='command')
    parser_create = subparsers.add_parser('create', description='Create a VM')
    parser_delete = subparsers.add_parser('delete', description='Delete a VM')
    
    opt = parser.parse_args(args)
    return opt


if __name__=='__main__':
    options = parse_options(sys.argv[1:])

    vm = BuildVM(options)

    if not cmd_exists("qemu-img"):
        print "Missing qemu-img command"
        sys.exit(1)

    if not cmd_exists("virt-resize"):
        print "Missing virt-resize command"
        sys.exit(1)

    if not cmd_exists("virt-customize"):
        print "Missing virt-customize command"
        sys.exit(1)

    if not cmd_exists("virt-install"):
        print "Missing virt-install command"
        sys.exit(1)

    if not cmd_exists("virsh list --all"):
        print "Missing virsh command"
        sys.exit(1)

    if vm.opt.command == 'create':
        vm.create()
        sys.exit(0)

    if vm.opt.command == 'delete':
        vm.delete()
        sys.exit(0)

    print "Unknown command: ", vm.opt.command
    sys.exit(1)
