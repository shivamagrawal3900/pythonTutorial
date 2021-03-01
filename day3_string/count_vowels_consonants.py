a1 = input("Enter a string: ")

vowel_count = 0
consonant_count = 0
other_count = 0

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

for character in a1:
    if character in vowels:
        vowel_count += 1
    elif character in consonants:
        consonant_count += 1
    else:
        other_count += 1

print("Length of string:", len(a1))
print("Vowels count:", vowel_count)
print("Consonant count:", consonant_count)
print("Others count:", other_count)
