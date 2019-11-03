#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run the-defenders

# 
# END_DESC

# Taken from mission Army Battles


# Taken from mission The Warriors


import itertools

from typing import NamedTuple, Type, List


class Unit(object):
    HEALTH = None
    ATTACK = None
    DEFENSE = 0

    def __init__(self):
        self.health = getattr(self, 'HEALTH', None)
        self.attack = getattr(self, 'ATTACK', None)
        self.defence = getattr(self, 'DEFENSE')

    def protect(self, damage):
        self.health -= max((damage - self.defence), 0)

    @property
    def is_alive(self):
        return True if self.health > 0 else False


class Warrior(Unit):
    HEALTH = 50
    ATTACK = 5


class Knight(Warrior):
    HEALTH = 50
    ATTACK = 7


class Defender(Warrior):
    HEALTH = 60
    ATTACK = 3
    DEFENSE = 2


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
            defender.protect(attacker.attack)
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


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    rookie = Rookie()
    defender = Defender()
    assert rookie.health == 50
    assert rookie.attack == 1
    fight(defender, rookie)
    assert defender.health == 60

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")