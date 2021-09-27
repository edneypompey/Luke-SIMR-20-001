# Monday 27th September
# Module 4
# Luke Edney

# 4.3.1.6 LAB: A leap year: writing your own functions

# (Simplified variant of the task to make it understandable for myself)
# write and test a function which takes one argument (a year)
# and returns True if the year is an even year, or False otherwise.

def is_year_even(year): # define the function, with a year (parameter)
    if year % 2 == 0:   # if the year is even (conditions are met)
        return True     # terminate the function's execution, with True
    else:               # otherwise
        return False    # terminate the function's execution, with False
        
print(is_year_even(1900))    # printing test data, expceting it to be True
print(is_year_even(2000))    # printing test data, expceting it to be True
print(is_year_even(2016))    # printing test data, expceting it to be True
print(is_year_even(1987))    # printing test data, expceting it to be False

# 4.3.1.7 LAB: How many days: writing and using your own functions
# 4.3.1.8 LAB: Day of the year: writing and using your own functions
# 4.3.1.9 LAB: Prime numbers - how to find them

# # Haven't completed these because I do not understand the theory in netacad.


