# -*-coding:Utf-8 -*
#!/usr/bin/env python3


import os
import sys
import numpy as np

# import files arround roboc.py
from carte import Carte
from labyrinthe import Labyrinthe

# Name of the event file to find if the game is open or not
name_file_histo = "histo"
line_tab = []

"""
********************************************************************************
********************************************************************************
"""

map_game = []
line_tab = []
show_map = []


def choose_map_game():
    list_name_file = []
    i = 0

    print("Existing mazes :")
    print("")

    for name_file in os.listdir("cartes"):
        if name_file.endswith(".txt"):
            chemin = os.path.join("cartes", name_file)
            nom_carte = name_file[:-3].lower()
            list_name_file.append(nom_carte)
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                map_game.append(contenu)
        # Create a map_game.. need to be completed

    j = len(list_name_file)

    while i < j:
        print(f"     {i + 1} - {list_name_file[i]}")
        i += 1
    print(" ")

    asking_number = True

    while asking_number:
        try:
            print("")
            number_choose = int(input("Enter a number to select the maze : "))
            # Check if the number is correct and no higher to the map_games number
            if int(number_choose) > j:
                print("The number typed is higher of the map_games number.")
            else:
                asking_number=False
        except ValueError:
            print("Only letters beetween 1 to",j,"are allowed")

        # Show the map_game selected
    print("")
    print(map_game[int(number_choose) - 1])
    show_map = map_game[int(number_choose) - 1]
    line_tab.extend(show_map[:].split('\n'))


"""
********************************************************************************
********************************************************************************
"""

# if a save game, we show it, if not we continue


def check_if_game_session_open():
    if os.path.exists(name_file_histo):  # If the file exist we collect it
        file_histo = open(name_file_histo, "rb")
        # mon_depickler = pickle.Unpickler(file_histo)
        if os.stat(name_file_histo).st_size == 0:
            print("No game running.")
            choose_map_game()

        else:
            valide_selection=True
            while valide_selection:
                try:
                    print(" ")
                    print(
                        "A party is saved, do you want to continue? "
                        "(Y/N)"
                    )
                    selection = input()
                    if selection.lower() == 'y':
                        print("we'll continue the party")
                        map_game = Carte.load_game(file_histo)
                        map_game = str('\n' .join(
                                    ''.join(str(
                                        cell) for cell in row
                                        ) for row in map_game
                                    ))
                        print(map_game)
                        line_tab.extend(map_game[:].split('\n'))
                        valide_selection=False

                    elif selection.lower() == 'n':
                        print("New game")
                        Carte.delete_game()
                        print("Old party deleted.")
                        choose_map_game()
                        valide_selection=False
                    else:
                        print("You wrote a wrong command. Please retry.")
                except ValueError:
                    print("problem")

    else:  # The file doesn't exist
        histo = {}


"""
********************************************************************************
********************************************************************************
"""


continue_game = True

map_game_array = []
list_commands = ['e', 'o', 's', 'n', 'q']

histo = check_if_game_session_open()

while continue_game:
    try:

        nb_line_tab = len(line_tab)
        j = 0
        # If beginning of the game map_game_array needs to be list type
        if issubclass(type(map_game_array), list):
            for j in range(nb_line_tab):
                map_game_array.append(list(line_tab[j].strip()))
                j += 1
            map_game_array = np.asarray(map_game_array)

        # find position of X :
        x_position = np.where(map_game_array == 'X')
        x_position = np.asarray(x_position)

        # find position of U :
        u_position = np.where(map_game_array == 'U')
        u_position = np.asarray(u_position)

        # find position of O :
        o_position = np.where(map_game_array == 'O')
        o_position = np.asarray(o_position)

        execute_main = Labyrinthe(x_position, o_position, u_position)
        command = str(input().lower())

        if command == 'q':
            Carte.save_game(map_game_array)
            Carte.leave_game()
            sys.exit()

        elif len(command) == 1:
            print("")
            if command in list_commands:
                execute_main.movement(
                    command, map_game_array, x_position, show_map
                )
            else:
                print("you typed a wrong Letter")
                print("Restart :")
            print("")
            print(
                '\n'.join(
                    ''.join(
                        str(cell) for cell in row
                    ) for row in map_game_array
                )
            )
            print("")

        elif len(command) == 2:
            print("")
            print(
                '\n'.join(
                    ''.join(
                        str(cell) for cell in row
                    ) for row in map_game_array
                )
            )
            print("")
            if int(command[0]) < 10:
                if command[1] in list_commands:
                    execute_main.multi_movement(
                        command, map_game_array, x_position, show_map
                    )
                else:
                    print("the number of movements needs to be less than 10.")
            else:
                print("You typed a wrong command.")

        else:
            print("You typed (or not) a wrong command.")
    except ValueError:
        print('\n'.join(
            ''.join(str(cell) for cell in row) for row in map_game_array)
            )
        print("")
        print("You typed a wrong command.")
        print("Restart :")
        print("")
        print(
            '\n'.join(
                ''.join(
                    str(cell) for cell in row
                ) for row in map_game_array
            )
        )

        # x_position = Labyrinthe.check_next_case.command_position
        # print(x_position)

"""
********************************************************************************
********************************************************************************
"""

os.system("pause")
