def is_palindrome(word):
    odds = 0

    for letter in word:
        if word.count(letter) % 2 != 0:
            odds += 1

    if odds != 1:
        print False

    else:
        print True


is_palindrome("check")

is_palindrome("racecar")

is_palindrome("seeded")
