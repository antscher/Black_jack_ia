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



    # First we draw two cards for the player and one for the croupier
    #First card for the player
    random_index = random.randrange(len(cards))
    card = cards[random_index]
    print("You draw : " + DisplayCard(card))
    discard.append(card)
    player_points.append(card[1])
    cards.pop(random_index)

    #Second card for the player
    random_index = random.randrange(len(cards))
    card = cards[random_index]
    print("You draw : " + DisplayCard(card))
    discard.append(card)
    player_points.append(card[1])
    cards.pop(random_index)

    #First card for the croupier
    random_index = random.randrange(len(cards))
    card = cards[random_index]
    print("I draw : " + DisplayCard(card))
    discard.append(card)
    croupier_points.append(card[1])
    cards.pop(random_index)

    blackjack = False
    continue_game = True
    assurance = False
    split = False
    mise = bet
    surrender = False
    double = False
    player_pointssplit = [player_points]
    total_points = []

    #Case where the player has a blackjack in is first hand
    if sum(player_points) == 21:
        print("You win with a blackjack !")
        blackjack = True
        total_points.append(21)
        continue_game = False

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
    total =0 

    if split_point ==-1 :
        print("you surrender")
        total  -= bet/2        
    if assurance and sum(croupier_points)==21:
        total += bet
        print("you win your assurance !")
    if assurance and sum(croupier_points)!=21:
        total -= bet/2
    
    if blackjack :
        print("you win blackjack")
        total += bet*1.5
        if double :
            total += bet*1.5
    elif split_point >21 :
        print("you loose")
        total -= bet
    elif sum(croupier_points) >21 or sum(croupier_points)<split_point and split_point==21:
        print("you win blackjack")
        total += bet*1.5
        if double :
            total += bet*1.5
    elif sum(croupier_points) >21 or sum(croupier_points)<split_point:
        print("you win")
        total += bet
        if double :
            total += bet
    else :
        print("draw")
        total += 0
    
    return total


print(blackjack(4,10))