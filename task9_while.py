# ======= TASK 9 - Iteration =======

# Write a program that continually asks the user to enter a number. 
# When the user enters “-1”, the program should stop requesting the user to 
# enter a number. Please be aware that 0 is not a valid input. 
# Hint: think about how you might exit the loop if -1 is entered. 
# The program must then calculate the average of the valid numbers entered, 
# excluding the -1 and 0. 
# Use a while loop to achieve the continuous prompting and number 
# collection.


total = 0
num_iterations = 0
average = 0

while True :
    num = int(input("Please input a number (enter -1 to stop) : "))
    if num == -1 :
        break
    if num == 0 :
        print("Invalid number")
        break
    else :
        total += num
        num_iterations += 1
        average = total / num_iterations
print(average)




