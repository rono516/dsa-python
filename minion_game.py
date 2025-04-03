import string as st

def award_points(words, input_word): 
    count = 0
    for word in words:
        start = 0
        while True:
            start = input_word.find(word , start)
            if start == -1:
                break
            count +=1
            start +=1
    return count
def minion_game(input_word):
    input_word = input_word.upper()
    
    # print(input_word)
    input_word_letters = [letter.capitalize() for letter in input_word]
    vowels = ["A", "E", "I", "O", "U"]
    consonants = list(letter for letter in st.ascii_uppercase if letter not in vowels )
    # print(input_word)
    kevins_vowel_words = list(set(word for word in input_word_letters if word not in consonants))
    stuarts_consonant_words = list(set(word for word in input_word_letters if word in consonants))

    kevins_vowel_words =  list(set(
        input_word[i:j] 
        for i in range(len(input_word)) 
        for j in range(i + 1, len(input_word) + 1) 
        if input_word[i] in kevins_vowel_words
    ))
    stuarts_consonant_words =  list(set(
        input_word[i:j] 
        for i in range(len(input_word)) 
        for j in range(i + 1, len(input_word) + 1) 
        if input_word[i] in stuarts_consonant_words
    ))

    kevin_points = award_points(words=kevins_vowel_words,input_word=input_word)
    stuart_points = award_points(words=stuarts_consonant_words,input_word=input_word)

    if kevin_points > stuart_points:
        print(f"Kevin {kevin_points}")
    elif stuart_points> kevin_points:
        print(f"Stuart {stuart_points}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)