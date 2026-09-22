#
# Uses the heart curve formula: (x^2 + y^2 - 1)^3 - x^2*y^3 <= 0
for y in range(15, -15, -1):
    yy = y / 10
    row = ""
    for x in range(-15, 16):
        xx = x / 10
        val = (xx**2 + yy**2 - 1)**3 - (xx**2) * (yy**3)
        row += "*" if val <= 0 else " "
    print(row)
