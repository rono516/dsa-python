from cmath import phase

if __name__ == "__main__":
    number = input()
    polar = phase(complex(number))
    absolute = abs(complex(number))
    print(absolute)
    print(polar)