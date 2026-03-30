# ========= TASK 14 JOKES ========
'''Create a new Python file in this folder called jokes.py. 
2. You are going to create a random joke generator using Python’s random module. 
This will require a bit of research on your part. 
3. Create a list of jokes that include their punchlines. 
4. Use the random module to display a random joke each time the code runs. 
'''

import random

jokes = ["Why don’t skeletons fight each other?\nThey don’t have the guts",
         "What do you call fake spaghetti?\nAn impasta.",
         "Why did the scarecrow win an award?\nHe was outstanding in his field.",
         "Why don’t eggs tell jokes?\nThey’d crack each other up."
]

r_num = random.randint(1,3)

print("\nRANDOM JOKE:\n"+ "\n" + jokes[r_num] + "\n")

# ======== END OF THE CODE ========
