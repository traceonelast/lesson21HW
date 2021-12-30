class Unit:
    hp = 100
    got_key = False
    coord = (0, 0)
    escaped = False

    def __init__(self, coord=(0, 0), hp=100):
        self.coord = coord
        self.hp = hp

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        self.has_escaped

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def get_damage(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            return "IS DEAD"
        else:
            return "TRAP! STILL ALIVE"

    def set_coordinates(self, coord):
        self.coord = coord

    def get_coordinates(self):
        return self.coord

    def has_position(self, pos):
        if self.coord is pos:
            return True
        else:
            return False


class Ghost(Unit):
    name = "Ghost"
