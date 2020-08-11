###FUNCTIONS###

def hello_func(): #parenthesis are very important, can execute without them
    pass
#the 'pass' keyword means we dont want anything in there for now but it wont return an error

def hello_fun():
    print('Hello function!')

hello_fun()
#output = 'Hello Function!'
#because 'print' is used in the def, we only need to call the function

def hello_function():
    return 'Hello Function :)'
#the return key word makes it so the function is equal to the string inputted
#without print() this function will give no output
print(hello_function())
#this now, with the print function, outputs a value of 'hello function'

print(hello_function().upper())
#we can carry out functions to pre defined functions

#To allow us to add argumnents to our function, we will need to input some parameters to our function
def greeting_func(greeting): # greeting is now the parameter
    return '{} Function.'.format(greeting) # the {} represent the space in which 'greeting' will fill
print(greeting_func('Hello there'))
#output is 'Hello there function'

#Say we want to add a name as a parameter so we get the greeting and name returned
#we can add that to the function very easily
def greeting_function(greeting, name='You'):
    return '{} {}, this is the greeting function'.format(greeting, name)
print(greeting_function('Hey there', 'Pete'))
#parameters are added after the name of the function and need to be accounted for in the retrun value
#we also set a default value for name, so if no value was inputted it would resort to this value

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)  
#we can use the above function if we want to accept an unknown quantity of arguments
#*args = arguments (single variable format)
#**kwargs = key word arguments (always something = something format)
#lets say args allows us to input the classes a student is taking
#lets say kwargs allows us to input random details about the student
student_info('Math', 'Chem', 'Physics', name='John', age=20)
#Output
# ('Math', 'Chem', 'Physics') <-- created as a Tuple (args)
# {'name':'John', 'age':20} <-- created as a dictionary (kwargs)

courses = ['Math', 'Chem', 'Physics']
info = {'name':'John', 'age':20}
student_info(*courses, **info)


##EXAMPLE###

#Number of dats per month. First value is a placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 ==0) # checking if year inputted is a leap year. Return is true or false

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:   # checking if the month inputted is a proper value
        return 'Invalid Month'  # if not, 'Invalid month' returned

    if month == 2 and is_leap(year): # checking if month is Feb AND is_leap evaluates to True
        return 29                     # if both evaluate to true, return 29 

    return month_days[month] # this is using the value produced from the above 2 lines as the index for month_days list
#if month inputted is 2, the month_days[month] = month_days[2] which is referring to index 2 in this list






