# /////////// بسم الله  ////////////

print("#" * 20, "Welcome to the game", "#" * 20)
playing = input("Do you want to play ?(y/n) : ").lower()

print()
while playing != "n" and playing != "y":
    print("Your choice is wrong")
    playing = input("Chose again ?(y/n) : ").lower()
print()

if playing == "n":
    print("Well, as you like.")
    quit()  # <- new to me, but it is important.

print("Ok, let's play")
print()
score = 0
questions = 0
# question 1
answer = input("What's CPU stander for ? : ").lower()
questions += 1
if answer == "central processing unit":
    print("# Correct. #")
    score += 1
else:
    print("# Incorrect! #")
    print('The correct answer is : "central processing unit"')

# question 2
print()
answer = input("What's GPU stander for ? : ").lower()
questions += 1
if answer == "graphics processing unit":
    print("# Correct. #")
    score += 1
else:
    print("# Incorrect! #")
    print('The correct answer is : "graphics processing unit"')

# question 3
print()
answer = input("What's PSU stander for ? : ").lower()
questions += 1
if answer == "power supply unit":
    print("# Correct. #")
    score += 1
else:
    print("# Incorrect! #")
    print('The correct answer is : "power supply unit"')

# question 4
print()
answer = input("Do you want me to continue questions ? (y/n) : ").lower()
while answer != "n" and answer != "y":
    print("Your choice is wrong")
    answer = input("Chose again ?(y/n) : ").lower()

if answer == "n":
    print(f"Your Score is : => [{score}].")
    quit()
else:
    print("Ok, take another one.")
    print()
    answer = input("What's RAM stander for ? : ").lower()
    questions += 1
    if answer == "random access memory":
        print("# Correct. #")
        score += 1
    else:
        print("# Incorrect! #")
        print('The correct answer is : "random access memory"')
# finally
print()
print(f"That was the last one, and the number of question was [{questions}].")
if score == questions:
    print("Congratulations!, all answers are correct")
print()
print(f"Your Score is : => [{score}].")
print(f"Your percentage is : => [{score / questions * 100}]%.")

print("#" * 60)