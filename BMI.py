weight_in_pounds = int(input('Enter weight in pounds: '))
height_in_inches = int(input('Enter height in inches: '))
weight_in_kilos = weight_in_pounds * 0.45359237
height_in_meters = height_in_inches * 0.0254
bmi = weight_in_kilos / height_in_meters ** 2
print(bmi)
