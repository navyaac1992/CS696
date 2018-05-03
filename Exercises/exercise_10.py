"""
Exercise 10 - Generators

For this exercise you will be writing a class for several different generator functions.

1) Write a class called "Gens".
    - This class is initialized with a single integer that is called "start"
    - Include a __str__() method so that when an instance of your class is printed, the returned string includes the value of "start"
        EX: "Start value for generators class is: 5"
    - All generator methods should start at the "start" value, if one is not provided, the class should default to a start value of 1

2) Include in this class, the following methods:
    doubles() - yields number * 2 to infinity, starting at self.start
        Gens(1).doubles() -> 1, 2, 4, 8, 16, ...

    fib() - Yields the next number in the fibonacci sequence to infinity, starting at 1
        Gens(100).fib() -> 1, 1, 2, 3, 5, 8, ...

    linear(n) - yields number + n to infinity, starting at self.start
        Gens(1).linear(2) -> 1, 3, 5, 7, 9, ...

    exponential(n) - yields number raised to the power n to infinity, starting at self.start
        Gens(2).exponential(2) -> 2, 4, 16, 256, ...

    sequence(list) - Ignores starting number, yields one value at a time in the list, looping infinitely many times
        Gens(0).sequence([2, 3, 4]) -> 2, 3, 4, 2, 3, 4, ...

    triple_half() -  Yields a number * 3, then the number / 2, repeating to infinity, starting at self.start
        Gens(2).triple_half() -> 2, 6, 3, 9, 4.5, 13.5, ...

"""


class Gens:
    def __init__(self, start=1):
        self.start = start

    def __str__(self):
        return "Start value for generators class is:" + str(self.start)

    def doubles(self):
        val = self.start
        while True:
            val *= 2
            yield val

    def fib(self):
        previous_value = 0
        current_value = self.start

        while True:
            yield current_value
            previous_value, current_value = current_value, previous_value + current_value

    def linear(self, num):
        value = self.start
        while True:
            yield value
            value = value + num

    def exponential(self, num):
        value = self.start
        while True:
            yield value
            value = value ** num

    def sequence(self, sample_list):
        value = self.start
        while True:
            yield sample_list[value]
            value= value +1


    def triple_half(self):
        value = self.start
        while True:
            yield value
            value = (value * 3) / 2


print(next(Gens(1).doubles()))
print(next(Gens(1).fib()))
print(next(Gens(1).exponential(2)))
print(next(Gens(1).sequence([10,20,30])))
print(next(Gens(10).triple_half()))
