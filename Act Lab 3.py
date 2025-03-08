#Act 3
def check_number():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")
    user_input = input("Do you want to check another number? (yes/no): ").lower()
    if user_input == 'yes' or user_input == 'y':
        check_number()
    else:
        print("Number checking skipped.")
    
check_number()
