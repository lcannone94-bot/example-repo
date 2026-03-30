# ======== TASK 13 -LOOP LIST ========

'''Use this opportunity to extend yourself by completing an optional challenge activity. 
1. 
Create a new file in this folder called loop_lists.py. 
2. Inside it, define a list of strings of your five favourite movies. 
3. Now, loop over the list. For each item in the list, print out “Movie: ” plus the 
movie's name. 
4. Can you figure out how to print out “Movie 1: <Movie 1's name>, Movie 2: …”, etc.? 
Hint: You will need to look up the enumerate command in Python using a Google 
search. This command allows you to loop over a list retaining both the item at every 
position and its index (i.e., position in the list).'''

movies = ["LOTR", "Seven", "Harry Potter", "Love Actually", "This is the end"]

for i, it in enumerate(movies, start=1) :
    print(f"Movie {i} : {it}")


# for index, item in enumerate(my_list): print(index, item)
