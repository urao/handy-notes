#!/usr/bin/env python
# Tested on MacOS

import sys
import argparse
import os
import time

class OpenBrowser(object):

    def __init__(self, options):
        self.opt = options
        self.appPath = '/Applications/Google\ Chrome.app'

    def contrail(self):
        """
        Open Contrail WebUI
        """
        url = 'https://'+ str(self.opt.ipaddr)+':8143'
        
        try: 
            driver = webdriver.Chrome(executable_path=self.driverPath)
        except WebDriverException:
            print("Failed to start driver at "+ self.driverPath)

        driver.implicitly_wait(30) # seconds
       
        #url = 'https://rankade.com/'
        driver.get(url)
        time.sleep(15)
        #assert 'rankade' in driver.title
        #driver = webdriver.Chrome(capabilities=capabilities)

    def openstack(self):
        """
        Open OpenStack UI
        """
        url = 'http://'+ str(self.opt.ipaddr)+':8143'
        print "URL:"+url


def execute(cmd, output, ignore_errors=False):

    print cmd
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

    parser = argparse.ArgumentParser(description='Login to Contrail WebUI')
    parser.add_argument('-i', '--ipaddr', nargs='?', dest='ipaddr',
                        help='Controller IP Address.')
    parser.add_argument('-u', '--username', nargs='?', dest='username',
                        help='Controller username.')
    parser.add_argument('-p', '--password', nargs='?', dest='passwd',
                        help='Controller password.')
    subparsers = parser.add_subparsers(title='OpenBrowser Commands',
                                      description='Select one action',
                                      dest='command')
    parser_create = subparsers.add_parser('contrail', description='Open Contrail UI')
    parser_delete = subparsers.add_parser('openstack', description='Open Openstack Horizon UI')
    opt = parser.parse_args(args)
    return opt


if __name__=='__main__':
    options = parse_options(sys.argv[1:])

    browser = OpenBrowser(options)

    if browser.opt.command == 'contrail':
         browser.contrail()

    if browser.opt.command == 'openstack':
         browser.contrail()
         sys.exit(0)

    #print "Unknown command: ", browser.opt.command
    #sys.exit(1)
