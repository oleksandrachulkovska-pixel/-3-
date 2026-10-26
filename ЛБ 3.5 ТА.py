numbers = []

while True:
    x = float(input("Введіть число (0 для завершення): "))

    if x == 0:
        break

    numbers.append(x)

if len(numbers) == 0:
    print("Немає введених чисел.")
else:
    average = sum(numbers) / len(numbers)
    product = 1

    for x in numbers:
        if x > average:
            product *= x

    print("Середнє арифметичне:", average)
    print("Добуток чисел, більших за середнє:", product)