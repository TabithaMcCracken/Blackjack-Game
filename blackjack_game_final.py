# Blackjack game
# The dealer acts as a player and is required to hit on 16, stay on 17

import random
import os
import time

class Card:
    def __init__(self, suit, rank, card_value):
        
        self.suit = suit # Suit of the Card like Spades and Clubs
        self.rank = rank # Representing Value of the Card like A for Ace
        self.card_value = card_value # Score Value for the Card like 10 for King

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self) -> None:
        self.deck = []
        suit_name = [
            '\u2667', # Clubs
            '\u2662', # Diamonds
            '\u2661', #Hearts
            '\u2664' #Spades
        ]
        rank_name = [
            'A',
            '2', 
            '3', 
            '4', 
            '5', 
            '6', 
            '7', 
            '8', 
            '9', 
            '10', 
            'J', 
            'Q', 
            'K'
        ]
        card_value = {
            'A':11, 
            '2':2, 
            '3':3, 
            '4':4, 
            '5':5, 
            '6':6, 
            '7':7, 
            '8':8, 
            '9':9, 
            '10':10, 
            'J':10, 
            'Q':10, 
            'K':10
        } 
        # Ace starts as an 11 and is changed to a 1 if hand goes over 21

        for suit in suit_name:
            for rank in rank_name:
                self.deck.append(Card(suit, rank, card_value[rank]))

    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

    def __str__(self) -> str:
        return f"{self.deck}"

    def __repr__(self) -> str:
        return f"Deck: \n{self.deck}"

class Player:
    """Creates a player which could be the dealer
    """
    def __init__(self, name, isDealer) -> None:
        self.name = name
        self.isDealer = isDealer
        self.cards = []
        self.score = 0

    def calculate_score(self):
        score = 0
        for card in self.cards:
            score += card.card_value
        self.score = score

        # Checks for 2 Aces in hand, change 1st one to value 1
        if len(self.cards) == 2:
            if self.cards[0].card_value == 11 and self.cards[1].card_value == 11:
                self.cards[0].card_value = 1
                self.score -= 10

        # Checks to see if Ace should be an 11 or changed to a 1 if the hand is over 21
        x = 0
        while self.score > 21 and x < len(self.cards):
            if self.cards[x].card_value == 11:
                self.cards[x].card_value = 1
                self.score -= 10
                x += 1
            else:
                x += 1

        return self.score

    def get_card(self):
        dealt_card = random.choice(game_deck.deck)
        self.cards.append(dealt_card)
        game_deck.deck.remove(dealt_card)

def print_cards(player):
    if player.isDealer == False:
        print("==Your Cards==")
        for card in player.cards:
            print(card)
        
    else:
        print("\n==Dealer's Cards==")
        print("The first card is hidden.")
        for card in player.cards[1:]:
            print(card)

CARD_SLICES = [
    " _________________",
    "|                 |",
    "|   {rank}            |",  # 2
    "|                 |",
    "|                 |",
    "|                 |",
    "|        {suit}        |",
    "|                 |",
    "|                 |",
    "|                 |",
    "|            {rank}   |",  # 9
    "|_________________|",
]

HIDDEN_CARD_SLICES = [
    " ________________",
    "| !              |",
    "|      * *       |",
    "|    *     *     |",
    "|          *     |",
    "|         *      |",
    "|       *        |",
    "|       *        |",
    "|                |",
    "|                |",
    "|       *     !  |",
    "|________________|",
]

def print_cards_fancy(player_hand):
    print(f"=={player_hand.name}'s Cards==")
    for card_slice, hidden_slice in zip(CARD_SLICES, HIDDEN_CARD_SLICES):
        if player_hand.isDealer:
            card_slices = "\t".join(
                [   
                        card_slice.format(rank = card.rank + (" " if len(card.rank) == 1 else ""), 
                        suit = card.suit + "") for card in player_hand.cards[1:]

                ]
            )
            print(f"\t{hidden_slice}\t{card_slices}")
        else:
            card_slices = "\t".join(
                [   
                        card_slice.format(rank = card.rank + (" " if len(card.rank) == 1 else ""), 
                        suit = card.suit + "") for card in player_hand.cards

                ]
            )
            print(f"\t{card_slices}\t{hidden_slice if player_hand.isDealer else ''}") # Still not sure what the second tab section is for
            
