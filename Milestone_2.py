# Step 1: Importing the random module
import random

# Step 2: Assigning this list to a variable called word_list.
word_list = ["Mango", "Apple", "Banana", "Cherry", "Grapes"]

# Step 3: Using Randome.choice method to choose random word from the word_list,
word = random.choice(word_list)

# Step 4: Print out the newly created list to the standard output.
print(word)

# Step 5: Ask the user to enter a single letter.
guess = input("Enter a single letter: ")

# Step 6: Validate the user input.
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")