#Création du profil du joueur.

def create_player(name, human = True) :
    player = {"name": name, "human": human, "wins": 0}
    return player


#Création du profil de l'IA.

def create_ia(name = "ia", human= False) :
    ia = {"name": name, "human": human, "wins": 0}
    return ia


#Fonction pour avoir tous les joueurs (humain + IA)

def all_player (nb_players, tournament_size) :
    players = []
    for i in range (nb_players) :
        name = input(f"Nom du joueur {i+1} : ")
        players.append(create_player(name))
    
    nb_ia = tournament_size - nb_players
    for ia in range(nb_ia) :
        name_ia = "IA_" + str(ia + 1)
        players.append(create_ia(name_ia))
    
    return players


#Choix du tournoi.

def tournament_choice():
    while True :
        try:
            tournament = int(input("Salut ! Tu souhaite créer un tournoi de 4, 8 ou 16 participants ? : "))
            if tournament == 4 or tournament == 8 or tournament == 16:
                break
            print (" ")
            print ("Désolé mais le nombre n'est pas correct,recommence.")
            print (" ")
        except ValueError:
            print ("Vous devez entrer un nombre entier")
    
    print (f"Très bien ! Il y aura donc {tournament} joueurs !")
    while True :
        saisie = (input("Combien de joueur (humain) y'aura t'il (ou STOP pour quitter) : "))
        if saisie == "STOP":
            break
        try:
            nb_players = int(saisie)
            if nb_players <= tournament:
                print("Ok nickel, on peut passer aux noms des joueurs. \n")
                break
            print("Le nombre est trop élevé, recommence ou écrit STOP pour arrêter.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    return all_player(nb_players, tournament)
