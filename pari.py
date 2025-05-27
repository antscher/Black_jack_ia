import random

def pari(action,player_points,player_points2,croupier_points,cards,discard,mise,assurance ,split , surrender):
    """
    Actions possibles du joueur au Blackjack :
    1. Tirer une carte (Hit)
    2. Rester (Stand)
    3. Doubler la mise (Double Down)
    4. Séparer (Split)
    5. Prendre une assurance (Insurance)
    6. Abandonner (Surrender)
    """
    action = int(action)
    if action == 1:
        random_index = random.randrange(len(cards))
        card = cards[random_index]
        print("You draw : " + DisplayCard(card))

        discard.append(card)
        player_points.append(card[1])
        cards.pop(random_index)
        continue_game = True

    if action == 2:
        # Rester (Stand)
        continue_game = False
    if action == 3:
        # Doubler la mise (Double Down)
        mise *= 2
        random_index = random.randrange(len(cards))
        card = cards[random_index]
        print("You draw : " + DisplayCard(card))
        discard.append(card)
        player_points.append(card[1])
        cards.pop(random_index)
        continue_game = False
    if action == 4:
        # Séparer (Split)
        for i in range(len(player_points)):
            if player_points[-1] in [card for card in player_points[:-1]]:
                print("You can split these cards.")
                continue_game = True
                split = True
                player_points2.append(player_points.pop())
                mise *= 2

            else:
                print("You cannot split these cards.")
                continue_game = True
    if action == 5:
        # Prendre une assurance (Insurance)
        if croupier_points[0] == 11 and not assurance:
            print("You take insurance.")
            mise *= 1.5
            assurance = True
            continue_game = True

    if action == 6:
        # Abandonner (Surrender)
        print("You surrender.")
        surrender = True 
        continue_game = False
    else:
        print("Invalid action. Please choose a valid action.")

    return continue_game,player_points,player_points2,croupier_points,cards,discard,mise,assurance ,split,surrender


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
