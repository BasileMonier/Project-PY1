from profiles import tournament_choice
import random

# Choix de la personne, soit humain soit IA, et verifie que le choix est correct.
def choice(person) :
    if person["human"] == True :
        while True :
            print ("\n Choisissez entre 🗿  Pierre, 🍃  Feuille et ✂️  Ciseaux.")
            player_choice = input("> ")
            print ("_" * 70)
            if player_choice in ["Pierre", "Feuille", "Ciseaux"] :
                print (f"\n {person['name']} a choisi : {player_choice}")
                return player_choice
            else :
                print ("\n Cette valeur est incorrect, reessaye s'il te plait !")
    if person["human"] == False :
        ia_choice = random.choice (["Pierre", "Feuille", "Ciseaux"])
        print(f"\n {person['name']} a choisi : {ia_choice}")
        return ia_choice

# Fonction déroulement d'une partie, affiche le gagnant ou une égalité, et retourne le gagnant.
def game_1 (p1, p2) :
    p1_play = choice(p1)
    p2_play = choice(p2)
    choice_win = {"Pierre": "Ciseaux", "Feuille": "Pierre", "Ciseaux": "Feuille"}
    if p1_play == p2_play :
        print ("\n Égalité, vous avez fais pareil.")
        print ("\n Passons à la prochaine manche !")
        print ("_" * 70)
        return None
    if choice_win[p1_play] == p2_play :
        print (f"\n {p1['name']} a gagné cette manche !")
        print ("\n Passons à la prochaine manche !")
        print ("_" * 70)
        return p1
    if choice_win[p1_play] != p2_play :
        print (f"\n {p2['name']} a gagné cette manche !")
        print ("\n Passons à la prochaine manche !")
        print ("_" * 70)
        return p2

# Règle du match, le premier à gagner 3 manches l'emporte, affiche le gagnant et le perdant, et retourne le gagnant.
def all_game (p1, p2) :
    p1_score = 0
    p2_score = 0
    print(f"\n {p1['name']} contre {p2['name']}")

    while p1_score < 3 and p2_score < 3 :
        game = game_1(p1, p2)
        if game == None :
            continue
        if game == p1 :
            p1_score += 1
        if game == p2 :
            p2_score += 1
        print(f"\n Score : {p1['name']} : {p1_score} - {p2_score} : {p2['name']}")
        print("_"*70)

    winner = p1 if p1_score == 3 else p2
    loser = p2 if winner is p1 else p1
    print (f"\n {winner['name']} a gagné le match !")
    print (f"\n {loser['name']} a perdu le match et est donc éliminé du tournoi !")
    print("_"*70)
    return winner

# Déroulement du tournoi, les joueurs s'affontent par pairs, la fonction fait une liste avec les gagnants de chaque match, jusqu'à ce qu'il ne reste qu'un seul joueur, le vainqueur du tournoi.
def tournament_start(players):
    print("_"*70)
    print(f"\n🏆 Le tournoi commence avec {len(players)} joueurs. Que le meilleur gagne !  🏆")
    print("_"*70)
    tour = 1
    
    while len(players) > 1:
        players_next_round = []

        for i in range(0, len(players), 2):
            r = all_game(players[i], players[i + 1])
            players_next_round.append(r)
        
        players = players_next_round
        tour += 1

    print("\n" + "="*70)
    print(f"\n👑 {players[0]['name']} remporte la finale, il est le grand champion du tournoi !  👑")
    print("\n" + "="*70)
    return players[0]


players = tournament_choice()
if players:
    tournament_start(players)
