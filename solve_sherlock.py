def decode_char(char):
    replacements = {'!': 's', '@': 'h', '#': 'e', '$': 'r', '%': 'l', '^': 'o', '&': 'c', '*': 'k'}
    return replacements.get(char, char)

def decode_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    decoded_content = ''.join(map(decode_char, content))

    words_with_a = list(filter(lambda word: word.startswith('a'), decoded_content.split()))

    return words_with_a

# Functional version using list comprehensions
def decode_content_functional(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    decoded_content = ''.join(map(decode_char, content))

    words_with_a = [word for word in decoded_content.split() if word.startswith('a')]

    return words_with_a
