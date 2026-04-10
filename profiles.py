#Création du profil du joueur.

def create_player(name, human = True) :
    player = {"name": name, "human": human, "wins": 0}
    return player


#Création du profil de l'IA.

def create_ia(name = "ia", human= False) :
    ia = {"name": name, "human": human, "wins": 0}
    return ia