has_high_income = True
has_good_credit = True
has_criminal_record = True
if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for Loan")
elif (has_good_credit or has_high_income) and not has_criminal_record:
    print("Maybe Eligible for Loan")
else:
    print("Not eligible for loan")
