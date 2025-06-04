import random

def pari(action,player_points,croupier_points,cards,discard,assurance , surrender,double,split):
    """
    Actions possibles du joueur au Blackjack :
    1. Tirer une carte (Hit)
    2. Rester (Stand)
    3. Doubler la mise (Double Down)
    4. Séparer (Split)
    5. Prendre une assurance (Insurance)
    6. Abandonner (Surrender) (not in this rule set)
    """
    action = int(action)
    if action == 1:
        random_index = random.randrange(len(cards))
        card = cards[random_index]

        discard.append(card)
        player_points.append(card[1])
        cards.pop(random_index)
        continue_game = True

    elif action == 2:
        # Rester (Stand)
        continue_game = False
    elif action == 3:
        # Doubler la mise (Double Down)
        if not (split and (player_points[0]== 1 or player_points[0] == 11)):
            random_index = random.randrange(len(cards))
            card = cards[random_index]
            discard.append(card)
            player_points.append(card[1])
            cards.pop(random_index)
            continue_game = False
            double = True

    elif action == 4:
        # Prendre une assurance (Insurance)
        if (croupier_points[0] == 11 or croupier_points[0] == 1 ) and not assurance:
            assurance = True
            continue_game = True

        else:
            continue_game = True
    else:
        continue_game = True
    """
    if action == 6:
        # Abandonner (Surrender)
        print("You surrender.")
        surrender = True 
        continue_game = False
    """

    return continue_game,player_points,croupier_points,cards,discard,assurance ,surrender,double,split


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
