# ======== TASK 10 ERROR  =======

# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")   # syntax error fixed. missing parenthesis
print ("\n")                            # syntax error : no parenthesis and runtime error : code not indent

    # Variables declaring the user's age, casting the str to an int, and printing the result
age  = 24                                # unexpected indent, fixed - runtime error. Syntax error :  == is not used for defining a variable. In addition, this variable should be equal to a number.
age_str = str(age)                       # unexpected indent, fixed - runtime error. Name of variables is wrong
print("I'm " + age_str + " years old.")  # unexpected indent, fixed - runtime error

    # Variables declaring additional years and printing the total years of age
years_from_now = 3.5                    # unexpected indent. Fixed + logical error, the answer should take into account 3 years from now + 6 months
total_years = age + years_from_now      # unexpected indent. fixed. 

print("The total number of years:" + str(total_years)) # syntax error.fixed + logical error: if we print a variable we should't have ""

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = str(total_years * 12)                 # runtime error. variable not defined 
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") #Syntax error. We cannot concatenate an integer

#HINT, 330 months is the correct answer


