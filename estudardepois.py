while True:
    if gameover_function(coins):
        level = input("Choose Level (1-Easy, 2-Normal, 3-Insane): ").lower()
        
        # 1. Definimos apenas as REGRAS aqui
        if level in ["easy", "1", "e"]:
            chances, premio = 20, 20
        elif level in ["normal", "2", "n"]:
            chances, premio = 15, 30
        elif level in ["insane", "3", "i"]:
            chances, premio = 10, 40
        else:
            print("Invalid Level!")
            continue

        # 2. O MOTOR do jogo roda UMA VEZ só para qualquer nível
        sort_number = random.randint(1, 100)
        for i in range(chances):
            try:
                guess = int(input(f"Chances left: {chances} | Guess: "))
                if guess_function(guess, sort_number):
                    coins += premio
                    save_coins(coins)
                    if retry_function(): break
                    else: exit()
                else:
                    chances -= 1
                    if chances <= 0:
                        coins -= premio # Penalidade
                        save_coins(coins)
                        if retry_function(): break
            except ValueError:
                print("Numbers only!")