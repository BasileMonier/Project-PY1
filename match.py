from profiles import tournament_choice
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
        print (f"{p1['name']} à gagner cette manche !")
        return p1
    if choice_win[p1_play] != p2_play :
        print (f"{p2['name']} à gagner cette manche !")
        return p2
    if p1_play == p2_play :
        print ("Égalité, vous avez fais pareil.")
        return None

def all_game (p1, p2) :
    p1_score = 0
    p2_score = 0
    while p1_score < 3 and p2_score < 3 :
        game = game_1(p1, p2)
        if game == p1 :
            p1_score += 1
        if game == p2 :
            p2_score += 1
        if game == None :
            continue
    winner = p1 if p1_score == 3 else p2
    loser = p2 if winner is p1 else p1
    print (f"{winner['name']} à gagner le match !")
    print (f"{loser['name']} à perdu le match et est donc éliminé du tournoi !")
    return winner

if __name__ == "__main__":
    players = tournament_choice()
    if players:
        # For simplicity, just play between first two players
        winner = all_game(players[0], players[1])
        print(f"Final winner: {winner['name']}")

