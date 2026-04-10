from profiles import create_player, create_ia, all_player
import random

def choice(person) :
    if person["human"] == True :
        while True :
            print ("Choisissez entre Pierre, Feuille et Ciseaux.")
            player_choice = input("> ")
            if player_choice in ["Pierre", "Feuille", "Ciseaux"] :
                return player_choice
            else :
                print ("Cette valeur est incorrect, reessaye s'il te plait !")
    if person["human"] == False :
        ia_choice = random.choice (["Pierre", "Feuille", "Ciseaux"])
        return ia_choice