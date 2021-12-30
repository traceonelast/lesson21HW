import random


class Terrain:

    def __init__(self, is_walkable, terrain):
        self.is_walkable = is_walkable
        self.terrain = terrain

    def step_on(self, unit):
        return False

    def is_walkable(self):
        return self.is_walkable

    def get_terrain(self):
        return self.terrain


class Door(Terrain):
    terrain = "Door"

    def __init__(self):
        self.is_walkable = True

    def step_on(self, unit):
        if unit.has_key():
            unit.escaped = True
            print("\nYou have found a way out, victory!")
            input("\nPress enter to continue")


class Key(Terrain):
    terrain = "Key"

    def __init__(self):
        self.is_walkable = True

    def step_on(self, unit):
        if unit.has_key() is False:
            unit.set_key()
            print("\n You found the key!")
            input("\nPress enter to continue")


class Trap(Terrain):
    terrain = "Trap"

    def __init__(self, damage):
        self.damage = damage
        self.is_walkable = True

    def step_on(self, unit):
        unit.get_damage(self.damage)
        print(f"\nYou trapped, damage{self.damage}!")
        input("\nPress enter to continue")


class TerrainGrass(Terrain):
    terrain = "Grass"

    def __init__(self):
        self.is_walkable = True


class Wall(Terrain):
    terrain = "Wall"

    def __init__(self):
        self.is_walkable = False


class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj


class Field:
    def __init__(self, cols, rows, unit, field):
        self.unit = unit
        self.cols = cols
        self.rows = rows
        self.field = field
        self.hero_on_door = False
        hero_set_position = False
        while hero_set_position is False:
            randx = random.randint(0, cols - 1)
            randy = random.randint(0, rows - 1)
            if self.field[randy][randx].get_obj().terrain == "Grass":
                self.unit.set_coordinates((randy, randx))
                self.field[randy][randx].set_obj(self.unit)
                hero_set_position = True

    def cell(self, coord):
        return self.field[coord[0]][coord[1]].get_obj()

    def move_unit_up(self):
        old_coord = self.unit.get_coordinates()
        if old_coord[0] == 0:
            return
        new_coord = (old_coord[0] - 1, old_coord[1])
        self._move_to(old_coord, new_coord)

    def move_unit_down(self):
        old_coord = self.unit.get_coordinates()
        if old_coord[0] == self.rows - 1:
            return
        new_coord = (old_coord[0] + 1, old_coord[1])
        self._move_to(old_coord, new_coord)

    def move_unit_left(self):
        old_coord = self.unit.get_coordinates()
        if old_coord[1] == 0:
            return
        new_coord = (old_coord[0], old_coord[1] - 1)
        self._move_to(old_coord, new_coord)

    def move_unit_right(self):
        old_coord = self.unit.get_coordinates()
        if old_coord[1] == self.cols - 1:
            return
        new_coord = (old_coord[0], old_coord[1] + 1)
        self._move_to(old_coord, new_coord)

    def _move_to(self, old_coord, new_coord):
        to_cell = self.cell(new_coord)

        if to_cell.is_walkable:
            to_cell.step_on(self.unit)
            if self.hero_on_door:
                self.field[old_coord[0]][old_coord[1]].set_obj(Door())
                self.hero_on_door = False
            else:
                self.field[old_coord[0]][old_coord[1]].set_obj(TerrainGrass())
            self.field[new_coord[0]][new_coord[1]].set_obj(self.unit)
            self.unit.set_coordinates(new_coord)
            if to_cell.get_terrain() == "Door":
                self.hero_on_door = True

        else:
            return

    def get_field(self):
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows
