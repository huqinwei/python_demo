from time import sleep
from time import time
t = time()
duration = 5
print("the time is ",t)
print("sleep , wakeup in ",duration,"seconds")
sleep(duration)
print("waked!")
t_new = time()
print("what's the time? ~is ",t_new)

sleep(1)
sleep(2)
#help(sleep)
