import maph

weight_lb = input('What is your weight in pounds: ')
weight_kg = 0.45359237 * int(weight_lb)
print('You weigh ' + str(maph.ceil(weight_kg)) + 'kg')
print('You weigh ' + str(weight_kg) + 'kg')
