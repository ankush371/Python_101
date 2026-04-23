def fibonacci_n(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

""" # there is a different way to do this using (functool lru cache).where fib is already defined as a recursive function and the lru cache will store the results of previous calls to avoid redundant calculations. Here's how you can implement it:


from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci_n(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_n(n - 1) + fibonacci_n(n - 2)

"""

# for series generation 

def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

#The best way to do this is using the generator function which will yield the next number in the sequence each time it is called, allowing you to generate Fibonacci numbers on-the-fly without storing the entire series in memory. Here's how you can implement it:

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


"""
    print(fibonacci_n(10))   # output: 55
    print(fibonacci_series(10))  # output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(list(fibonacci_generator(10))) # output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

"""

#If you want to generate Fibonacci numbers indefinitely, you can modify the generator function to run in an infinite loop. 

# You can use case statements to make a simple dashboard where user can get a single or series of fibonacci numbers. Here's an example of how you can implement this using a simple command-line interface:

def fibonacci_dashboard():
    while True:
        print("Welcome to the Fibonacci Dashboard!")
        print("1. Get a single Fibonacci number")
        print("2. Get a series of Fibonacci numbers")
        print("3. Exit")
        
        choice = input("Please enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            n = int(input("Enter the position of the Fibonacci number you want: "))
            print(f"The {n}th Fibonacci number is: {fibonacci_n(n)}")
        
        elif choice == '2':
            n = int(input("Enter how many Fibonacci numbers you want in the series: "))
            print(f"The first {n} Fibonacci numbers are: {fibonacci_series(n)}")
        
        elif choice == '3':
            print("Exiting the dashboard. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    fibonacci_dashboard()