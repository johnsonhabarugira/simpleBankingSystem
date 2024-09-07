while True:
    balance = 300000
    action = input(f"choose action: check balance,deposit money, withdraw").strip().lower()
    if action == "check balance":
        print(f"Your current balance is:{balance}")
    elif action =="deposit money":
        deposited_amount = float(input(f"enter amount"))
        balance += deposited_amount
        print(f"you have deposited {deposited_amount}. you new balance is:{balance}")
    elif action == "withdraw":
        withdraw_amount= float(input(f"enter amount to withdraw"))
        if withdraw_amount > balance:
            print(f"low balanc")
        else:
            balance -= withdraw_amount
            print(f"you have withdrawn {withdraw_amount}. your new balance is{balance}")
            break
    else:
        print("dfdf")