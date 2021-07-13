money_owed = float(input("How much do you owe?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("What will your monthly payment be?\n"))
months = int(input("How many months is the term?\n"))

monthly_rate = apr/100/2

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print('the last payment is', money_owed)
        print('you paid off the loan in', i+1, 'months')
        break

    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest.", end=' ')
    print("Now I owe", money_owed)