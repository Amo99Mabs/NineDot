# income - expenses = margin
print("Welcome to NineDot - Budget App!")
income = float(input('Enter your monthly post-tax income (R): '))
additional = float(input('Enter any additional income you expect next month (R): '))
total_income = income + additional
print('Great your total income next month will be R' + str(total_income))
print('Now we will get some expenses data...')

def gather_expenses():
    housing = float(input('Enter your monthly housing expenses (R): '))
    utilities = float(input('Enter your monthly utility expenses (R): '))
    food = float(input('Enter your monthly food expenses (R): '))
    misc = float(input('Enter your monthly misc expenses (R): '))
    total_expenses = housing + utilities + food + misc
    return total_expenses

expense_total = gather_expenses()
print('Great your total expenses next month will be R' + str(expense_total))
margin = total_income - expense_total 
if margin >= 0:
    print('Your total surplus next month will be R' + str(margin))
else:
    print('Your will come up' + str(margin)) + ' negative!'

print('Thanks for using NineDot')