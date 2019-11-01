# each python process gets its own Python interpreter
# and memory space so the GIL won't be a problem.

from multiprocessing import Pool
import time

CNT = 50000000
def countdown(n):
	while n>0:
		n-=1

if __name__ == '__main__':
	pool = Pool(processes=2)
	start = time.time()
	r1 = pool.apply_async(countdown, [CNT/2])
	r2 = pool.apply_async(countdown, [CNT/2])
	pool.close()
	pool.join()
	end = time.time()
	print('Time taken in seconds', end-start)