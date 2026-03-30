# ======== TASK 9 ========

# Create a new Python file in this folder called pattern.py.  
# Write code to output the arrow pattern shown below, using an if-else 
# statement in combination with a for loop  
#  You are allowed to use more than one for loop. But use only one for 
# loop if you wish to challenge yourself):

'''
* 
** 
*** 
**** 
***** 
**** 
*** 

'''

# Define symbol, number of iterations and list in order to include the number of iterations

symbol="*"
num = 6
y = []

# Creation of the list with the number of iterations requested

for x in range(1,num) :
    y.append(x)

# I multiply the symbol time the number of iterations requested and stored in the list y

for i in y :
    first =symbol*i
    print(first)

# Creation of the reverse of the number of iterations. We want only the first two iterations in reverse
# This allows to to dynamically change the number of iterations from the variable num

y2 = y[::-1]

for i in y2[1:4] :
    second = symbol*i
    print(second)
