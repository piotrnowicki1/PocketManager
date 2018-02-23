incomes = {}
expenses = {}

incomes['Salary'] = 4100
incomes['Part-time Job'] = 600
incomes['Flatmate rent'] = 799

expenses['Flat rent'] = 1500


def NewIncome():
  a = input("Please name your new income: \n")
  b = input("Please set the value of this income: \n")
  incomes[a] = b
  print("Your new list of incomes: \n")
  print(incomes)
  
  
def NewExpense():
  a = input("Please name your new expense: \n")
  b = input("Please set the value of this expense: \n")
  expenses[a] = b
  print("Your new list of expenses: \n")
  print(expenses)
  
  
def Main():
  print("Hello, this is your pocket manager! \n")
  print("What would you like to do? \n")
  print("1. Check my money balance \n")
  print("2. Check list of incomes \n")
  print("3. Add new income \n")
  print("4. Check list of expenses \n")
  print("5. Add new expense \n")
  print("6. Add not regular expense \n")
  
Main()
