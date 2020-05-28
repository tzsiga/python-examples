from string import Template

# generator function
def create_subtitle(section):
    title = Template('\n$section example $i')
    i = 0
    while True:
        i += 1
        yield title.substitute(section=section, i=i)

def print_methods(fn):
    methods = list(filter(lambda m: m[0] != '_', dir(fn)))
    print('Methods of "' + fn.__name__ + '":')
    [print('  ' + m) for m in methods]
