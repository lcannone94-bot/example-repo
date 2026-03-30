# ======= TASK 8 - List types =======
#
# Imagine you want to store the names of three of your friends in a list of strings. 
# Create a list variable called friends_names, and write the syntax to store the full names of three of your friends. 

friends_names = ["Riccardo", "Agata", "Mara"]

# Now, write statements to print out the name of the first friend, then the name of the last friend, and finally the length of the list. 

print(f"The name of the first friend is {friends_names[0]}")
print(f"The name of the last friends is {friends_names[-1]}")
print(f"The legth of the list is {len(friends_names)}")


# Now, define a list called friends_ages that stores the age of each of your friends 
# in a corresponding manner, i.e., the first entry of this list is the age of the friend named first in the other list. 

friends_ages = [31, 29, 28]

# Print each friend’s name and age in a sentence similar to this: Sophia is 25 years old

print(f"{friends_names[0]} is {friends_ages[0]} years old")
print(f"{friends_names[1]} is {friends_ages[1]} years old")
print(f"{friends_names[2]} is {friends_ages[2]} years old")