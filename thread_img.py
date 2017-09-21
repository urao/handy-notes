import os
import sys
import subprocess
import threading
import Queue
import time

def worker(i, q):
   start = time.time()
   url = "http://x.x.x.x/images/jinstall-qfx-5-VX3714470006-domestic-img.tgz"
   p = subprocess.Popen(["curl","-s", url,"-o", "{}.txt".format(i)], stdout=None, stderr=None)
   p.communicate()
   exit_code = p.returncode
   if exit_code != 0:
      q.put((i, exit_code))
      return
   end = time.time()
   q.put((i, end-start))

queue = Queue.Queue()
threads = []
for i in range(int(sys.argv[1])):
   t = threading.Thread(target=worker, args=(i,queue))
   threads.append(t)
   t.start()

for t in threads:
   t.join()
   print "completed"

print "ThreadID\tTimeTaken"
while not queue.empty():
   thread_id, time_taken = queue.get()
   print str(thread_id) + "\t" + str(time_taken)
