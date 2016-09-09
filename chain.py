from fmap import FuncMap, FrozenFunction

chain1 = FuncMap(val='Michael')
chain2 = FuncMap(val='b')

@chain1
def a(stdin, link=None):
    if link:
        href = ' extra=' + link
    else:
        href = ''
    return '<a' + href + '>' + stdin + '</a>'


@chain1
@chain2
def b(stdin):
    return '<strong>' + stdin + '</strong>'

@chain2
def c(stdin):
    return stdin + '<br>' + stdin

print(chain1.id)
print(chain2.id)
print(chain1.call([{'link': 'Michael'}, None, None]))
print(chain2.call())
