from utils import create_subtitle, print_methods

# lists
subtitle = create_subtitle('lists')

# ----------
print(next(subtitle))

print_methods(list)

# ----------
print(next(subtitle))

# list (array)
lst = ['foo', 'bar']
print('list:', lst)
print('type:', type(lst))

# length
print('length:', len(lst))

# add new item to end
lst.append('baz')
print('append:', lst)

# pick last item
print('pop:', lst.pop())
print(lst)

# check value in array
print('includes:', 'foo' in lst)

# clone array
cl = lst.copy()
print('clone:', cl)

# sort array by values, .sort is in-place!
nums = [3, 1, 2]
nums.sort()
print('sort:', nums)
cl.sort(reverse=True)
print('sort:', cl)

# sort with sorted()
sentence = 'foo 1 bar 2 baz'
print('sorted', sorted(sentence.split(), key=lambda w: len(w)))

# reverse
lst.reverse()
print('reverse:', lst)

# concat lists
print(nums + lst)
print([*nums, *lst])

# ----------

# tuples
subtitle = create_subtitle('tuples')

# ----------
print(next(subtitle))

print_methods(tuple)

# ----------
print(next(subtitle))

print((1, 2, 3))
print((4))
print((5,))

print(len((1, 2, 3, 4, 5)))

print((6, 7, 8) + (9, 10))
