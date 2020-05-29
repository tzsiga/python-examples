from utils import create_subtitle
from functools import reduce

# iterations
subtitle = create_subtitle('iterations')

# ----------
print(next(subtitle))

start = 1
end = 13
step = 2

for i in range(start, end, step):
    print(i)

# ----------
print(next(subtitle))

pos = [2, 5, 8, 13]
arr = range(20)

it = [arr[i] for i in pos]
print(it)

lst = ['foo', 'bar', 'baz']

for idx, item in enumerate(lst):
  print(idx, item)

# ----------
print(next(subtitle))

# functional list transforms

# map
words = 'foo barr ba azzzz'
lengths = list(map(lambda w: len(w), words.split()))
print('map', lengths)

# same with list comprehension
lengths_alt = [len(word) for idx, word in enumerate(words.split())]
print('map', lengths_alt)

# filter
longs = list(filter(lambda w: len(w) > 3, words.split()))
print('filter', longs)

# same with list comprehension
longs_alt = [word for idx, word in enumerate(words.split()) if len(word) > 3]
print('filter', longs_alt)

# reduce
# from functools import reduce
shortest = reduce((lambda x, y: x if x < y else y), lengths)
print('reduce', shortest)

# same with a simple loop
shortest_alt = lengths[0]
for l in lengths:
    shortest_alt = l if l < shortest_alt else shortest_alt
print('reduce', shortest_alt)

# ----------
print(next(subtitle))

m = min(len(x) for x in words.split())
print(m)

generated_list = [idx + len(item) for idx, item in enumerate(lst)]
print(generated_list)
