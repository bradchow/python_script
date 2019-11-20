import threading
import time

stop_threads = False

# thread function
def job():
  for i in range(5):
    print ("Child thread:", i)
    time.sleep(1)
    if (stop_threads == True):
      break

# create thread
t = threading.Thread(target = job)

# start thread
t.start()

for i in range(2):
  print("Main thread:", i)
  time.sleep(1)
  stop_threads = True

# waiting for thread done
t.join()

print("Done.")