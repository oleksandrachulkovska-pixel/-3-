s = input("Введіть рядок: ")

upper_count = 0
lower_count = 0

for symbol in s:
    if symbol.isupper():
        upper_count += 1
    elif symbol.islower():
        lower_count += 1

print("Кількість великих літер:", upper_count)
print("Кількість малих літер:", lower_count)