from blackjack import create_packofcard, blackjack,adjust_points, game_result,turn
import numpy as np
import random as random

nb_of_pack = 4

Qtable = np.load('Qtable.npy', allow_pickle=True).item()

def blackjack(Q,epsilon,bet) :
    list_of_action = []
    list_of_state = []

    cards = []
    discard = []
    player_points = []
    croupier_points = []
    for i in range(nb_of_pack):
        cards += create_packofcard()
  
    
    random_index = random.randrange(len(cards))
    card = cards[random_index]
    discard.append(card)
    player_points.append(card[1])
    cards.pop(random_index)

    #Second card for the player
    random_index = random.randrange(len(cards))
    card = cards[random_index]
    discard.append(card)
    player_points.append(card[1])
    cards.pop(random_index)

    if player_points[0] > player_points[1]:
        player_points[0], player_points[1] = player_points[1], player_points[0]

    #First card for the croupier
    random_index = random.randrange(len(cards))
    card = cards[random_index]
    discard.append(card)
    croupier_points.append(card[1])
    cards.pop(random_index)

    state = (player_points[0], player_points[1], min(22,sum(adjust_points(player_points))) , croupier_points[0])  # Update state with player and croupier points
    list_of_state.append(state)

    blackjack_first = False
    continue_game = True
    assurance = False
    split = False
    surrender = False
    double = False
    total_points = 0



    #Case where the player has a blackjack in is first hand
    if sum(adjust_points(player_points)) == 21:
        total_points =21
        continue_game = False
        blacjack_first = True


    while sum(adjust_points(player_points)) < 21 and  continue_game:
        action = np.argmax(Q[state])
        print("action : ", action)
        print(f"State : {state}")
        list_of_action.append(action)
        continue_game,player_points,croupier_points,cards,discard,assurance ,surrender,double,split= turn(action,player_points,croupier_points,cards,discard,assurance , surrender,double,split) # type: ignore
        print(f"player_points avant ajustement: {player_points}")
        print(f"adjust_points: {adjust_points(player_points)}")
        print(f"sum: {sum(adjust_points(player_points))}")
        state = (player_points[0], player_points[1], min(22,sum(adjust_points(player_points))) , croupier_points[0]) # Update state with player and croupier points
        list_of_state.append(state)

    if surrender:
        total_points==-1
    else:
        total_points= sum(adjust_points(player_points))

    
    while sum(croupier_points)<=17 : 
        random_index = random.randrange(len(cards))
        card = cards[random_index]

        discard.append(card)
        croupier_points.append(card[1])
        croupier_points = adjust_points(croupier_points)
        cards.pop(random_index)


    gain= game_result(bet,total_points,croupier_points,assurance,surrender,double,blackjack_first)
    return gain

print("Starting the game...")
print(blackjack(Qtable, 0.1, 10))  # Example bet of 10