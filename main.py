## Create a function for a leap year.

prompt = input('Enter a year: ')

def leapYear(param_year):
    if param_year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(str(param_year) + ' is a leap year.')
    else:
        print(str(param_year) + ' is  not a leap year.')

prompt
