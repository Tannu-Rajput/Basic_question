import string
alpha = string.ascii_lowercase + string.ascii_uppercase

vowels = []
for i in alpha:
    if i in 'aeiouAEIOU':
        vowels.append(i)
print("Vowels in the alphabet:", vowels)  