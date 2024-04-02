def count_vowels(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count

input_text = input("Enter some text: ")
print("Number of vowels:", count_vowels(input_text))
