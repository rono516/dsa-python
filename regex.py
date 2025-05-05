import re
import string

def check_if_float(float_no):
    is_float = True
    all_numbers = string.digits

    allowed_starting_characters = [number for number in all_numbers]+ [".", "+", "-" ]

    for value in float_no:
        if value not in allowed_starting_characters:
            is_float = False

    if bool(re.search(r"\.", str(float_no))) == False:
        is_float = False
    try:
        float(float_no)
    except Exception:
        is_float = False

    return is_float

if __name__ == "__main__":
    strings_to_check = []

    number_of_inputs = int(input())
    for i in range(number_of_inputs):
        string_to_check = input()
        strings_to_check.append(string_to_check)

    for string_to_check in strings_to_check:
        is_float = check_if_float(string_to_check)

        print(is_float)
# detecting floating number https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
        


