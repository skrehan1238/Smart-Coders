#
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Two real roots: {root1:.2f}, {root2:.2f}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One repeated real root: {root:.2f}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-discriminant) / (2*a)
    print(f"Complex roots: {real:.2f} + {imag:.2f}i, {real:.2f} - {imag:.2f}i")
