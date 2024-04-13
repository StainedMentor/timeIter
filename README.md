## A simple python package for profiling loops
This package was made in order to easily show how much time each element in a loop takes. It is made with the tought of having to use the least amount of code in order to measure segment execution time in iterative processes.

## Usage
The package contains 3 main functions to use. *timeIter.start()* resets the clock. *timeIter.measure("key_name")* adds the time since last measurement or start to the specifed key. *timeIter.print_all()* prints min,max,average data for every specified key.
```python
import time
import timeIter

for i in range(10):
    timeIter.start()
    time.sleep(0.1)
    timeIter.measure("sleep")
    a = 2+4
    timeIter.measure("add")

timeIter.print_all()
```
