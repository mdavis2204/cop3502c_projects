from p1_random import P1Random

rng = P1Random() # keep outside of loop

doGame = True
innerDoGame = True
game_count = 0
player_win = 0
dealer_win = 0
tie = 0

def card_name(num): # Returns the name of the card based upon the number inputted
    if num == 1:
        return "ACE"
    elif 1 < num <= 10:
        print()
        return num
    elif card == 11:
        return "JACK"
    elif card == 12:
        return "QUEEN"
    elif card == 13:
        return "KING"

def card_value(num): # Returns the value of the card based upon the card number
    if 1 <= num <= 10:
        return num
    elif card >= 11 and card <= 13:
        return 10

def print_menu(): # Prints out the menu using only a single line
    print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")

def getCard(): # Returns a number between 1 and 13, which is the card's number
    return rng.next_int(13) + 1

def getOption(): # I moved the input sanitization process outside of the main loop to improve readability.
    while True:
        print_menu()
        selection = input("\nChoose an option: ")
        if selection == "1" or selection == "2" or selection == "3" or selection == "4": # If the user inputs anything other than 1, 2, 3, or 4, they are given an error and prompted to reenter.
            return selection # Handles all inputs as a string for extra input sanitization
        else:
            print("\nInvalid input!\nPlease enter an integer value between 1 and 4.")



while doGame: # Iterates through the game in a large
    innerDoGame = True # (Re)defines the inner loop as true for when a game is ended but the program continues
    game_count += 1
    print(f"\nSTART GAME #{game_count}")
    player_hand = 0 # Resets the player's hand to be 0
    card = getCard()
    player_hand += card_value(card)

    print(f"Your card is a {card_name(card)}!")
    print(f"Your hand is: {player_hand}")

    dealer_hand = 0
    while innerDoGame: # Loops through inner user selection process
        selection = getOption()
        if selection == "1": # If player hits, the program gives them another card and performs checks
            card = getCard()
            player_hand += card_value(card)

            print(f"Your card is a {card_name(card)}!")
            print(f"Your hand is: {player_hand}")

            if player_hand == 21: # Checks whether the player won or lost after receiving their cards. If neither, then continues as normal.
                print("\nBLACKJACK! You win!")
                innerDoGame = False
                player_win += 1
                break
            elif player_hand > 21:
                print("\nYou exceeded 21! You lose.")
                innerDoGame = False
                dealer_win += 1
                break

        elif selection == "2": # If the user holds the program generates the dealer's hand and checks to see who won (or tied)
            dealer_hand = rng.next_int(11) + 16
            innerDoGame = False
            print(f"\nDealer's hand: {dealer_hand}\nYour hand is: {player_hand}")
            if player_hand > dealer_hand or dealer_hand > 21:
                print("\nYou win!")
                player_win += 1
            elif player_hand < dealer_hand:
                print("\nDealer wins!")
                dealer_win += 1
            elif player_hand == dealer_hand:
                print("\nIt's a tie! No one wins!")
                tie += 1


        elif selection == "3": # Displayes game statistics in a single line for conciseness
            print(f"Number of Player wins: {player_win}\nNumber of Dealer wins: {dealer_win}\nNumber of tie games: {tie}\nTotal # of games played is: {game_count -1 }\nPercentage of Player wins: {player_win/(game_count - 1) * 100}%")

        elif selection == "4": # Sets both loops to be false to be extra sure, then breaks program if the user wishes to end.
            innerDoGame = False
            doGame = False
            break

