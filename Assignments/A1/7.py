i_str = input('Input a string: ')
vowel = []
for x in i_str:
    if x == 'A' or x == 'a' or x == 'e' or x == 'E' or x == 'i' or x == 'I' or x == 'o' or x == 'O' or x == 'u' or x == 'U':
        if x in vowel:
            continue
        else:
            vowel.append(x)
print(vowel)
n = len(vowel)
print(f'There are {n} different vowels in the string.')
