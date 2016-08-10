# pig latin functions

def piggify_word(pw):
    pigword = []
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    if pw[0] not in vowels:
        for l in pw[1: ]:
            pigword.append(l)
        pigword.append(pw[0] + 'ay')
    elif len(pw) <= 1:
        pigword.append(pw[0] + 'say')
    else:
        pigword.append(pw[1:] + 'say')

    return ''.join(pigword)

print(piggify_word('eddie'))
print(piggify_word('lopez'))

assert piggify_word("hello") == "ellohay"
assert piggify_word("goodbye") == "oodbyegay"
assert piggify_word("allowance") == "llowancesay"
assert piggify_word("I") == "Isay"

def piggify_string(ps):
    pigstring = ps
    pigstringL = pigstring.split()
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for word in pigstringL:
        if word[0] not in vowels:
            for l in word[1: ]:
                pigstringL.append(l)
            pigstringL.append(word[0] + 'ay')
        elif len(word) <= 1:
            pigstringL.append(word[0] + 'say')
        else:
            pigstringL.append(word[1:] + 'say')

        return ' '.join(pigstringL)

print(piggify_string('python pig latin is not fun a all'))
