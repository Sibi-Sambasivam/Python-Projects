def pig_latin(word):
    vowels = 'aeiou'
    if word[0].lower() in vowels:
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

input_word = input("Enter a word: ")
print("Pig Latin:", pig_latin(input_word))
