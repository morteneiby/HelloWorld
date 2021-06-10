price = [10, 20, 30]
sum = 0
for item in price:
    sum += item
print(sum)

#numbers = [5, 2, 5, 2, 2]
numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += "X"
    print(output)

numbers = [10, 5, 225, 40 , 21, 50]
low = 100

for number in numbers:
    if number < low:
        low = number
print(f"Laveste nummer er {low}")

numbers = [10, 5, 225, 40 , 21, 50, 10, 5, 40 , 50]
new_list = []
for number in numbers:
    if numbers.count(number) == 1:
        new_list.append(number)
print(new_list)


