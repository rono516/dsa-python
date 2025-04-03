
import string as st

def minion_game(input_word):
    input_word = input_word.upper()
    
    vowels = {"A", "E", "I", "O", "U"}  # Using a set for O(1) lookup
    kevin_score = 0
    stuart_score = 0
    length = len(input_word)

    for i in range(length):
        if input_word[i] in vowels:
            kevin_score += length - i  # Kevin scores from vowel positions
        else:
            stuart_score += length - i  # Stuart scores from consonant positions

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)