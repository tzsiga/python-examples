# lists

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

# sort array by values
nums = [3, 1, 2]
nums.sort()
print('sort:', nums)
cl.sort()
print('sort:', cl)

# reverse
lst.reverse()
print('reverse:', lst)
