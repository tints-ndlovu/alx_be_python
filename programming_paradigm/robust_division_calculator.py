def safe_divide(numerator, denominator):
    try:
        
        if denominator != 0:
            return f"The result of the division is {numerator/denominator}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Please enter numeric values only.")
    

