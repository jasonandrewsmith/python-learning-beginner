expenses = []
for i in range(7):
    expenses.append(float(input('enter a expense: ')))
total = sum(expenses)


print('you spent $', total, sep='')