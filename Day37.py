def count_the_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            count += 1
    return count


word = "hello"
print(count_the_vowels(word))
