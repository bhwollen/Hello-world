import math
number_of_lb_in_kilo = 2.2046226218488
done = False

print('This calculator will convert your weight from Pounds to Kilos and vice versa')
weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')
unit = unit.upper()
while not done:
    try:
        weight = int(weight)
        done = True
    except ValueError:
        weight = input("Please input a numerical value for weight: ")

while unit != 'L' and unit != 'K':
    unit = input("Please type 'K' for Kilograms or 'L' for Pounds: ")
    unit = unit.upper()

if unit == 'L':
    print('You weigh {} Kg'.format(math.ceil(weight / number_of_lb_in_kilo)))
else:
    print('You weigh {} Lbs'.format(math.ceil(weight * number_of_lb_in_kilo)))
