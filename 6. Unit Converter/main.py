def convert_length():
    print("Length Converter")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Feet to Centimeters")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet:.2f} feet.")
    elif choice == '2':
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is equal to {meters:.2f} meters.")
    elif choice == '3':
        feet = float(input("Enter length in feet: "))
        centimeters = feet * 30.48
        print(f"{feet} feet is equal to {centimeters:.2f} cm.")
    else:
        print("Invalid choice. Please try again.")
        
def convert_area():
    print("Area Converter")
    print("1. Square Meters to Square Feet")
    print("2. Square Feet to Square Meters")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        sqm = float(input("Enter area in square meters: "))
        sqft = sqm * 10.7639
        print(f"{sqm} square meters is equal to {sqft:.2f} square feet.")
    elif choice == '2':
        sqft = float(input("Enter area in square feet: "))
        sqm = sqft / 10.7639
        print(f"{sqft} square feet is equal to {sqm:.2f} square meters.")
    else:
        print("Invalid choice. Please try again.")

def convert_weight():
    print("Weight Converter")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg is equal to {pounds:.2f} lbs.")
    elif choice == '2':
        pounds = float(input("Enter weight in pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} lbs is equal to {kg:.2f} kg.")
    else:
        print("Invalid choice. Please try again.")
        
def convert_temperature():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
    else:
        print("Invalid choice. Please try again.")


def converter():
    print("Welcome to the Unit Converter!")
    print("Please select the type of conversion:")
    print("1. Length")
    print("2. Area")
    print("3. Weight")
    print("4. Temperature")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        convert_length()
    elif choice == '2':
        convert_area()
    elif choice == '3':
        convert_weight()
    elif choice == '4':
        convert_temperature()
    else:
        print("Invalid choice. Please try again.")
if __name__ == "__main__":
    while True:  
        converter()
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            print("Thank you for using the Unit Converter. Goodbye!")
            break