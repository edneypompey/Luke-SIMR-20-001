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
    # # Haven't completed these because I do not understand the theory in netacad.

# 4.3.1.9 LAB: Prime numbers - how to find them
    # # Haven't completed these because I do not understand how to convert the maths to python.

# 4.3.1.10 LAB: Converting fuel consumption

# write a pair of functions converting l/100km into mpg, and vice versa.
def liters_100km_to_miles_gallon(liters):
    
    # 1 mile = 1609.344 metres; 
    # convert km to miles, then multiply by 100
    miles = 100 * (1000 / 1609.344) # 100 * (number of kilometers)
    
    # 1 gallon = 3.785411784 litres
    # convert gallons to litres
    gallons = liters / 3.785411784  # litres variable diveded by gallon value from scenario
    
    # return with miles to gallons conversion
    return miles / gallons  # terminate and return to the point of invocation.

def miles_gallon_to_liters_100km(miles):
    litres = 3.785411784    # define litre variable
    kilometers = miles * 1609.344 / 1000  # kilometers in a mile, then divide by 1000 to give 100km
    km100 = kilometers / 100    # create km variable
    return litres / km100 # divide litres by km
    

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

