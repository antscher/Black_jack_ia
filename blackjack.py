import random
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

def DisplayCard(card):
    res= ""
    color = card[0]
    figure = card[1]
    if color==0:
        res+="of spade "
    elif color == 1:
        res+="of heart "
    elif color ==2 : 
        res+= "of clubs "
    else :
        res += "of diamonds "

    if figure == 10 : 
        res = "head wich is worth 10 points "+res
    if figure ==11:
        res = "Ace "
    else :
        res = str(figure) +" "+res
    return res


def blackjack(numberofpack) :
    cards = []
    discard = []
    player_points = 0
    croupier_points = 0
    for i in range(numberofpack):
        cards += create_packofcard()
    print("Welcome to the game")
    user_play = input("Would you like to play ? write y if yes, anything else otherwise ")

    if user_play == "y": 


        random_index = random.randrange(len(cards))
        card = cards[random_index]
        print("You draw : " + DisplayCard(card))

        discard.append(card)
        player_points += card[1]
        cards.pop(random_index)


        random_index = random.randrange(len(cards))
        card = cards[random_index]
        print("I draw : " + DisplayCard(card))

        discard.append(card)
        croupier_points += card[1]
        cards.pop(random_index)

        user_input = "y"
        while player_points < 21 and  user_input == "y":
            user_input = input("Would you like another card ? write y if yes, anything else otherwise")
            random_index = random.randrange(len(cards))
            card = cards[random_index]
            print("You draw : " + DisplayCard(card))

            discard.append(card)
            player_points += card[1]
            cards.pop(random_index)

        if player_points >=21 :
            return "you loose"
        while croupier_points<=17 : 
            random_index = random.randrange(len(cards))
            card = cards[random_index]
            print("I draw : " + DisplayCard(card))

            discard.append(card)
            croupier_points += card[1]
            cards.pop(random_index)
        if croupier_points >=21 or croupier_points<player_points:
            return "you win"
        else :
            return "you loose"

    else :
        return "too bad !"
            





print(blackjack(4))