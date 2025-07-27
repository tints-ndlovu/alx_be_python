import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)

number_of_days = int(input("Enter a number of days (as an integer): "))

def calculate_future_date():
    future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    print(future_date)