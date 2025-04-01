import string as st
def minion_game(input_word):
    input_word = input_word.upper()
    # print(input_word)
    input_word_letters = [letter.capitalize() for letter in input_word]
    vowels = ["A", "E", "I", "O", "U"]
    consonants = list(letter for letter in st.ascii_uppercase if letter not in vowels )
    # print(input_word)
    kevins_vowel_words = list(set(word for word in input_word_letters if word not in consonants))
    stuarts_consonant_words = list(set(word for word in input_word_letters if word in consonants))

    kevins_vowel_words =kevins_vowel_words + [vowel+consonant+vowel+consonant+vowel for vowel in kevins_vowel_words for consonant in stuarts_consonant_words if input_word.find(vowel+consonant) != -1  ]
    print(kevins_vowel_words)

if __name__ == '__main__':
    s = input()
    minion_game(s)