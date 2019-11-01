#multithreaded.py
# Time taken in seconds - 3.853003978729248 for single thread
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
	while n>0:
		n-=1


t1 = Thread(target=countdown, args=(COUNT/2,))
t2 = Thread(target=countdown, args=(COUNT/2,))

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print('Time taken in seconds for 2 threads', end-start)
# Time taken in seconds for 2 threads 4.067925930023193

# in multithreaded version GIL prevented execution of two threads simultaneously
# but still then time should be at max = to above time (3.85)
# it is greater because of result of release and acquire overhead added by the lock