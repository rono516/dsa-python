from itertools import product # type: ignore
if __name__ == "__main__":
    first_input = input("Two first values ")
    second_input = input("Second first values ")
    A = list(map(int, first_input.split()))
    B = list(map(int, second_input.split()))
    output = list(product(A,B))
    for solution in output:
        print(solution, end=" ") # type: ignore