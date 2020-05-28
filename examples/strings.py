from utils import create_subtitle, print_methods

# strings
subtitle = create_subtitle('strings')

# ----------
print(next(subtitle))

print_methods(str)

# ----------
print(next(subtitle))

# split string by spaces
print('foo bar baz'.split())

# split string to characters
print(list('foo'))

# trim string
print(len('foo     '))
print(len('foo     '.rstrip()))
print(len('   foo  '.strip()))

# casing
print('fooOOoo'.lower())
print('fooOOoo'.upper())
print('fooOOoo'.title())

# isdigit
print('13'.isdigit())
