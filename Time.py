import time
from Cat import Cat
from SmallCat import SmallCat
from BigCat import BigCat

def Timer(f):
    def func(*args, **kwargs):
        currtime = time.time()
        result = f(*args, ** kwargs)
        print ("Время выполнения = %f" % (time.time() - currtime) )
        return result

    return func

smallcat = SmallCat()
bigcat = BigCat()

@Timer
def measure_time(f):
    print(f)


measure_time(smallcat.et_eat())
measure_time(smallcat.et_sleep())
measure_time(smallcat.et_run())
measure_time(bigcat.et_eat())
measure_time(bigcat.et_sleep())
measure_time(bigcat.et_run())
