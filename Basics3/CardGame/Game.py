import GameSetup

game_on = True

round_num = 0

while game_on:
     
     round_num += 1
     print(f"Round {round_num}")

     if len(GameSetup.player_one.all_cards) == 0:
          print('Player One, out of cards! Player Two Wins')
          game_on = False
          break
     
     if len(GameSetup.player_two.all_cards) == 0:
          print('Player Two, out of cards! Player One Wins')
          game_on = False
          break
     
     # Start a New Round

     player_one_cards = []
     player_one_cards.append(GameSetup.player_one.remove_one())

     player_two_cards = []
     player_two_cards.append(GameSetup.player_two.remove_one())



     at_war = True

     while at_war:
          
          if player_one_cards[-1].value > player_two_cards[-1].value:
               GameSetup.player_one.add_cards(player_one_cards)
               GameSetup.player_one.add_cards(player_two_cards)
               at_war = False

          elif player_one_cards[-1].value < player_two_cards[-1].value:
               GameSetup.player_two.add_cards(player_one_cards)
               GameSetup.player_two.add_cards(player_two_cards)
               at_war = False

          else:
               print('WAR!')

               if len(GameSetup.player_one.all_cards) < 5:
                    print("Player One unable to declare war")
                    print('Player Two Wins!')
                    game_on = False
                    break
               
               elif len(GameSetup.player_two.all_cards) < 5:
                    print("Player Two unable to declare war")
                    print('Player One Wins!')
                    game_on = False
                    break
               else:
                    for num in range(5):
                         player_one_cards.append(GameSetup.player_one.remove_one())
                         player_two_cards.append(GameSetup.player_two.remove_one())
