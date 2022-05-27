## Create a function for a leap year.

prompt = int(input('Enter a year: '))

def leapYear(param_year):
    if param_year % 4 == 0 and param_year % 100 != 0 or param_year % 400 == 0:
        print(str(param_year) + ' is a leap year.')
    else:
        print(str(param_year) + ' is  not a leap year.')

leapYear(prompt)
