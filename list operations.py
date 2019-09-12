numbers = [5, 2, 1, 7, 4, 1]

numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(5)
print(numbers)

print(50 in numbers)
print(10 in numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers2.append(100)
print(numbers2)

print(numbers.index(1))
print(numbers)

numbers.pop()
print(numbers)

numbers.pop()
print(numbers)

numbers.clear()
print(numbers)

