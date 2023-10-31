import random
import time

def get_player_names():
    player1 = input("Speler 1, voer je naam in: ")
    player2 = input("Speler 2, voer je naam in: ")
    return player1, player2

def generate_random_number():
    return random.randint(1, 100)

def get_guess(player_name):
    while True:
        try:
            guess = int(input(f"{player_name}, doe een gok: "))
            if 1 <= guess <= 100:
                time.sleep(2)
                return guess
            else:
                print("Ongeldige gok. Probeer opnieuw.")
        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in.")

def display_winner(player_name):
    print(f" ** **      ** **     ** **")
    print(f" *****      *****     *****")
    print(f"  ***        ***       *** ")
    print(f"   *          *         *  ")
    print(f"{player_name} wint! Goed gedaan!")

def main():
    print("Welkom bij het raadspel!")

    player1, player2 = get_player_names()
    score_player1 = 0
    score_player2 = 0

    while True:
        secret_number = generate_random_number()
        print(f"\n{player1} en {player2}, ik heb een getal bedacht tussen 1 en 100. Raad welk getal het is!")

        while True:
            guess_player1 = get_guess(player1)
            if guess_player1 == secret_number:
                display_winner(player1)
                score_player1 += 1
                break
            elif guess_player1 < secret_number:
                print("Hoger!")
            else:
                print("Lager!")

            guess_player2 = get_guess(player2)
            if guess_player2 == secret_number:
                display_winner(player2)
                score_player2 += 1
                break
            elif guess_player2 < secret_number:
                print("Hoger!")
            else:
                print("Lager!")
                
        play_again = input("Wil je nog een keer spelen? (ja/nee): ")
        if play_again.lower() != "ja":
            break

    print("\n=== Eindstand ===")
    print(f"{player1}: {score_player1} punten")
    print(f"{player2}: {score_player2} punten")

if __name__ == "__main__":
    main()