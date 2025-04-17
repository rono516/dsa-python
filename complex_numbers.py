import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)
    
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
    
    def __mul__(self, no):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)
    
    def __truediv__(self, no):
        # (a + bi)/(c + di) = ((ac + bd)/(c^2 + d^2)) + ((bc - ad)/(c^2 + d^2))i
        denominator = no.real**2 + no.imaginary**2
        if denominator == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        real = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(real, imaginary)
    
    def mod(self):
        # Modulus: sqrt(real^2 + imaginary^2)
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    # x = 4
    # y = 6
    # print(cmath.phase(complex(x,y)))