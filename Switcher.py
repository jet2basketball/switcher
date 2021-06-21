
#converts a string into a list of its characters
def list_of_letters(word):
    letters = []

    for letter in word:
        letters.append(letter)

    return letters

#converts a list of characters into a string 
def list_to_string(list):
    new_str = ""

    for character in list:
        new_str += character
    
    return new_str


def swap_letters():

    index_one = 0
    index_two = 0

    word = input('Pick a word ')
    letters = list_of_letters(word)

    #finding index of first letter 
    letter_one = input('Pick a letter ')
    if letters.count(letter_one.lower()) > 1:
        indices = []

        for i in range(len(letters)):
            if letters[i] == letter_one.lower():
                indices.append(i)

        number = int(input('Which one(1,2,3,etc) '))

        index_one += indices[number - 1]

    else:
        index = letters.index(letter_one)
        index_one += index

    #finding index of second letter 
    letter_two = input('Pick another letter ')
    if letters.count(letter_two.lower()) > 1:
        indices = []

        for i in range(len(letters)):
            if letters[i] == letter_two.lower():
                indices.append(i)

        number = int(input('Which one(1,2,3,etc) '))
        index_two += indices[number - 1]

    else:
        index = letters.index(letter_two)
        index_two += index


    #swapping the two letters based on their index 
    letters[index_one] = letter_two
    letters[index_two] = letter_one

    #converting the list of characters back into a string
    updated_word = list_to_string(letters)

    return updated_word

print(swap_letters())


