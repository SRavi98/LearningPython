myString = 'Shailu'
for letter in myString:
    if letter == 'a':
        continue
    elif letter == 'i':
        print('y', end="\n")
    else:
        print(letter, end=" \n")