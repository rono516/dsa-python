import string as st
def minion_game(input_word):
    input_word = [letter.capitalize() for letter in input_word]
    vowels = ["A", "E", "I", "O", "U"]
    consonants = list(letter for letter in st.ascii_uppercase if letter not in vowels )
    # print(input_word)
    kevins_vowel_words = [word for word in input_word if word not in consonants]
    kevins_consonant_words = [word for word in input_word if word in consonants]

    print(kevins_consonant_words)

if __name__ == '__main__':
    s = input()
    minion_game(s)