from Incinerator.the_lancers import *


def test_lancer():
    army1 = Army()
    army2 = Army()

    army1.add_units(Lancer, 1)
    army2.add_units(Warrior, 1)
    army2.add_units(Knight, 1)

    b = Battle().fight_iter(army1, army2)
    lancer = army1.alive_units[0]
    warrior, knight = army2.alive_units

    assert lancer.health == 50
    assert warrior.health == 50
    assert knight.health == 50

    next(b)

    assert lancer.health == 50
    assert warrior.health == 44  # 50 - 6
    assert knight.health == 47  # 50 - 6*05


def test_army_create():
    army = Army()
    assert Army.convert_unit_to_army(army) is army

    u = Warrior()
    a = Army.convert_unit_to_army(u)
    assert isinstance(a, Army)
    assert a.alive_units[0] is u


def test_fight_is_iterator():
    war1 = Warrior()
    war2 = Warrior()
    fiter = Battle().fight_iter(war1, war2)
    assert war1.health == 50
    assert war2.health == 50

    next(fiter)
    assert war1.health == 50
    assert war2.health == 50 - 5

    next(fiter)
    assert war1.health == 50 - 5
    assert war2.health == 50 - 5


def test_smoke_fight():
    chuck = Warrior()
    bruce = Warrior()
    assert fight(chuck, bruce) == True

    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True


def test_from_issue():
    battle = Battle()
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Lancer, 2)
    army_2.add_units(Warrior, 3)

    assert battle.fight(army_1, army_2) == True


def test_battle_smoke():
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False


def test_from_task_13():
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 11)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 13)
    battle = Battle()
    assert battle.fight(army_1, army_2) == True
