from textblob import Word


def spelling_checker(word):
    correct_word = Word(word).correct()
    if correct_word == word:
        return word
    else:
        answer = input(
            "Did you mean to type '{}'? Enter Y for yes or N for no: ".format(correct_word))
        if answer.lower() == 'y':
            return correct_word
        else:
            return spelling_checker(input("Please enter the correct spelling: "))
