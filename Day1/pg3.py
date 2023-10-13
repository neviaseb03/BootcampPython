def countofvowandconst(text):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count

input_string = input("Enter a string: ")

vowels, consonants = countofvowandconst(input_string)


print("Total characters:", len(input_string))
print("Vowels:", vowels)
print("Consonants:", consonants)
