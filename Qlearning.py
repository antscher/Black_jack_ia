from blackjack import create_packofcard, blackjack,adjust_points
import numpy as np
import random

'''
a state = (player cards, croupier cards, action)
action = hit , stand, double, take_insurance (1 to 4)


'''
num_episodes = 100000
alpha = 0.1
gamma = 1.0
epsilon = 0.1  # exploration rate
nb_of_pack = 4

def create_Qtable():
    deck = create_packofcard(nb_of_pack)
    Qtable = []
    for player_first_draw in range(2,12):
        for player_second_draw in range(2,12):
            for croupier_first_draw in range(2,12):
                sum_card = adjust_points([player_first_draw,player_second_draw])
                Qtable.append((player_first_draw,player_second_draw,sum_card,croupier_first_draw),[0, 0, 0, 0])  # Initialize Q-values for each action


def choose_action(state, Q, epsilon):
    rd = np.random.rand()
    if rd < epsilon and state[3]==11 and state[3]==1:
        return np.random.choice([1,2,3,4])  # exploration

    
    elif rd < epsilon :
        return np.random.choice([1,2,3])

    else:
        return np.argmax(Q[state])


def update_Q(Q, state, action, reward, next_state, alpha, gamma):
    best_next_action = np.argmax(Q[next_state])
    td_target = reward + gamma * Q[next_state][best_next_action]
    td_delta = td_target - Q[state][action]
    Q[state][action] += alpha * td_delta



def blackjack(numberofpack,game_state) :

    cards = []
    discard = []
    player_points = []
    croupier_points = []
    for i in range(numberofpack):
        cards += create_packofcard()
    print("Welcome to the game")
    user_play = input("Would you like to play ? write y if yes, anything else otherwise ")
    
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
    

    #First card for the croupier
    random_index = random.randrange(len(cards))
    card = cards[random_index]
    discard.append(card)
    croupier_points.append(card[1])
    cards.pop(random_index)

    blackjack_first = False
    continue_game = True
    assurance = False
    split = False
    mise = bet
    surrender = False
    double = False
    total_points = 0

    #Case where the player has a blackjack in is first hand
    if sum(player_points) == 21:
        print("You win with a blackjack !")
        total_points =21
        continue_game = False
        blacjack_first = True


    while sum(player_points) < 21 and  continue_game:
        user_input = input("Would you like another card ? write y if yes, anything else otherwise")
        continue_game,player_points,croupier_points,cards,discard,assurance ,surrender,double,split= turn(user_input,player_points,croupier_points,cards,discard,assurance , surrender,double,split)
            
            
        adujste_points(player_points)
        print("ajustement ", sum(player_points))
    if surrender:
        total_points==-1
    else:
        total_points==sum(player_points)

    print("end on this hand")



    print("mise : ", mise)
    
    while sum(croupier_points)<=17 : 
        random_index = random.randrange(len(cards))
        card = cards[random_index]
        print("I draw : " + DisplayCard(card))

        discard.append(card)
        croupier_points.append(card[1])
        adujste_points(croupier_points)
        cards.pop(random_index)


    gain= game_result(bet,total_points,croupier_points,assurance,surrender,double,blackjack_first)
    return state, gain


num_episodes = 100000
alpha = 0.1
gamma = 1.0
epsilon = 0.1
Q = create_Qtable()

for _ in range(num_episodes):
    action = choose_action(state, Q, epsilon)
    next_state, reward, = blackjack(action)
    """
    Implementaion of a propagation of the reward in all the trajectory
    """

    # Update Q-table
    update_Q(Q, state, action, reward, next_state, alpha, gamma)
    state = next_state



        