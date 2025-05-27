import random
from pari import pari as turn, DisplayCard

def create_packofcard() : 
    #We create a pack of cards 0=spade, 1=heart, 2=clubs, 3=diamonds,
    #Also everything beyond ten so every head is valued at 10 points
    #Exepect for the ace wich can either be 1 or 11
    pack = []
    for i in range(4):
        for j in range(1,12): 
            pack.append((i,j))
            if j == 10:
                for k in range(3):
                    pack.append((i,j))

    random.shuffle(pack)
    return pack


def adujste_points(list):
    for point in  list : 
        if point == 11 and sum(list)>=21: 
            index = list.index(11)
            list[index]=1
    return list
    


def blackjack(numberofpack,bet) :
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
    print("You draw : " + DisplayCard(card))

    discard.append(card)
    player_points.append(card[1])
    cards.pop(random_index)


    random_index = random.randrange(len(cards))
    card = cards[random_index]
    print("I draw : " + DisplayCard(card))

    discard.append(card)
    croupier_points.append(card[1])
    cards.pop(random_index)

    continue_game = True
    assurance = False
    split = False
    mise = bet
    surrender = False
    double = False
    player_pointssplit = [player_points]
    total_points = []

    while player_pointssplit != []:
        player_points = player_pointssplit.pop().copy()
        while sum(player_points) < 21 and  continue_game:
            user_input = input("Would you like another card ? write y if yes, anything else otherwise")
            continue_game,player_points,player_pointssplit,croupier_points,cards,discard,assurance ,surrender,double= turn(user_input,player_points,player_pointssplit,croupier_points,cards,discard,assurance , surrender,double)
            
            
            adujste_points(player_points)
            print("ajustement ", sum(player_points))
        if surrender:
            total_points.append(-1)
        else:
            total_points.append(sum(player_points))


    print("mise : ", mise)
    
    while sum(croupier_points)<=17 : 
        random_index = random.randrange(len(cards))
        card = cards[random_index]
        print("I draw : " + DisplayCard(card))

        discard.append(card)
        croupier_points.append(card[1])
        adujste_points(croupier_points)
        cards.pop(random_index)

    gain = 0
    for split_point in total_points: 
        gain += game_result(bet,split_point,croupier_points,assurance,surrender,double)
    return gain
    

    


def game_result(bet,split_point,croupier_points,assurance,surrender,double): 

    if double :
        bet *=2

    if split_point ==-1 :
        print("you surrender")
        return -bet/2

        
    if split_point >=21 :
        print("you loose")
        return -bet
        

    if assurance and sum(croupier_points)==21:
        bet += bet *1.5
        print("you win your assurance !")
        return bet/2
    if assurance and sum(croupier_points)!=21:
        return -bet/2

    if surrender:
        print("you loose half of your bet")
        return -bet/2
    
    if sum(croupier_points) >21 or sum(croupier_points)<split_point:
        print("you win")
        return bet*2
    
    elif max(21,sum(croupier_points)) == max(21,split_point):
        print("draw")
        return bet
    
    else :
        print("you loose")
        return -bet




print(blackjack(4,10))