def print_showing_score(player):
        if player.isDealer == False:
            print(f"\n{player.name}'s Score: {player.calculate_score()}\n")
        else:
            print(f"\nDealer's showing score: {player.calculate_score() - player.cards[0].card_value}\n")

def print_all_cards_and_scores(player_hand):
    print(f"=={player_hand.name}'s Cards==")
    for card_slice, hidden_slice in zip(CARD_SLICES, HIDDEN_CARD_SLICES):
        card_slices = "\t".join(
            [   
                card_slice.format(rank = card.rank + (" " if len(card.rank) == 1 else ""), 
                suit = card.suit + "") for card in player_hand.cards

            ]
        )
        print(f"\t{card_slices}\t")
    print(f"\n{player_hand.name}'s Final Score: {player_hand.calculate_score()}\n")

def clear():
    os.system("clear")

def game_engine():
    # Players turn
    while True:
        if dealer.score == 21:
            print("The dealer has hit 21! You lose!")
            break
        
        if player.score <= 21:
            print("It's your turn.")
            player_response = input("Would you like to stay(S), hit(H), or fold(F)?")
            
            clear()
            
            if player_response == "F":
                print("You have folded. Game Over")
                break

            if player_response == "S":
                print("You have decided to stay.")
                time.sleep(1)
                break

            if player_response == "H":
                print("Here is another card.")
                time.sleep(1)
                player.get_card()
                print_cards_fancy(player)
                player.calculate_score()
                print(f"\nYour score: {player.score}")
                
                if player.score > 21:
                    time.sleep(1)
                    print("You bust! Game Over!")
                    break

    # Dealers turn
    while True:
        if player_response == "F" or player.score > 21:
            break
        
        if dealer.score >= 21:
            print("The dealer busted! You win!")
            break
        
        elif dealer.score >= 17 and dealer.score <= 21:
            print("The dealer stays!")
            break

        elif dealer.score <= 16:
            print("The dealer is taking another card.")
            time.sleep(1)
            dealer.get_card()
            print_cards_fancy(dealer)
            print_showing_score(dealer)
            time.sleep(2)
        
        else:
            break

    # Game results
    time.sleep(1)
    input("\nPress Enter to flip all cards over")
    clear()
    print_all_cards_and_scores(player)
    print_all_cards_and_scores(dealer)

    # Determine winner
    if player.score > dealer.score and player.score <= 21:
        print("You win!")
    if dealer.score > player.score and dealer.score <=21:
        print("The dealer wins!")
    if dealer.score == player.score:
        print("It's a tie!")

if __name__ == '__main__':
    # Setup    
    # Create deck
    print("Welcome to Blackjack!")
    game_deck = Deck()
    game_deck.shuffle()

    # Create dealer and player
    dealer = Player("Dealer", True)
    player_name = input("What is your name?")
    player = Player(player_name, False)
    print(f"Welcome {player.name}!")
    print(f"You are playing the {dealer.name}.")

    input("Press Enter to Continue")
    clear()

    print("We will now deal 2 cards to each player.")
    time.sleep(1)

    # Deal 2 cards to player and dealer
    while len(dealer.cards) < 2:
        # Deal a card to the player, print cards and score
        player.get_card()

        # Deal a card to the dealer, print cards and score
        dealer.get_card()    

    time.sleep(1)
    print_cards_fancy(player)
    print_showing_score(player)
    time.sleep(1)
    print_cards_fancy(dealer)
    print_showing_score(dealer)

    game_engine()


