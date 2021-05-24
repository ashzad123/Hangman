import random

print("----------------WELCOME TO HANGMAN GAME--------------------")
with open('words.txt','r') as f:
    words=f.readlines()

word=random.choice(words)[:-1]


allowed_error=7
guesses=[]
done=False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end=" ")
        else:
            print("_",end=" ")
    print(" ")


    guess=input(f"Allowed Guesses left{allowed_error}, Next Guess:")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_error-=1
        if allowed_error==0:
            break
    done=True
    for letter in word:
        if letter.lower() not in guesses:
            done=False

if done:
    print(f"Congratulation You have succesfully found the word it is: {word}")
else:
    print(f"Game Over,the word was{word}")

