#!/usr/bin/env checkio --domain=py run the-healers

# https://py.checkio.org/mission/the-healers/

# 
# END_DESC

# Taken from mission The Lancers


# Taken from mission The Vampires


# Taken from mission The Defenders


# Taken from mission Army Battles


# Taken from mission The Warriors
from collections import UserList
from typing import Type, List


class Unit(object):
    HEALTH = None
    ATTACK = None
    DEFENSE = 0
    VAMPIRISM = 0
    HEAL = 0

    def __init__(self):
        self.health = getattr(self, 'HEALTH', None)
        self.attack = getattr(self, 'ATTACK', None)
        self.defence = getattr(self, 'DEFENSE')
        self.vampirism = getattr(self, 'VAMPIRISM')

    def __repr__(self):
        return f"{self.__class__.__name__}: h={self.health}"

    def protect(self, attack):
        hurt = max(int(attack - self.defence), 0)
        self.health -= hurt
        return hurt

    def heal_self(self, health):
        self.health = min(self.HEALTH, self.health + health)

    def regenerate(self, hurt):
        """
        :param hurt: really hurt for other unit
        :return:
        """
        self.heal_self(hurt * self.vampirism)

    @property
    def is_alive(self):
        return True if self.health > 0 else False

    def hit(self, my_army: 'Army', enemy: 'Army'):
        """
        Return True if kill unit
        :param my_army:
        :param enemy:
        :return:
        """
        enemy_first_unit = enemy.alive
        hurt = enemy_first_unit.protect(self.attack)
        self.regenerate(hurt)
        return not enemy_first_unit.is_alive

    def heal(self, ally: 'Unit'):
        ally.heal_self(self.HEAL)

    def passive_action(self, my_army: 'Army', enemy: 'Army'):
        """
        Some action if unit not in front of army
        :param attacker:
        :param defender:
        :return:
        """
        pass


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

    def hit(self, my_army: 'Army', enemy: 'Army'):
        super().hit(my_army, enemy)
        # Damage half damage to the second unit, if have
        if len(enemy.alive_units) >= 2:
            enemy.alive_units[1].protect(self.attack / 2)


class Healer(Warrior):
    HEALTH = 60
    ATTACK = 0
    HEAL = 2

    def passive_action(self, my_army: 'Army', enemy: 'Army'):
        my_ix = my_army.index(self)
        ally_ix = my_ix - 1
        if ally_ix >= 0:
            self.heal(my_army[ally_ix])


class Army(UserList):
    def __init__(self):
        super().__init__([])
        self.data: List[Unit] = []

    def add_units(self, type_: Type[Unit], count=1):
        units = [type_() for _ in range(count)]
        self.append_units(units)

    def append_units(self, units):
        if isinstance(units, Unit):
            units = [units]
        self.data += units

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
        return tuple(unit for unit in self.data if unit.is_alive)

    @property
    def is_alive(self):
        return bool(self.alive_units)

    def __repr__(self):
        return f"({'; '.join(map(str, self.data))})"


class Battle(object):
    def __init__(self):
        self.army_1 = None
        self.army_2 = None

    def fight(self, army_1, army_2):
        for _ in self.fight_iter(army_1, army_2):
            pass
        return self.result

    def fight_iter(self, army_or_unit_1, army_or_unit_2):
        self.army_1 = Army.convert_unit_to_army(army_or_unit_1)
        self.army_2 = Army.convert_unit_to_army(army_or_unit_2)

        attacker = self.army_1
        defender = self.army_2
        while self.army_1.is_alive and self.army_2.is_alive:
            # Back army actions
            for unit in attacker.alive_units:
                unit.passive_action(attacker, defender)
            # Front army battle
            kill = attacker.alive.hit(attacker, defender)
            if kill:
                attacker, defender = self.army_1, self.army_2
            else:
                attacker, defender = defender, attacker
            yield

    @property
    def result(self):
        return self.army_1.is_alive


fight = Battle().fight