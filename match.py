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
    

def game_1 (p1, p2) :
    p1_play = choice(p1)
    p2_play = choice(p2)
    choice_win = {"Pierre": "Ciseaux", "Feuille": "Pierre", "Ciseaux": "Feuille"}
    if choice_win[p1_play] == p2_play :
        print (f"{p1} à gagner cette manche !")
        return p1
    if choice_win[p1_play] != p2_play :
        print (f"{p2} à gagner cette manche !")
        return p2
    if p1_play == p2_play :
        print ("Égalité, vous avez fais pareil.")
        return None


