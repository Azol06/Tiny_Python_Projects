def retry_function():
    try:

        retry = input("If you wanna play again type 'continue' or 'quit' to close the game: ")
        if retry in ["continue", "yes", "y", "play"]:
            return True
                    
        else: exit()
    
    except ValueError:
        print("Something went wrong, please try again.")