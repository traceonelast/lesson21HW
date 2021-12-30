import random
import FieldElements
import Characters


class GameController:
    mapping = None
    hero = None
    game_on = False
    field = None
    difficulty_level = 1

    def __init__(self):
        self.mapping = {
            'Wall': '🔲',
            'Grass': '⬜️',
            'Ghost': '👻',
            'Key': '🗝',
            'Door': '🚪',
            'Trap': '💀',
        }
        self.game_on = True

    def start_game(self, rows=10, cols=10, difficulty_level=1):
        self.difficulty_level = difficulty_level
        if self.difficulty_level > 10:
            self.difficulty_level = 10
        elif self.difficulty_level < 1:
            self.difficulty_level = 1
        self.hero = Characters.Ghost((0, 0), 100)
        self.make_field(rows, cols)
        self.play()
        if self.game_on is False: exit()

    def make_field(self, rows, cols):
        field = [[0 for j in range(cols)] for i in range(rows)]
        trap_count = int(rows * cols * (self.difficulty_level * 3 / 100))
        while trap_count != 0:
            randx = random.randint(0, cols - 1)
            randy = random.randint(0, rows - 1)
            if field[randy][randx] == 0:
                field[randy][randx] = FieldElements.Cell(FieldElements.Trap(random.randint(15, 50)))
                trap_count -= 1

        door_set = False
        while door_set is False:
            randx = random.randint(0, cols - 1)
            randy = random.randint(0, rows - 1)
            if field[randy][randx] == 0:
                field[randy][randx] = FieldElements.Cell(FieldElements.Door())
                door_set = True

        # key_set = False
        # while key_set is False:
        while True:
            randx = random.randint(0, cols - 1)
            randy = random.randint(0, rows - 1)
            if field[randy][randx] == 0:
                field[randy][randx] = FieldElements.Cell(FieldElements.Key())
                break
                # key_set = True
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] == 0: field[i][j] = FieldElements.Cell(FieldElements.TerrainGrass())

        self.field = FieldElements.Field(cols, rows, self.hero, field)

    def _print_field(self):
        for i in range(len(self.field.get_field())):
            temp = ""
            for j in range(len(self.field.get_field()[i])):
                temp_obj = self.field.cell((i, j))
                if temp_obj is self.hero:
                    temp += self.mapping.get("Ghost")
                else:
                    temp += self.mapping.get(temp_obj.get_terrain())
            print(temp)

    def _clr_scrn(self):
        clear = "\n" * 100
        print(clear)

    def play(self):
        while self.game_on:
            self._clr_scrn()
            self._print_field()
            print(f"\nHealt {self.hero.hp}, key {self.hero.has_key()}")
            temp = input("\npress w,a,s,d to move\n")
            if temp == "esc":
                game_on = False
                break
            elif temp == "w":
                self.field.move_unit_up()
            elif temp == "s":
                self.field.move_unit_down()
            elif temp == "a":
                self.field.move_unit_left()
            elif temp == "d":
                self.field.move_unit_right()
            if self.hero.is_alive() is False:
                print("\nYou dead, game over")
                self.game_on = False
                break
            if self.hero.escaped is True:
                print("\nYou win!")
                self.game_on = False
                break
