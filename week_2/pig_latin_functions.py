# pig latin functions

def piggify_word(pl):
    piglatin = []
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    if pl[0] not in vowels:
        for l in pl[1: ]:
            piglatin.append(l)
        piglatin.append(pl[0] + 'ay')
    elif len(pl) <= 1:
        piglatin.append(pl[0] + 'say')
    else:
        piglatin.append(pl[1:] + 'say')

    return ''.join(piglatin)

print(piggify_word('allowance'))

assert piggify_word("hello") == "ellohay"
assert piggify_word("goodbye") == "oodbyegay"
assert piggify_word("allowance") == "llowancesay"
assert piggify_word("I") == "Isay"
