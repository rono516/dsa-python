#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    letters_in_name = [n.capitalize() for n in s.split(" ")] 
    word = " ".join(letters_in_name)
    print(word)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
