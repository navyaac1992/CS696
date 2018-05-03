"""
Exercise 8


1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float

2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 exercise_08.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 exercise_08.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument

"""
import sys
import argparse

def compute(**kwargs):

    numlist = kwargs['input']
    if kwargs['action'] == 'sum':
        if kwargs.get('return_float') == True:
            return float(sum(numlist))
        else:
            return sum(numlist)

    elif kwargs['action'] == 'mean':
        if kwargs.get('return_float') == True:
            return float(sum(numlist)/len(numlist))
        else:
            return sum(numlist)/len(numlist)


if __name__ == '__main__':
    print(compute(input=[1, 2, 3], action="mean", return_float=False))
    print(compute(input=[1, 2, 3], action='sum', return_float=True))
    print(compute(input=[1, 2, 3], action='mean'))

    parser = argparse.ArgumentParser(description='Finds some or product')
    parser.add_argument('-m', '--multiply', help='use -m for product', type=int)
    parser.add_argument('-s', '--sum', help='use -s for sum', action='store_true')
    parser.add_argument('remainder', help='remainder', nargs=argparse.REMAINDER)

    try:
        args = parser.parse_args()
        print(args)
        if args.sum:
            print('Sum:', sum(int(i) for i in args.remainder))
        else:
            print('Product:', [int(args.multiply) * int(x) for x in args.remainder])
    except:
        parser.print_help()
        sys.exit(1)
