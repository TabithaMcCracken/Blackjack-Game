# Blackjack game
# The dealer acts as a player and is required to hit on 16, stay on 17

import random
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
        suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        rank_name = [
            'Ace',
            '2', 
            '3', 
            '4', 
            '5', 
            '6', 
            '7', 
            '8', 
            '9', 
            '10', 
            'Jack', 
            'Queen', 
            'King'
        ]
        card_value = {
            'Ace':11, 
            '2':2, 
            '3':3, 
            '4':4, 
            '5':5, 
            '6':6, 
            '7':7, 
            '8':8, 
            '9':9, 
            '10':10, 
            'Jack':10, 
            'Queen':10, 
            'King':10
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

    def print_cards(self):
        if self.isDealer == False:
            print("Your Cards:")
            for card in self.cards:
                print(card)
            
        else:
            print("\nDealer's Cards:")
            print("The first card is hidden.")
            for card in self.cards[1:]:
                print(card)

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

    def print_showing_score(self):
        if self.isDealer == False:
            print(f"\nYou're score: {self.calculate_score()}")
        else:
            showing_score = dealer.calculate_score() - dealer.cards[0].card_value # Can I put this into the line below?
            print(f"\nDealer's showing score: {showing_score}")

    def print_all_cards_and_scores(self):
        for card in self.cards:
            print(card)
        print(f"{self.name}'s Score: {self.calculate_score()}")

    def get_card(self):
        dealt_card = random.choice(game_deck.deck)
        self.cards.append(dealt_card)
        game_deck.deck.remove(dealt_card)

def game_engine():
# Evaluate if player or dealer has hit 21
    while True:
        if dealer.score == 21:
            dealer.print_cards()
            print("The dealer has hit 21! You lose!")
            break

        player_response = input("Would you like to stay(S), hit(H), or fold(F)?")

        if player_response == "F":
            print("You have folded. Game Over")
            break

        if player_response == "H":
            player.get_card()
            player.print_cards()
            player.calculate_score()
            print(f"\nYour score: {player.score}")
            
            if player.score > 21:
                print("You bust! Game Over!")
                player.print_all_cards_and_scores()
                dealer.print_all_cards_and_scores()
                break

        if player_response == "S":
            print("You have decided to stay.")
            
        
        print(" The dealer now plays.")
        if dealer.score <= 16:
            dealer.get_card()
            dealer.print_cards()
            dealer.print_showing_score()
        
        elif dealer.score >= 17 and dealer.score <= 21:
            dealer.print_cards()
            dealer.print_showing_score()
            print("The dealer stays!")

        else:
            print("The dealer busted! You win!")
            dealer.print_all_cards_and_scores()
            player.print_all_cards_and_scores()
            break

            
        print("We will now flip all cards over:")
        player.print_all_cards_and_scores()
        dealer.print_all_cards_and_scores()

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

    print("We will now dealer 2 cards to each player.")
    time.sleep(2)

    # Deal 2 cards to player and dealer
    while len(dealer.cards) < 2:
        # Deal a card to the player, print cards and score
        player.get_card()
        player.print_cards()
        player.print_showing_score()

        time.sleep(2)

        # Deal a card to the dealer, print cards and score
        dealer.get_card()    
        dealer.print_cards()
        dealer.print_showing_score()

        time.sleep(2)

    game_engine()


