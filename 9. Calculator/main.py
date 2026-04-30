def calculator():
    history = []   # This list will store the history of calculations performed by the user.
    
    while True:
        print("============================== Simple Calculator ===============================")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == '1':
                result = num1 + num2                            # addition operation
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = num1 - num2                            # subtraction operation 
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = num1 * num2                             # multiplication operation
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2                         # division operation with error handling for division by zero
                    operation = f"{num1} / {num2} = {result}"
                else:
                    operation = "Error: Division by zero is not allowed."
                    result = None
            
            if result is not None:
                history.append(operation)                    # Add the operation to the history list. 
                print(f"Answer: {result}")                   # Print the result of the current operation.
        
        elif choice == '5':
            print("\nCalculation History:")
            for item in history:
                print(item)
        
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a number between 1 and 6.")
            
            
if __name__ == "__main__":
    calculator()