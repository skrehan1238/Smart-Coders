#
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(f"{c}°C = {f}°F")

f2 = float(input("Enter temperature in Fahrenheit: "))
c2 = (f2 - 32) * 5/9
print(f"{f2}°F = {c2:.2f}°C")
