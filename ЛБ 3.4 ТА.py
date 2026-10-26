N = int(input("Введіть число N: "))

power = 1

print("Степені двійки, менші за N:")

while power < N:
    print(power, end=" ")
    power *= 2

print()