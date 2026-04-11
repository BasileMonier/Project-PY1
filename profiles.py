#Création du profil du joueur.

def create_player(name, human = True) :
    player = {"name": name, "human": human, "wins": 0}
    return player


#Création du profil de l'IA.

def create_ia(name = "ia", human= False) :
    ia = {"name": name, "human": human, "wins": 0}
    return ia


#Fonction pour avoir tous les joueurs (humain + IA)

def all_player (nb_players, tournament) :
    players = []
    for i in range (nb_players) :
        name = input(f"Nom du joueur {i+1} :")
        players.append(create_player(name))
    nb_ia = tournament - nb_players
    for ia in range(nb_ia) :
        name_ia = "IA_" + str(ia + 1)
        players.append(create_ia(name_ia))
    return players


#Choix du tournoi.

while True :
    tournament = int(input("Salut ! Tu souhaite créer un tournoi de 4, 8 ou 16 participants : "))
    if tournament == 4 or tournament == 8 or tournament == 16 :
       break
    else :
        print (" ")
        print ("Désolé mais le nombre n'est pas correct,recommence.")
        print (" ")


#Choix du nombres de joueurs (humain).

print (f"Très bien ! Il y aura donc {tournament} joueurs !")
while True :
    saisie = (input("Combien de joueur (humain) y'aura t'il : "))
    if saisie == "STOP" :
        break
    nb_players = int(saisie)
    if nb_players <= tournament :
        print ("Ok nickel, on peut passer aux noms des joueurs.")
        break
    else :
        print ("Le nombre est trop élevés, recommence ou écrit STOP pour arrêter.")