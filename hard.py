



loan_quantity = eval(input("Enter the amount you will loan: "))
loan_time = eval(input("Enter the loan for how many years: "))

loan_time *= 12
monthly = loan_quantity / loan_time
balance = loan_quantity
interest = 0

print("PAYMENT SCHEDULE")
print("MONTH\t|MONTHLY PAYMENT\t|INTEREST\t|PRINCIPAL\t|REMAINING LOAN\t|")

for i in range(1,loan_time + 1,1):
    balance -= monthly
    interest = balance * 0.00212
    month = interest + monthly
    print(f"{i}\t  {round(monthly,2)} \t\t{round(balance,2)} \t\t{round(interest,2)}\t\t{month}")
    print()