from string import Template

# generator function
def create_subtitle(section):
    title = Template('\n$section example $i')
    i = 0
    while True:
        i += 1
        yield title.substitute(section=section, i=i)
