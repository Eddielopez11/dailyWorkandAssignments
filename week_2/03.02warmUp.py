

def plus(one, tow):
    return one + tow

print(plus(2,3))

def power(x,y):
    if y == 1:
        return x
    else:
        return x ** y

print(power(4,2))
print(power(4,1))

assert power(2,2) == 4
assert power(3,3) == 27
assert power(-4,2) == 16

def join_words(l):
    return " ".join(l)

print(join_words(['Hello', 'my', 'name', 'is', 'Nibor']))
