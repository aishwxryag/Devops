#def main():
#  print("Workflow successful!")
#if __name__=='__main__':
#  main()
import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def create_deck():
    return [(rank, suit) for rank in RANKS for suit in SUITS]

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def evaluate_card(card):
    rank, suit = card
    if rank in ['Jack', 'Queen', 'King']:
        return 10
    elif rank == 'Ace':
        return 11
    else:
        return int(rank)

def play_card_game():
    print("Welcome to the Card Game!")
    deck = create_deck()
    shuffle_deck(deck)

    player_score = 0
    computer_score = 0
    rounds = 5

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        player_card = deal_card(deck)
        computer_card = deal_card(deck)

        print(f"Player's card: {player_card}")
        print(f"Computer's card: {computer_card}")

        player_score += evaluate_card(player_card)
        computer_score += evaluate_card(computer_card)

    print("\nGame Over!")
    print(f"Final Scores:")
    print(f"Player: {player_score} | Computer: {computer_score}")

    if player_score > computer_score:
        print("Congratulations! You win!")
    elif player_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_card_game()
