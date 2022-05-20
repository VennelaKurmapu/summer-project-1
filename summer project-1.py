import time
import threading
x = 0
def print_num(i):
    print(i)

endtime = time.time() + 1
while time.time() < endtime:
    t1 = threading.Thread(target = print_num, args=[x])
    x = x + 1
    t2 = threading.Thread(target = print_num, args=[x])
    x = x + 1
    t3 = threading.Thread(target = print_num, args=[x])
    x = x + 1
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()