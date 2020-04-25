# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
import pickle


class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        # self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def save_game(name_file_histo, map_array):
        print("Game saved !")
        # We erase the last score
        file_histo = open(name_file_histo, "wb")
        pickle.dump(map_array, file_histo)
        file_histo.close()
        pass

    def leave_game():
        print("Game finished !")
        pass

    def load_game(file_histo):
        print("Game loaded !")
        game_loaded = pickle.load(file_histo)
        return game_loaded
        file_histo.close()

    def delete_game(name_file_histo):
        file_histo = open(name_file_histo, "wb")
        pickle.dump(" ", file_histo)
        file_histo.close()
