names = ['john', 'bob', 'ben', 'lewis']
names[0] = 'jon'
print(names[0])
print(names[-2])
print(names[2:3])

numbers = [10, 2, 200, 3, 5, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
