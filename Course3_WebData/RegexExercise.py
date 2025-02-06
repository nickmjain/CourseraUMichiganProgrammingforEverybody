import re

filename = "regex_sum_2076242.txt"

handle = open(filename)

total = 0
for line in handle:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        total = total + int(number)

print(total)

# writing above code as a list comprehension
total = sum([int(number) for number in re.findall('[0-9]+', open(filename).read())])
print(total)