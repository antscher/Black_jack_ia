from blackjack import DisplayCard
import random

def pari(action,player_points,croupier_points,cards,discard,mise,assurance):
    """
    Actions possibles du joueur au Blackjack :
    1. Tirer une carte (Hit)
    2. Rester (Stand)
    3. Doubler la mise (Double Down)
    4. Séparer (Split)
    5. Prendre une assurance (Insurance)
    6. Abandonner (Surrender)
    """
    if action == 1:
        random_index = random.randrange(len(cards))
        card = cards[random_index]
        print("You draw : " + DisplayCard(card))

        discard.append(card)
        player_points.append(card)
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
        player_points.card
        cards.pop(random_index)
        continue_game = False
    if action == 4:
        # Séparer (Split)
        for i in range(len(player_points)):
            if player_points[-1][1] in [card[1] for card in player_points[:-1]]:
                print("You can split these cards.")
                continue_game = True
            else:
                print("You cannot split these cards.")
                continue_game = True
    if action == 5:
        # Prendre une assurance (Insurance)
        if croupier_points[0][1] == 11:
            mise *= 1.5
            assurance = True
            continue_game = True

    if action == 6:
        # Abandonner (Surrender)
        pass

    if player_points > 21:
        print("You busted with " + str(player_points) + " points.")
        continue_game = False
    return player_points,continue_game,assurance 
