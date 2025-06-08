######################----ATM----######################
balance = 0
while True:
    print("/nATM MENU")
    print("1.CREDIT")
    print("2.DEBIT")
    print("3.BALANCE")
    print("4.EXIT")

    your_choice = input("enter your choice 1 to 4: ")
    if your_choice == '1':
        amount = float(input("enter the amount to credit:" ))
        if amount <=0:
            print("plese enter positive amount")
        else: balance += amount
        print(f"${amount} credited to your account: ")

    elif your_choice == '2':
        amount = float(input("enter the amount to debit: "))
        if amount <=0:
            print("plese enter positive amount:" )
        elif amount > balance:
            print("insufficient balance: ")
        else:
            balance -= amount
            print(f"${amount}debited to you from your account:" )
    
    elif your_choice == '3':
        print(f"your current balance is : ${balance}: ")

    elif your_choice == '4':
        print("THANK YOU FOR USING ME come again!")
        break
    else:
        print("INVALID your_choice plese try again")