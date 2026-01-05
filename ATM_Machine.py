balance=0
def deposit():
    global balance
    amount=int(input("Enter the amount="))
    balance+=amount
    print("Amount deposited successfully!")
def withdraw():
    global balance
    amount=int(input("Enter the amount="))
    if amount<balance:
        balance-=amount
        print("Amount withdraw successfully!")
    else:
        print("INsufficient balance!")
def balances():
    global balance
    print("Balance=",balance)
def atm():
    while True:
        print("===================ATM SIMULATION SYSTEM=====================")
        print("1.Withdraw")
        print("2.Deposit")
        print("3.Balance")
        print("4.Exit")
        choice=int(input("Enter the choice="))
        if choice==1:
            withdraw()
        elif choice==2:
            deposit()
        elif choice==3:
            balances()
        elif choice==4:
            print("Thank you for using.")
            break
        else:
            print("Invalid choice")
atm()
