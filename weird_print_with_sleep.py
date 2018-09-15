from time import sleep
from time import time

def time_call(fn, arg):
    """Return the amount of time the given function takes (in seconds) when called with the given argument.
    """
    t_start = time()
    fn(arg)
    t_end = time()
    elapsed = t_end - t_start
    print("will return!")
    return elapsed
def do_sleep(t):
    sleep(t)
    

take_time = time_call(do_sleep,2)
print("wtf:",take_time)


time_call(sleep, 2)
#print("wtf!")
