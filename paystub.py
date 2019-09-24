name = input("Enter employee's name: ")
hours_worked = int(input('Enter number of hours worked in a week: '))
hourly_pay = float(input('Enter hourly pay rate: '))
federal_withholding_rate = float(input('Enter federal tax withholding rate: '))
state_withholding_rate = float(input('Enter state tax withholding rate: '))
gross_pay = hourly_pay * hours_worked
federal_withholding = gross_pay * federal_withholding_rate
state_withholding = gross_pay * state_withholding_rate
total_deductions = state_withholding + federal_withholding

print(f"""
Employee name: {name}
Hours worked: {hours_worked}
Pay Rate: ${hourly_pay}
Gross Pay: ${round(gross_pay, 2)}
Deductions:
    Federal Withholding ({federal_withholding_rate * 100}%): ${round(federal_withholding, 2)}
    State Withholding ({state_withholding_rate * 100}%): ${round(state_withholding, 2)}
    Total Deduction: ${round(state_withholding + federal_withholding, 2)}
Net Pay: ${round(gross_pay - total_deductions, 2)}
""")
