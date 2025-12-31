#Expense Tracker Project
expenses = [] #list of all expenses
print('Welcome To Expenses Tracker')
while True:
    print('===MENU====')
    print("1.Add Expenses")
    print("2.View All Expenses")
    print("3.View Total Expenses")
    print("4.Exit")

    choice = int(input('Please Enter your Choice :'))


    if (choice==1):
        date = input ('Enter the date')#Add expenses
        Category = input("Enter the category(Food,Travel,Shopping)")
        Description = input("Enter  specified item")
        amount = float(input("Enter the amount"))
        expense = {
            "date" : date,
            "category" : Category,
            "description" : Description,
            "amount"  : amount
        }    
        expenses.append(expense)
        print("\nExpenses is added successfully")

#2 View all Expenses
    elif(choice==2):
        if(len(expenses)==0):
            print("no expenses added")
        else:
            print("====Total expense")
            count = 1
            for eachexpense in expenses:
                print(f"Expense number{count} -> {eachexpense['date']},{eachexpense['category']},{eachexpense['description']},{eachexpense['amount']}")
                count+=1

#View Total Spending
    elif(choice==3):
        total = 0
        for eachexpense in expenses:
            total = total + eachexpense['amount']
        
        print("\n Total expense =",total)
#4 EXIT
    elif(choice==4):
        print("Thanks for using our system")
        break
    else:
        print("invalid")