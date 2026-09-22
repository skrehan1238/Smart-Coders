#
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
# Alternative: print(n * (n + 1) // 2)
