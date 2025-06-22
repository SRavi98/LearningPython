import Player
import Deck

# GAME SETUP

player_one = Player.Player("One")
player_two = Player.Player("Two")

new_deck = Deck.Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())