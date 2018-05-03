"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math


def decorater(my_function):
    def inner_function():
        t0 = time.time()
        d0 = time.process_time()
        result = my_function()
        t1 = time.time()
        d1 = time.process_time()
        time_diff = t1 - t0
        process_time_diff = d1 - d0
        print("Inner function")
        print("Real World Time Taken:{}  Process Time Taken:{}  Size of Return Value:{}".format(str(time_diff),str(process_time_diff * 1000),str(sys.getsizeof(result))))
        findingLogTen(result)
        return result
    return inner_function


def findingLogTen(myfunc):
    def wrapper():
        res = myfunc()
        logval = [math.log10(i) for i in res]
        print("Log 10 value : {}".format(logval))
        return logval
    return wrapper


@decorater
@findingLogTen
def for_loop():
    print("For loop : ")
    sample_list = []
    for x in range(1,1000000):
        sample_list.append(x)
    return sample_list


@decorater
@findingLogTen
def list_comp():
    print("List Comp : ")
    sample_list = [x for x in range(1,1000000)]
    return sample_list


@decorater
@findingLogTen
def numpy_list():
    print("Numpy list : ")
    sample_list = numpy.arange(1,1000000)
    return sample_list


@decorater
@findingLogTen
def pandas_list():
    print("Pandas List : ")
    sample_data = numpy.arange(1,1000000)
    return pandas.DataFrame(sample_data).values


@decorater
@findingLogTen
def generator_list():
    print("Generator list : ")
    sample_list = (x for x in range(1,1000000))
    return sample_list


for_loop()
list_comp()
numpy_list()
pandas_list()
generator_list()