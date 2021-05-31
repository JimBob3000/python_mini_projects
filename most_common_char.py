def get_most_common_char(sentence):
    characters = {}

    # Populate dictionary with each character and number of occurances
    for char in sentence:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    # Create ordered list using characters dictionary
    sorted_characters = sorted(
        characters.items(),
        key=lambda kv: kv[1],
        reverse=True)

    # Return most common character without number of occurances
    return sorted_characters[0][0]


print(f"The most common character is: '{get_most_common_char('The quick brown fox jumps over the lazy dog')}'")
