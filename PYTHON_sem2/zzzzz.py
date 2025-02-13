import threading
import time
t=time.time()
def func(s):
    print(f"sleeping for {s} seconds")
    time.sleep(s)
t1=threading.Thread(target=func,args=(4,))
t2=threading.Thread(target=func,args=(2,))
t3=threading.Thread(target=func,args=(1,))
t1.start()
t1.join()
t2.start()
t3.start()
print(threading.Thread_count)
t3.join()
t2.join()

print(time.time()-t)