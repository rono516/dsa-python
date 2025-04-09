from itertools import combinations as cb

if __name__ == "__main__":
    string, no_of_combinations = input().split(" ")
    string = string.upper()
    string = sorted(string)

    string = "".join(string)

    no_of_combinations = int(no_of_combinations)
    result_combinations = []

    for i in range(1, no_of_combinations+1):
        result_combinations +=  list(cb(string, i))
    for combination in result_combinations:
        for x in combination:
            print(x, end="")
        print()




