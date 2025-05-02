from math import atan, degrees
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    hypotenuse = a*a + b*b
    adjacent_angle = degrees(atan(a/b))
    our_angle = 90 - adjacent_angle
    our_angle = round(our_angle)
    print(f"{our_angle}\u00B0")
