investmentAmount = float(input('Enter investment amount: '))
annualInterestRate = float(input('Enter annual interest rate: '))
monthlyInterestRate = ((annualInterestRate) / 100 / 12)
numberOfYears = int(input('Enter the number of years: '))
numberOfMonths = numberOfYears * 12
futureInvestmentValue = round((investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths), 2)
print(f'Accumulated value is {futureInvestmentValue}')
