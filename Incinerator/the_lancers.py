#!/usr/bin/env checkio --domain=py run the-lancers

# https://py.checkio.org/mission/the-lancers/

# 
# END_DESC

# Taken from mission The Vampires


# Taken from mission The Defenders


# Taken from mission Army Battles


# Taken from mission The Warriors


import itertools

from typing import NamedTuple, Type, List


class Unit(object):
    HEALTH = None
    ATTACK = None
    DEFENSE = 0
    VAMPIRISM = 0

    def __init__(self):
        self.health = getattr(self, 'HEALTH', None)
        self.attack = getattr(self, 'ATTACK', None)
        self.defence = getattr(self, 'DEFENSE')
        self.vampirism = getattr(self, 'VAMPIRISM')

    def protect(self, unit):
        hurt = max((unit.attack - self.defence), 0)
        self.health -= hurt
        return hurt

    def regenerate(self, hurt):
        """
        :param hurt: really hurt for other unit
        :return:
        """
        self.health += hurt * self.vampirism

    @property
    def is_alive(self):
        return True if self.health > 0 else False

    def hit(self, my_army: 'Army', enemy: 'Army'):
        enemy_first_unit = enemy.alive
        hurt = enemy_first_unit.protect(self)
        self.regenerate(hurt)


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


class Vampire(Warrior):
    HEALTH = 40
    ATTACK = 4
    VAMPIRISM = 0.5


class Lancer(Warrior):
    HEALTH = 50
    ATTACK = 6


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


class Round(NamedTuple):
    round: int
    health_1: int
    health_2: int


class Fight(object):
    def __init__(self, unit_1, unit_2):
        self.unit_1: Unit = unit_1
        self.unit_2: Unit = unit_2


class Army(object):
    def __init__(self):
        self.__units: List[Unit] = []

    def add_units(self, type_: Type[Unit], count=1):
        units = [type_() for _ in range(count)]
        self.append_units(units)

    def append_units(self, units: List[Unit]):
        self.__units = self.__units + units

    @classmethod
    def convert_unit_to_army(cls, unit_or_army):
        if isinstance(unit_or_army, Army):
            return unit_or_army
        elif isinstance(unit_or_army, Unit):
            army = cls()
            army.append_units([unit_or_army])
            return army

    @property
    def alive(self):
        return self.alive_units[0] if self.alive_units else None

    @property
    def alive_units(self):
        return tuple(unit for unit in self.__units if unit.is_alive)

    @property
    def is_alive(self):
        return bool(self.alive_units)


class Battle(object):
    def __init__(self):
        self.army_1 = None
        self.army_2 = None

    def fight(self, army_1, army_2):
        for _ in self.fight_iter(army_1, army_2):
            pass
        return bool(self.army_1.alive)

    def fight_iter(self, army_1, army_2):
        army_1 = Army.convert_unit_to_army(army_1)
        army_2 = Army.convert_unit_to_army(army_2)
        self.army_1 = army_1
        self.army_2 = army_2

        while self.army_1.alive and self.army_2.alive:
            unit_1 = self.army_1.alive
            unit_2 = self.army_2.alive
            attacker = unit_1
            defender = unit_2
            for round_ in itertools.count(1):
                attacker.hit()
                # Hack for Lancer
                # if isinstance(attacker, Lancer) and len(defender.alive_units) >= 2:
                #     defender.alive_units[1].protect(attacker.attack / 2)

                yield
                if not defender.is_alive:
                    break
                attacker, defender = defender, attacker

    @property
    def result(self):
        return self.army_1.is_alive


fight = Battle().fight
