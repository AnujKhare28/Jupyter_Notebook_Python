from threading import * 
from time import *

def display(str1):
    s.acquire()
    for i in str1:
        print(i)
        sleep(0.3)
    s.release()

s = Semaphore(1)

t1 = Thread(target=display, args=('Hello World',))
t2 = Thread(target=display, args=(' You are welcome',))
t3 = Thread(target=display, args=(' This is Python Programming',))
t4 = Thread(target=display, args=(' 0123456789',))
t5 = Thread(target=display, args=(' Thank You',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()