import math

print('This calculator will convert your weight from Pounds to Kilos and vice versa')
weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

while True:
    try:
        weight = int(weight)
        break
    except ValueError:
        weight = input("Please input a numerical value for weight: ")

while unit.upper() != 'L' and unit.upper() != 'K':
    unit = input("Please type 'K' for Kilograms or 'L' for Pounds: ")

if unit.upper() == 'L':
    print('You weigh {} Kg'.format(math.ceil(int(weight) * 0.45359237)))
else:
    print('You weigh {} Lbs'.format(math.ceil(int(weight) / 0.45359237)))
