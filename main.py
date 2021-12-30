# This is a sample Python script.
import Characters
import GameContr


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_field(position):
#    field = [[0,0,0],[0,0,0],[0,0,0]]
#    field[position[1]][position[0]] = "X"
#    for i in field:
#        print(i),
#        print




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    game = GameContr.GameController()
    game.start_game(6, 6, 5)

