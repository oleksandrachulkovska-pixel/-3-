a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

L = min(a, b)
R = max(a, b)

S = 0

for x in range(L + 1, R):
    if x % 2 != 0:
        S += x

print("Сума непарних чисел:", S)