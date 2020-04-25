# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

import numpy as np
from carte import Carte


class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, barrier, way_out):
        self.robot = robot
        self.grille = {}
        self.barrier = "O"
        self.way_out = "U"
        self.door = "."
        self.position_update = []

    def check_next_case(
        self, x_position, command_position, show_map, map_array
    ):
        if map_array[command_position] == self.barrier:
            print("There is a barrier")

        elif map_array[command_position] == self.way_out:
            print("That's the way_out")
            print("")
            print("You win !!!")
            print("")
            Carte.delete_game()
            Carte.leave_game()

        elif map_array[command_position] == self.door:
            print("There is a door")
            print("")
            map_array[command_position] = "X"
            map_array[x_position[0], x_position[1]] = " "

        elif map_array[command_position] == " ":
            print("Movement of X")
            print("")
            map_array[command_position] = "X"
            map_array[x_position[0], x_position[1]] = " "

        else:
            print("There is an issue")
            print("")

    def movement(self, command, map_array, x_position, show_map):
        try:
            position_update = []

            if command == 'n':
                print("Movement to the North.")
                position_update = x_position[0]-1, x_position[1]

            elif command == 's':
                print("Movement to the South.")
                position_update = x_position[0]+1, x_position[1]

            elif command == 'e':
                print("Movement to the East.")
                position_update = x_position[0], x_position[1]+1

            elif command == 'o':
                print("Movement to the West.")
                position_update = x_position[0], x_position[1]-1

            self.check_next_case(
                x_position, position_update, show_map, map_array
            )

        except ValueError:
            print("You wrote too much Letters/Numbers.")

    def multi_movement(self, command, map_array, x_position, show_map):

        i = 0
        self.movement(command[1], map_array, x_position, show_map)
        print('\n'.join(
            ''.join(str(cell) for cell in row) for row in map_array
            ))
        print("")

        for i in range(int(command[0])-1):
            x_position = np.where(map_array == 'X')
            x_position = np.asarray(x_position)
            self.movement(command[1], map_array, x_position, show_map)
            print('\n'.join(
                ''.join(str(cell) for cell in row) for row in map_array
                ))
            print("")
            i += 1
