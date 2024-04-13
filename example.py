import time

import timeIter


for i in range(10):
    timeIter.start()
    time.sleep(0.1)
    timeIter.measure("sleep")
    a = 2+4
    timeIter.measure("add")


timeIter.print_all()

timeIter.window()
