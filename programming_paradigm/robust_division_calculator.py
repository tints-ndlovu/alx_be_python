def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        return num/den
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Please enter numeric values only.")
    

