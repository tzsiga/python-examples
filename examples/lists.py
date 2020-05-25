# lists

# list (array)
arr = ['foo', 'bar']
print('list:', arr)
print('type:', type(arr))

# length
print('length:', len(arr))

# add new item to end
arr.append('baz')
print('append:', arr)

# pick last item
print('pop:', arr.pop())
print(arr)

# check value in array
print('includes:', 'foo' in arr)

# clone array
cl = arr.copy()
print('clone:', cl)

# sort array by values
nums = [3, 1, 2]
nums.sort()
print('sort:', nums)
cl.sort()
print('sort:', cl)

# reverse
arr.reverse()
print('reverse:', arr)
