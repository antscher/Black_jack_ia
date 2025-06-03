from pari import pari as turn, DisplayCard

def create_packofcard() : 
    #We create a pack of cards 0=spade, 1=heart, 2=clubs, 3=diamonds,
    #Also everything beyond ten so every head is valued at 10 points
    #Exepect for the ace wich can either be 1 or 11
    pack = []
    for i in range(4):
        for j in range(2,12): 
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
    ''''
    cheat_index = cards.index((1,4))
    card = cards[cheat_index]
    print("You draw : " + DisplayCard(card))
    discard.append(card)
    player_points.append(card[1])
    cards.pop(cheat_index)

    cheat_index = cards.index((2,4))
    card = cards[cheat_index]
    print("You draw : " + DisplayCard(card))
    discard.append(card)
    player_points.append(card[1])
    cards.pop(cheat_index)
    '''
    
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
    return gain
    

    


def game_result(bet,split_point,croupier_points,assurance,surrender,double,blackjack_first): 
    
    total =0 
    print("somme du croupier : ", sum(croupier_points))
    if split_point ==-1 :
        print("you surrender")
        total  -= bet/2        
    if assurance and sum(croupier_points)==21:
        total += bet
        print("you win your assurance !")
    if assurance and sum(croupier_points)!=21:
        total -= bet/2
    
    if blackjack_first :
        print("you win blackjack")
        total += bet*1.5
        if double :
            total += bet*1.5
    elif split_point >21: 
        print("you loose")
        total -= bet
        if double :
            total -= bet
    elif (sum(croupier_points) >21 or sum(croupier_points)<split_point) and split_point==21:
        print("you win blackjack")
        total += bet*1.5
        if double :
            total += bet*1.5
    elif sum(croupier_points) >21 or sum(croupier_points)<split_point:
        print("you win")
        total += bet
        if double :
            total += bet
    elif sum(croupier_points) > split_point:
        print("you loose")
        total -= bet
        if double :
            total -= bet
    else :
        print("draw")
        total+= 0
    
    return total


print("total point :",blackjack(4,10))