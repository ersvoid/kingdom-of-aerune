from random import randint


def build_hp(char):
    return


def build_mp(char):
    return char.get_lvl() * 10 + char.lvl * char.get_wis()


def value_mod(stat):
    if stat <= 3:
        return -4
    elif stat <= 5:
        return -3
    elif stat <= 7:
        return -2
    elif stat <= 9:
        return -1
    elif stat <= 11:
        return 0
    elif stat <= 13:
        return 1
    elif stat <= 15:
        return 2
    elif stat <= 17:
        return 3
    elif stat <= 19:
        return 4
    elif stat <= 21:
        return 5


class Character:

    def __init__(self, name, _str, _int, dex, wis, cha, con, magic, items, money=0, lvl=1, _id="player"):
        self.name = name
        self.lvl = lvl
        self.str = _str
        self.int = _int
        self.dex = dex
        self.wis = wis
        self.cha = cha
        self.con = con
        self.magic = magic
        self.items = items
        self.maxhp = 10 + (self.lvl * 1) + (self.con - 10)
        self.hp = self.maxhp
        self.maxmp = 10 + (self.lvl * 1) + (self.wis - 10)
        self.mp = self.maxmp
        self.sleep = False
        self.fire = 0
        self.money = money
        self.quest = 0
        self.xp = 0
        self.id = _id

    def get_lvl(self):
        return self.lvl

    def display_name(self):
        print("I am called ", self.name, "!")

    def get_str(self):
        val = value_mod(self.str)
        return val

    def get_int(self):
        val = value_mod(self.int)
        return val

    def get_dex(self):
        val = value_mod(self.dex)
        return val

    def get_wis(self):
        val = value_mod(self.wis)
        return val

    def get_cha(self):
        val = value_mod(self.cha)
        return val

    def get_con(self):
        val = value_mod(self.con)
        return val

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def attack(self):
        print("{} attacks!".format(self.name))
        return randint(1, 21) + self.get_str()

    def initiative(self):
        return randint(1,21) + self.get_dex()

    def ac_rating(self):
        try:
            val = 10 + self.get_dex() + self.items["armor"].val
        except:
            return val
        else:
            return 10 + self.get_dex()

    def reflex(self):
        return randint(1, 21) + self.get_dex()

    def fortitude(self):
        return randint(1, 21) + self.get_con()

    def will(self):
        return randint(1, 21) + self.get_wis()

    def take_damage(self, val):
        self.hp -= val
        print("{} has taken {} points of damage.".format(self.name, val))
        return self.hp

    def take_mp(self, cost):
        self.mp -= cost
        return self.mp

    def heal(self, val):
        self.hp += val
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print("{} has healed for {} HP.".format(self.name, val))
        return self.hp

    def rest(self, val):
        self.mp += val
        if self.mp > self.maxmp:
            self.mp = self.maxmp
        return self.mp

    def display_stats(self):
        print("Name: ", self.name, "\n", "HP: ", self.hp, "/", self.maxhp, "\n", "MP: ", self.mp, "/", self.maxmp, "\n"
              "Strength: ", self.str, "\n"
              "Intelligence: ", self.int, "\n"
              "Dexterity: ", self.dex, "\n"
              "Wisdom: ", self.wis, "\n"
              "Charisma: ", self.cha, "\n"
              "Constitution: ", self.con)
        print("You have a {} equipped.".format(self.items["weapon"].name))
        print("You are wearing {}.".format(self.items["armor"].name))
        print("You have {} gold pieces.".format(self.money))
        print("You have the following items in your rucksack:")
        for item in self.items["items"]:
            print(item.name)

    def __del__(self):
        pass

    def death_check(self):
        if self.hp <= 0:
            return True
        else:
            pass

    def damage(self, enemy):
        if self.items["weapon"].type == "weapon":
            val = randint(1, self.items["weapon"].item_value()) + self.get_str()
            if val < 0:
                return 0
            else:
                if self.items["weapon"].elem == "Magic":
                    if self.attack() + 5 > enemy.ac_rating():
                        return val + 10
                    else:
                        return 0
                elif self.items["weapon"].elem == "Fire":
                    if self.attack() + 5 > enemy.ac_rating():
                        enemy.fire = 5
                        return val + 10
                    else:
                        return 0
                elif self.items["weapon"].elem == "Death":
                    if enemy.will() < self.will():
                        a = enemy.hp % 2
                        return val + a
                    else:
                        return val
                else:
                    if self.attack() > enemy.ac_rating():
                        return val
                    else:
                        return 0
        elif self.items["weapon"].type == "staff":
            if self.items["weapon"].elem == "Magic":
                return 10
            elif self.items["weapon"].elem == "Fire":
                return 25
            elif self.items["weapon"].elem == "Death":
                return 15
            elif self.items["weapon"].elem == "Alter":
                return self.will()

    def reset(self):
        self.hp = self.maxhp
        self.mp = self.maxmp
        return self.hp, self.mp

    def win_gold(self, val):
        self.money += val
        print("You have won {}gp.".format(val))
        return self.money

    def spend_gold(self, val):
        self.money -= val
        print("You have lost {}gp.".format(val))
        return self.money

    def get_xp(self, val):
        self.xp += val
        return self.xp
