#!/usr/bin/env checkio --domain=py run the-warlords

# https://py.checkio.org/mission/the-warlords/

# 
# END_DESC


from collections import UserList
from typing import Type, List, Optional

GAME_ATTR = ('health', 'attack', 'defense', 'vampirism', 'heal_power')


class Unit(object):
    HEALTH = None
    ATTACK = None
    DEFENSE = 0
    VAMPIRISM = 0
    HEAL_POWER = 0

    def __init__(self):
        self.health = getattr(self, 'HEALTH', None)
        self.attack = getattr(self, 'ATTACK', None)
        self.defense = getattr(self, 'DEFENSE')
        self.vampirism = getattr(self, 'VAMPIRISM')
        self.heal_power = getattr(self, 'HEAL_POWER')
        self.max_health = self.health

    def __repr__(self):
        # for attr in GAME_ATTR:
        return f"{self.__class__.__name__}: h={self.health}/{self.max_health};" + \
               f"a={self.attack};d={self.defense};v={self.vampirism};hp={self.heal_power}"

    def protect(self, attack):
        hurt = max(int(attack - self.defense), 0)
        self.health -= hurt
        return hurt

    def heal_self(self, health):
        health = int(health)
        self.health = min(self.max_health, self.health + health)

    def regenerate(self, hurt):
        """
        :param hurt: really hurt for other unit
        :return:
        """
        self.heal_self(hurt * self.vampirism / 100)

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
        kill = not enemy_first_unit.is_alive
        return kill

    def do_heal(self, ally: 'Unit'):
        if ally.is_alive:
            ally.heal_self(self.heal_power)

    def passive_action(self, my_army: 'Army', enemy: 'Army'):
        """
        Some action if unit not in front of army
        :param attacker:
        :param defender:
        :return:
        """
        pass

    def equip_weapon(self, weapon: 'Weapon'):
        for attr in GAME_ATTR:
            cur_val = getattr(self, attr)
            if cur_val == 0:
                continue
            value = cur_val + getattr(weapon, attr)
            value = max(0, value)
            setattr(self, attr, value)
        self.max_health += weapon.health


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
    VAMPIRISM = 50


class Lancer(Warrior):
    HEALTH = 50
    ATTACK = 6

    def hit(self, my_army: 'Army', enemy: 'Army'):
        # Damage half damage to the second unit, if have
        if len(enemy.alive_units) >= 2:
            enemy.alive_units[1].protect(self.attack / 2)
        return super().hit(my_army, enemy)


class Healer(Warrior):
    HEALTH = 60
    ATTACK = 0
    HEAL_POWER = 2

    def passive_action(self, my_army: 'Army', enemy: 'Army'):
        my_ix = my_army.alive_units.index(self)
        ally_ix = my_ix - 1
        if ally_ix >= 0:
            self.do_heal(my_army.alive_units[ally_ix])


class Warlord(Warrior):
    HEALTH = 100
    ATTACK = 4
    DEFENSE = 2


class Army(UserList):
    def __init__(self):
        super().__init__([])
        self.data: List[Unit] = []

    @property
    def units(self):
        return self.data

    def add_units(self, unit_cls: Type[Unit], count=1):
        if unit_cls is Warlord and self.warlord:
            return None
        if unit_cls is Warlord:
            count = 1
        units = [unit_cls() for _ in range(count)]
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
        return '\n'.join(map(str, self.data))

    @property
    def warlord(self):
        return any(map(lambda x: isinstance(x, Warlord), self.alive_units))

    def __move_unit(self, units, key=None, unit_cls: Optional[Type[Unit]] = None, pos=0):
        if unit_cls:
            key = lambda x: isinstance(x, unit_cls)

        for unit in reversed(units):
            if not key(unit):
                continue
            if unit in self.data:
                continue
            if pos == -1:
                self.data.append(unit)
            else:
                self.data.insert(pos, unit)

    def move_units(self):
        """
        :return:
        False - if not Warlord in army
        True - if have and move
        """
        if not self.warlord:
            return False

        units = list(self.data)
        self.data = []
        specific_rules = (Lancer, Healer, Warlord)
        # Dead first
        self.__move_unit(units, key=lambda x: x.health <= 0)

        # Bad unit first - not attack, but not Healer
        self.__move_unit(units, key=lambda x: type(x) not in specific_rules and x.attack == 0)

        # If there are no more Lancers in the army, but there are other soldiers who can deal damage,
        # they also should be placed in first position, and the Healer should stay in the 2nd row
        # (if army still has Healers).
        self.__move_unit(units, key=lambda x: type(x) not in specific_rules and x.attack > 0)

        # If there are Lancers in the army, they should be placed in front of everyone else.
        self.__move_unit(units, unit_cls=Lancer)

        # If there is a Healer in the army, he should be placed right after the first soldier to heal him during
        # the fight.
        # If the number of Healers is > 1, all of them should be placed right behind the first Healer.
        self.__move_unit(units, unit_cls=Healer, pos=1)

        # Warlord should always stay way in the back to look over the battle and rearrange the soldiers
        # when it's needed.
        self.__move_unit(units, unit_cls=Warlord, pos=-1)

        assert len(units) == len(self.data), "We have too much or less units :("
        return True


class Weapon(object):
    HEALTH = 0
    ATTACK = 0
    DEFENSE = 0
    VAMPIRISM = 0
    HEAL_POWER = 0

    def __init__(self, health=None, attack=None, defense=None, vampirism=None, heal_power=None):
        self.health = self.HEALTH if health is None else health
        self.attack = self.ATTACK if attack is None else attack
        self.defense = self.DEFENSE if defense is None else defense
        self.vampirism = self.VAMPIRISM if vampirism is None else vampirism
        self.heal_power = self.HEAL_POWER if heal_power is None else heal_power


class Sword(Weapon):
    HEALTH = +5
    ATTACK = +2


class Shield(Weapon):
    HEALTH = +20
    ATTACK = -1
    DEFENSE = +2


class GreatAxe(Weapon):
    HEALTH = -15
    ATTACK = +5
    DEFENSE = -2
    VAMPIRISM = +10


class Katana(Weapon):
    HEALTH = -20
    ATTACK = +6
    DEFENSE = -5
    VAMPIRISM = +50


class MagicWand(Weapon):
    HEALTH = +30
    ATTACK = +3
    HEAL_POWER = +3


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
                # The rearrangement is done not only before the battle, but during the battle too, each time the
                # allied units die.
                defender.move_units()
                attacker, defender = self.army_1, self.army_2
            else:
                attacker, defender = defender, attacker
            yield

    def straight_fight(self, army_1: Army, army_2: Army):
        while army_1.alive and army_2.alive:
            for sp1, sp2 in zip(army_1.alive_units, army_2.alive_units):
                self.fight(sp1, sp2)

        self.army_1 = army_1
        self.army_2 = army_2
        return self.result

    @property
    def result(self):
        return self.army_1.is_alive


fight = Battle().fight
