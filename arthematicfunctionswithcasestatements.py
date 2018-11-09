def switch_function(value, p,q):
    return {
        'a': lambda p: p+q,
        'm': lambda p: p*q,
        's': lambda p: p-q,
        'd': lambda p: p/q
    }.get(value)(p)

inp = input('operation Character as Input: ')

print('obtained result  : ', switch_function(inp, 5,10))
