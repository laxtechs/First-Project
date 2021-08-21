import random
attempts_values = []

def score_count():
    if len(attempts_values) <= 0:
        print("There is no currently no high score , it is your for taking ")
    else:
        print("the high score is {} attemps".format(min(attempts_values)))

def new_game():
    number_value = int(random.randint(1,10))
    print("Welcome, This is a Guessing game")
    player = input("Input your name ")
    play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player))

    counts = 0
    score_count()
    while play.lower() == "yes":
        try:
            guess = input("Selected a Number from 1 to 10")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Selected guess Number from 1 to 10")
            if int(guess) == number_value:
                print("you won ")
                counts += 1
                attempts_values.append(counts)
                print("you have attempts {}".format(counts))
                play_again = input("do u want to play the guess game again  / (yes/No)")
                counts = 0
                score_count()
                number_value = int(random.randint(1,10))
                if play.lower() == "no":
                    print("that is cool , have a good game")
                    break 
            elif int(guess) > number_value:
                print("It is Lower")
                counts +=1
            elif int(guess) < number_value:
                print("It is higher")
                counts += 1 
        except ValueError as err:
            print("this is not a valid a input")
            print("({})".format(err))

    else:
        print("This is a Good")
if __name__== "__main__":
    new_game()



                


