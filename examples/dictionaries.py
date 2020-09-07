from utils import create_subtitle

d = dict()

# (shallow!) copy
dict(d)

# dictionaries
subtitle = create_subtitle('dictionaries')

# ----------
print(next(subtitle))

# dictionary = js object like
words = { 'foo': 'FOO', 'bar': 'BAR' }

print(words.keys())
print(words.values())
print(words.items())
