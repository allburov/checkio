#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run the-warriors

# 
# END_DESC

import itertools

from typing import NamedTuple


class Unit(object):
    HEALTH = None
    ATTACK = None

    def __init__(self):
        self.__health = self.HEALTH

    def protect(self, damage):
        self.__health -= damage

    @property
    def is_alive(self):
        return self.__health > 0

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


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")