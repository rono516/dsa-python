from itertools import permutations as pt # type: ignore
import string as st

if __name__ == "__main__":
    allowed_letters = st.ascii_uppercase
    string, no_of_permutations = input().split()
    no_of_permutations = int(no_of_permutations)
    string = string.upper()
    string = sorted(string)
    string = "".join(string)
    for character in string:
        if character not in allowed_letters:
            string = string.replace(character,"")
    list_of_permutations = list(pt(string,int(no_of_permutations)))
    for permutation in list_of_permutations:
        for x in permutation:
            print(x,end="")
        print()
