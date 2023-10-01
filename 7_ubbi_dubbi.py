def ubbi_dubbi(word):
    new_word = ''
    for c in word:
        if c in 'aeiou':
            new_word += f'ub{c}'
        else:
            new_word += c


    return ''.join(new_word)

print(ubbi_dubbi("octopus"))
print('correct = ', ubbi_dubbi("octopus") == 'uboctubopubus')

print(ubbi_dubbi("elephant"))
print('correct = ', ubbi_dubbi("elephant") == 'ubelubephubant')

