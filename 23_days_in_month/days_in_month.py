#Exercise: Write a function that returns the number of days in a month in a given year

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year_given, month_given):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (month_given < 1) and (month_given > 12):
        return "Invalid month"
    else:
        if is_leap(year_given):
            month_days[1] = 29 
    return month_days[month_given-1]
  
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

