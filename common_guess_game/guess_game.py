from functions import retry_function #retry restart the game
import random #random generates sort_number 

coins = 100 #variables at alphabetical order
space = "      "

#attempts system
normal_try = 15
insane_try = 10

print("Welcome to the most generic guessing game you've ever seen!" "\n") #Title
print("Easy" + space + "Normal" + space + "Insane")

while True: #Game start
    easy_try = 20

    try:
        level = input("Choose the difficulty level: ")
        level = str(level).lower()
    except ValueError:
        print("Something went wrong, please try again.")

    try:
        if level in ["easy", "e", "1"]: #easy mode starts here

            sort_number = random.randint(1,100)


            for i in range (20): 

                try:
                    print(f"number: {sort_number}")

                    guess = int(input("Choose a number between 1 and 100: "))

                    if guess == sort_number: #If player wins, he earn coins
                        coins += 20
                        print("Player Wins!")
                        if retry_function ():
                            break
                        else: exit()

                    else: #else, loses his coins
                        easy_try -= 1
                        print(f"Your chances: {easy_try}")
                        if easy_try <= 0:
                            if retry_function():
                                break
                except ValueError:
                    print("Something went wrong, please try again.")                
        else:
            print("Please type a valid value!")
            continue



    except ValueError:
        print ("ValueError.")            
    

    
        


