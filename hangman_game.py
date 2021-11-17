import requests
from random import randint

# get request from this api

website = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(website)
words = response.content.splitlines()

# converting the list of bytes into list of strings

for i in range(0, len(words)):
    words[i] = words[i].decode("utf-8")

# print(randint(0, len(words)-1))

# getting a random item from the list

random_word = words[randint(0, len(words)-1)]
# print(random_word)

guesses_left = 6
random_word = "".join(list(random_word))
# print(random_word)
current_state = []
for item in range(0, len(random_word)):
    current_state.append("_")
while True:
    print("Here is the current state:")
    print("".join(current_state))
    print("You have " + str(guesses_left) + " more guesses")
    current_guess = input("What's your guess? Enter a letter: ")
    if current_guess in random_word:
        indices = []
        for i in range(0, len(random_word)):
            if random_word[i] == current_guess:
                current_state[i] = current_guess
    if "_" not in current_state:
        guesses_left -= 1
        print("Congratulations, you guessed the word correctly in " + str(6 - guesses_left) + " guesses!")
        print(random_word)
        guesses_left = 0
        for item in range(0, len(random_word)):
            current_state[item] = "_"
        break
    else:
        guesses_left -= 1
        if guesses_left == 0:
            print("".join(current_state))
            final_guess = input("You are out of guesses, please guess the whole word:")
            if final_guess == random_word:
                print("Congratulations, you guessed the word correctly in " + str(6 - guesses_left) + " guesses!")
                print(random_word)
                break
            else:
                print("Sorry, you lost, the correct word was: " + random_word)
                break
