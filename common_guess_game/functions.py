import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "database.txt")

def retry_function():
    try:
        retry = input("If you wanna play again type 'continue' or 'quit' to close the game: ")
        if retry in ["continue", "yes", "y", "play"]:
            return True          
        else: exit()
    except ValueError:
        print("Something went wrong, please try again.")

def guess_function(guess, sort_number):
        if guess == sort_number: #If player wins, he earn coins
            print("Player Wins!")
            return True
        elif guess > sort_number:
            print("Try lower...")
        else: print("Try higher...")
        return False

        
def gameover_function(coins):
        if coins <= 0:
            print("Game Over, you are broke!")
            return False
        return True

def load_coins ():
    try:
        with open(DB_PATH, "r") as archive:
            return int(archive.read())
    except:
         return 100

def save_coins(value):
     with open(DB_PATH, "w") as archive:
          archive.write(str(value))

     
