import string


def check_pangram(stre):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in stre.lower():
            return False
    return True


stringmax = "a quick brown fox jumps over the lazy dog"
print(check_pangram(stringmax))
