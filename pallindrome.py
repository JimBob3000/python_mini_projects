def is_pallindrome(word):
    reversed_word = ''.join(reversed(word))

    if word == reversed_word:
        return True
    return False


pallindrome = "racecar"
print(f"Is {pallindrome} a pallindrome: {is_pallindrome(pallindrome)}")
