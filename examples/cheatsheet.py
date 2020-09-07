# python cheatsheet
# =================

# style guide
# https://www.python.org/dev/peps/pep-0008/

# base types
# string, number, boolean, list, tuple, dict

global x
x = 13

# type conversion
type(int('13'))

dir(list)                                   # list available methods on object
help(list.copy)                             # display help of something
type(13)                                    # get type name of something
callable(obj)                               # check if obj is a function

all(iterable)                         # True if all elements of the iterable are true
any(iterable)                         # True if any element of the iterable is true

reversed(iterable)                          # return a reverse iterator
sorted(iterable, key)                       # sort iterable by key sorting fn

abs(iterable)
max(iterable)
min(iterable)
sum(iterable)

raise TypeError('Error description here')   # throw exception

a if condition else b                       # ternary expression
'', 0, 0.0, 0j, [], (), {}, False, None     # falsy values

'foo bar baz'.split()                       # split string by spaces
list('FooOOOo')                             # split string by characters
'   foo  '.strip()                          # trim string
'fooOOoo'.lower()                           # transformations
'fooOOoo'.upper()
'fooOOoo'.title()                           # sentence case
'13'.isdigit()                              # check if string means a number
'Foo'.startswith('F')                       # check first character
'{:02d}'.format(8)                          # leading zero

lst = ['foo  ', 'bar ', 'baz']
len(lst)                                    # length of list
lst.append('foo2')
lst.pop()
lst.copy()
lst.reverse()
lst.sort(reverse=True)                      # in-place!
sorted(lst, key=lambda w: len(w))
'foo' in lst                                # check value in list
lst1 + lst2                                 # concat lists

tpl = ('foo',)                              # tuple with one element
tpl2 = ('foo', 'bar')
len(tpl2)
(6, 7, 8) + (9, 10)                         # concat tuples

words = { 'foo': 'FOO', 'bar': 'BAR' }
words.keys()
words.values()
words.items()
'key1' in dct                               # check key in collection
'one' in dct.values()                       # check value in collection

range(length)
range(start, end, step)

import numpy as np                          # for advanced calculations

import random
random.random()                             # give a random number in [0, 1)
random.uniform(start, end)                  # random number in [start, end)
random.normalvariate(mean, deviation)       # random number by normal distr
random.randint(start, end)                  # random int from range
random.choice(['rock', 'paper', 'scissors'])  # random element from a list

for i in lst:
for idx, item in enumerate(lst):

for _ in range(2):
  print(_)

for x in [0,1,2]:                           # for - else
    if x == 3:
        break
else:
    print("not found")

list(map(lambda w: len(w), lst))            # list mapping with lambda
[len(w) for w in lst]                       # same with list comprehension

list(filter(lambda w: len(w) > 3, lst))     # filter
[w for w in lst if len(w) > 3]              # same with list comprehension

from functools import reduce                # reduce
reduce((lambda x, y: x if x < y else y), lst)

lambda x, y = 13: x + y                     # lambda with default argument value
def fn(n, pow=2):                           # function with named param
  return n ** pow
b(pow=3, n=3)

def something(first: str, second: int) -> str:
	'''
    help text here
  '''
	return first + second                     # help text

something(second=13, first="foo")           # named arguments

def getTuple(first: str, second: int) -> tuple:
	return first, second                      # return multiple values

class SampleClass:                          # class
  def __init__(self, arr):
    self.arr = arr

  def arrLength(self):
    return len(self.arr)

import datetime
import math

import re                                   # regex
match_obj = re.search(r'[1-9]', 'input 123')
value = match_obj.group()

# read files
with open(file_to_read) as infile:
  for index, line in enumerate(infile):
    print(index, line)

# serialize everything
import pickle

with open("dump.pkl", "wb") as f:
	pickle.dump(something, f)
