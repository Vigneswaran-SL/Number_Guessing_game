import random
rnum = random.randint(1,50)
maxAttempt = 5
attempts = 1
while attempts <= maxAttempt:
    print(f"You have {maxAttempt - attempts +1} attempts")
    try:
        guess = int(input("Guess the number between 1 to 50:"))
    except ValueError:
        print("Please enter only number")
        continue
    if guess == rnum:
        print(f"yay.. You guessed the number in {attempts}  attempt(s)")
        break
    elif guess > rnum:
        print("Too high!\n")
    else :
        print("Too low!\n")
    attempts += 1
if attempts > maxAttempt:
    print(f"you lost out of attempts , The correct number was {rnum}")