#10. Write a program that has following menu:
#Enter code w for withdraw.
#Enter code d for deposit.
#Enter code c for checking balance.

#Note: 1 take initial amount as input from user.

#Note:2 You can wwithdraw an amount only if balance is greater than or equal to 500
#and withdrawing amount should be less than balance.




option = input("""
Enter code w for withdraw.
Enter code d for deposit.
Enter code c for checking balance
""")

match option:
    case "W"|"w":
        balance = int(input("enter balance = "))
        #amount = int(input("enter amount = "))
        if balance >= 500:
            amount = int(input("enter amount = "))
            if amount <= balance:
                balance -= amount
                print("Transaction successful", balance)
            else:
              print("unsufficient balance")
        else:
             print("You cannot withdraw as min bal below 500 hundread")
    case "d"|"D":
        balance = int(input("enter balance"))
        deposited_amount = int(input("""enter amount"""))
        balance += deposited_amount 
        print("Deposite successful",balance)
        
    case "c"|"C":
        balance = int(input("enter balance = "))
        print("checking balance = ",balance)

    case default:
        
        print("invalid option")
        
