from blackjack import create_packofcard, blackjack,adjust_points, game_result,turn
import numpy as np
import random as random
import multiprocessing as mp
import os
'''
a state = (player cards, croupier cards, action)
action = hit , stand, double, take_insurance (1 to 4)


'''
nb_of_pack = 4

def create_Qtable():
    Qtable = mp.Manager().dict()
    for player_first_draw in range(1,12):
        for player_second_draw in range(player_first_draw,12):
            sum_card = 0
            if player_first_draw == 11 :
                sum_card += 1
            else: sum_card += player_first_draw
            if player_second_draw == 11:
                sum_card += 1   
            else: sum_card += player_second_draw
            for sum_card in range(sum_card,23):
                for croupier_first_draw in range(2,12):
                    if player_first_draw == 10 and player_second_draw==11 :
                        continue
                    else : 
                        Qtable[(player_first_draw,player_second_draw,sum_card,croupier_first_draw)] = [0, 0, 0, 0]  # Initialize Q-values for each action
    return Qtable

def choose_action(state, Q, epsilon):
    rd = np.random.rand()
    if rd < epsilon and (state[3]==11 or state[3]==1):
        return np.random.choice([0,1,2,3])  # exploration

    
    elif rd < epsilon :
        return np.random.choice([0,1,2])

    else:
        return np.argmax(Q[state])


def update_Q(Q, state, action,best_next_action, reward, next_state, alpha, gamma):
    td_target = reward + gamma * Q[next_state][best_next_action]
    td_delta = td_target - Q[state][action]
    Q[state][action] += alpha * td_delta

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
    if player_points[0] ==10 and player_points[1]==11:
        return 1, list_of_state, list_of_action
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
        action = choose_action(state, Q, epsilon)

        list_of_action.append(action)
        continue_game,player_points,croupier_points,cards,discard,assurance ,surrender,double,split= turn(action+1,player_points,croupier_points,cards,discard,assurance , surrender,double,split) # type: ignore
        player_points = adjust_points(player_points)
        if player_points[0] > player_points[1]:
            player_points[0], player_points[1] = player_points[1], player_points[0]
        state = (player_points[0], player_points[1], min(22,sum(player_points)) , croupier_points[0])
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
    return gain, list_of_state, list_of_action

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def training(Q) :
    num_episodes = 10000000
    alpha = 0.1
    gamma = 1.0
    epsilon = 0.3
    bet = 1

    for z in range(num_episodes):
        if z%100==0 :
            clear_console()
            print(f"pourcentage d'avancement : {(z/num_episodes)*100}%")
        gain,list_of_state,list_of_action = blackjack(Q,epsilon,bet)
        """
        Implementaion of a propagation of the reward in all the trajectory
        """

        # Update Q-table

        #1er cas : gagne directement blackjack (1 state - pas d'action)
        #2eme cas : on se couche directement 1 action 2 state (pareil)
        #3eme cas : plusieur action et 1 state finale pareil
        #4eme cas : 1 state finale different

        if len(list_of_action)>=2:
            for i in range(len(list_of_action) - 1):
                update_Q(Q, list_of_state[i], list_of_action[i],list_of_action[i+1], gain, list_of_state[i+1], alpha, gamma)

            update_Q(Q,list_of_state[-2], list_of_action[-2], np.argmax(Q[list_of_state[-1]]), gain,list_of_state[-1], alpha, gamma)
            
        elif  len(list_of_action)==1: 
            
            update_Q(Q,list_of_state[0], list_of_action[0], np.argmax(Q[list_of_state[1]]), gain,list_of_state[1], alpha, gamma)

    return Q
    

    # Save the Q-table to a file


if __name__ == '__main__':
    manager = mp.Manager()
    Q = manager.dict(create_Qtable())  # dictionnaire partagé

    processes = []
    for _ in range(5):  # 5 processus
        p = mp.Process(target=training, args=(Q,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Affichage final
    for _ in range(10):
        clé = random.choice(list(Q.keys()))
        print(clé, Q[clé])
    np.save('Qtable.npy', Q)
