def switch_letters():
    letters = []
    
    str = input('pick a word ')
    index_one = int(input('index of first letter '))
    index_two = int(input('index of second letter '))


    new_str = ""

    for letter in str:
        letters.append(letter)
    
    char_at_index_one = letters[index_one]
    char_at_index_two = letters[index_two]

    letters[index_one] = char_at_index_two
    letters[index_two] = char_at_index_one

    for character in letters:
        new_str += character

    return new_str


print(switch_letters())


