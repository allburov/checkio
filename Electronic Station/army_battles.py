#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run army-battles

# 
# END_DESC

# Taken from mission The Warriors


import itertools

from typing import NamedTuple, Type, List


class Unit(object):
    HEALTH = None
    ATTACK = None

    def __init__(self):
        self.__health = self.HEALTH

    def protect(self, damage):
        self.__health -= damage

    @property
    def is_alive(self):
        return True if self.__health > 0 else False

    @property
    def health(self):
        return self.__health


class Warrior(Unit):
    HEALTH = 50
    ATTACK = 5


class Knight(Warrior):
    HEALTH = 50
    ATTACK = 7


class Round(NamedTuple):
    round: int
    health_1: int
    health_2: int


class Fight(object):
    def __init__(self, unit_1, unit_2):
        self.unit_1: Unit = unit_1
        self.unit_2: Unit = unit_2

    def do_fight(self):
        print('Round - Unit1 - Unit2')
        attacker = self.unit_1
        defender = self.unit_2
        for round in itertools.count(1):
            defender.protect(attacker.ATTACK)
            print(f'{round} - {self.unit_1.health} - {self.unit_2.health}')
            if not defender.is_alive:
                break
            attacker, defender = defender, attacker

    @property
    def result(self):
        return self.unit_1.is_alive


def fight(unit_1, unit_2):
    f = Fight(unit_1, unit_2)
    f.do_fight()
    return f.result


class Army(object):
    def __init__(self):
        self.__units: List[Unit] = []

    def add_units(self, type: Type[Unit], count):
        self.__units = self.__units + [type() for _ in range(count)]

    @property
    def alive(self):
        return [unit for unit in self.__units if unit.is_alive]


class Battle(object):
    def fight(self, army_1, army_2):
        while army_1.alive and army_2.alive:
            fight(army_1.alive[0], army_2.alive[0])

        return bool(army_1.alive)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")