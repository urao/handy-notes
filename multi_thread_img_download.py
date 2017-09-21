#!/usr/bin/env python

import requests
import string
import random
import base64
import multiprocessing
import time
import re
import sys
import getopt

img_download_time = {}

def worker(url, tid):
  global img_download_time
  start = time.time()
  r = requests.get(url)
  if r.status_code == 200:
    filename = 'img_thread_%s' %tid
    with open(filename, "wb") as code:
      code.write(r.content)
      img_download_time[tid] = (time.time() - start)
      print ("Thread num %d--- %s seconds ---" %(tid, (time.time() - start)))


def usage():
  print("Usage: %s --nclients <clientnum> --serverip <ip> --imagename <img>" % sys.argv[0])


def main(argv):

  nclients = 1
  serverip = '127.0.0.1'
  found_arg = False
  imagename = 'jinstall-12.3R9.4-domestic-signed.tgz'

  try:
    opts, args = getopt.getopt(argv, "h:n:ip:img", ["help", "nclients=", "serverip=", "imagename="])
  except getopt.GetoptError as e:
    print (str(e))
    usage()
    sys.exit(2)

  for opt,arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-n", "--nclients"):
      found_arg = True
      nclients = int(arg)
    elif opt in ("-ip", "--serverip"):
      found_arg = True
      serverip = str(arg)
    elif opt in ("-img", "--imagename"):
      found_arg = True
      imagename = str(arg)

  if not found_arg:
    print "Either number of clients or server ip address or image name is not given"
    usage()
    sys.exit(2)

  print 'num of client connections to be simulated with server %s is %d to download image %s' % (serverip, nclients, imagename)

  #check if image exists on the server
  username = 'admin'
  password = 'admin'
  base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
  header = {'Authorization':'Basic %s' %base64string}

  #image_name = 'jinstall-qfx-10-f-15.2-20150421.0-domestic-img.tgz'
  get_url = "http://%s/images/" + imagename
  get_url_l = get_url %(serverip)

  r = requests.head(get_url_l, headers=header)
  if r.status_code != 200:
    print "Image does not exist on the server, please POST the image first, exiting now"
    sys.exit()

  jobs = []
  for i in range(nclients):
    p = multiprocessing.Process(target=worker, args=(get_url_l,i))
    jobs.append(p)
    p.start()


#main program
if __name__ == '__main__':
  main(sys.argv[1:])
