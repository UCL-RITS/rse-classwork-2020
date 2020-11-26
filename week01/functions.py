def jeeves(greeting="Very good", name="Sir"):
    return f"{greeting}, {name}"

print(jeeves())

print(jeeves("Hello"))

def double_inplace(vec):
    vec[:] = [element * 2 for element in vec]

z = list(range(4))
double_inplace(z)
print(z)

def extend(to, vec, pad):
    if len(vec) >= to:
        return #exit early list is long enough

    vec[:] = vec + [pad] * (to - len(vec)) 

x = list(range(3))
extend(6, x, 'a')
print(x)

z = range(9)
extend(6, z, 'a')
print(z)

def arrowify(**args):
    for key, value in args.items():
        print(f"{key} -> {value}")

arrowify(neutron='n', proton='p', electron='e')

def somefunc(a, b, *args, **kwargs):
    print("A:", a)
    print("B:", b)
    print("args:", args)
    print("keyword args", kwargs)

somefunc(1, 2, 3, 4, 5, fish="Haddock")