from datetime import datetime

def display_current_datetime():
    current_date = datetime.now("%Y-%m-%d %H:%M:%S")
    print(current_date)

number_of_days = int(input("Enter a number of days (as an integer): "))


def calculate_future_date():
    future_date = datetime.now("%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=number_of_days)
    print(future_date)