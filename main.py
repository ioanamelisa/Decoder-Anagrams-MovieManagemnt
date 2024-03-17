from solve_sherlock import decode_content
from second_assignment import find_meaningful_anagrams
from third_assignment import switch_menu

def main():
    #first assigment
    file_path = 'sherlock.txt'
    decoded_words = decode_content(file_path)
    print("First assignment result:", decoded_words)

    #second assigment
    user_input = input("\nSecond assignment/ Enter a word: ")
    dictionary_path = 'dictionary.txt'
    result = find_meaningful_anagrams(user_input, dictionary_path)
    print("The meaningful anagrams:", result)

    #third assigment
    switch_menu()


if __name__ == "__main__":
    main()
