from Dropbox.the_warlords import *


def test_lancer():
    army1 = Army()
    army2 = Army()

    army1.add_units(Lancer, 1)
    army2.add_units(Warrior, 1)
    army2.add_units(Knight, 1)

    battle_iter = Battle().fight_iter(army1, army2)
    lancer = army1.alive_units[0]
    warrior, knight = army2.alive_units

    assert lancer.health == 50
    assert warrior.health == 50
    assert knight.health == 50

    next(battle_iter)

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
    battle_iter = Battle().fight_iter(war1, war2)
    assert war1.health == 50
    assert war2.health == 50

    next(battle_iter)
    assert war1.health == 50
    assert war2.health == 50 - 5

    next(battle_iter)
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


def test_army_battles_example():
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 1)
    army_1.add_units(Knight, 2)
    army_2.add_units(Warrior, 2)
    army_2.add_units(Warrior, 1)
    battle = Battle()
    result = battle.fight(army_1, army_2)
    assert result is True


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


def test_army_list():
    army_1 = Army()
    v1 = Vampire()
    v2 = Vampire()
    v3 = Vampire()
    army_1.append_units([v1])
    army_1.append_units([v2])
    army_1.append_units([v3])
    army_1.add_units(Vampire, 10)
    assert army_1.index(v2) == 1


def test_the_healer_description():
    l = Lancer()
    w = Warrior()
    h = Healer()
    army1 = Army()
    army2 = Army()
    army1.append_units(l)
    army2.append_units(w)
    army2.append_units(h)
    battle = Battle()

    battle_iter = battle.fight_iter(army1, army2)

    next(battle_iter)
    assert w.health == 44
    assert h.health == 57
    assert l.health == 50

    next(battle_iter)
    assert w.health == 46
    assert h.health == 57
    assert l.health == 45


def test_the_healer_max():
    l = Lancer()
    w = Warrior()
    h = Healer()
    army1 = Army()
    army2 = Army()
    army1.append_units(l)
    army2.append_units(w)
    army2.append_units(h)
    battle_iter = Battle().fight_iter(army2, army1)
    next(battle_iter)
    assert w.health == 50
    assert h.health == 60
    assert l.health == 45


def test_the_healer():
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
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
    priest = Healer()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14
    priest.do_heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    assert Battle().fight(my_army, enemy_army) == False

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    assert Battle().fight(army_3, army_4) == True


def test_straight_fight_github_description():
    army_1 = Army()
    army_1.add_units(Warrior, 2)
    army_1.add_units(Knight, 1)
    army_2 = Army()
    army_2.add_units(Knight, 1)
    army_2.add_units(Healer, 1)
    army_2.add_units(Knight, 1)

    result = Battle().straight_fight(army_1, army_2)
    assert result is True


def test_straight_fight_github():
    chuck = Warrior()
    bruce = Warrior()
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
    priest = Healer()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14
    priest.do_heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    army_5 = Army()
    army_5.add_units(Warrior, 10)

    army_6 = Army()
    army_6.add_units(Warrior, 6)
    army_6.add_units(Lancer, 5)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    # assert battle.fight(army_3, army_4) == True
    assert battle.straight_fight(army_5, army_6) == False


def test_weapon_smoke():
    w = Warrior()
    sword = Sword()
    w.equip_weapon(sword)
    assert w.health == 55
    assert w.attack == 7

    w.equip_weapon(sword)
    assert w.health == 60
    assert w.attack == 9

    w_dead = Warrior()
    great_axe = GreatAxe()
    w_dead.equip_weapon(great_axe)
    w_dead.equip_weapon(great_axe)
    w_dead.equip_weapon(great_axe)
    w_dead.equip_weapon(great_axe)
    assert w_dead.is_alive is False


def test_weapon_vampire():
    w = Warrior()
    ga = GreatAxe()
    w.equip_weapon(ga)
    assert w.health == 35
    assert w.attack == 10
    assert w.vampirism == 0
    assert w.defense == 0


def test_the_weapons_6():
    weapon_1 = Sword()
    weapon_2 = GreatAxe()
    my_army = Army()
    my_army.add_units(Defender, 1)
    my_army.add_units(Warrior, 1)
    enemy_army = Army()
    enemy_army.add_units(Knight, 1)
    enemy_army.add_units(Healer, 1)
    my_army.units[0].equip_weapon(weapon_2)
    my_army.units[1].equip_weapon(weapon_2)
    enemy_army.units[0].equip_weapon(weapon_1)
    enemy_army.units[1].equip_weapon(weapon_1)
    battle = Battle()
    result = battle.fight(my_army, enemy_army)
    assert result is True


def test_the_weapons():
    ogre = Warrior()
    lancelot = Knight()
    richard = Defender()
    eric = Vampire()
    freelancer = Lancer()
    priest = Healer()

    sword = Sword()
    shield = Shield()
    axe = GreatAxe()
    katana = Katana()
    wand = MagicWand()
    super_weapon = Weapon(50, 10, 5, 150, 8)

    ogre.equip_weapon(sword)
    ogre.equip_weapon(shield)
    ogre.equip_weapon(super_weapon)
    lancelot.equip_weapon(super_weapon)
    richard.equip_weapon(shield)
    eric.equip_weapon(super_weapon)
    freelancer.equip_weapon(axe)
    freelancer.equip_weapon(katana)
    priest.equip_weapon(wand)
    priest.equip_weapon(shield)

    assert ogre.health == 125
    assert lancelot.attack == 17
    assert richard.defense == 4
    assert eric.vampirism == 200
    assert freelancer.health == 15
    assert priest.heal_power == 5

    assert fight(ogre, eric) == False
    assert fight(priest, richard) == False
    assert fight(lancelot, freelancer) == True

    my_army = Army()
    my_army.add_units(Knight, 1)
    my_army.add_units(Lancer, 1)

    enemy_army = Army()
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 1)

    my_army.units[0].equip_weapon(axe)
    my_army.units[1].equip_weapon(super_weapon)

    enemy_army.units[0].equip_weapon(katana)
    enemy_army.units[1].equip_weapon(wand)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True


def test_warlord_smoke():
    my_army = Army()
    my_army.add_units(Warrior, 2)
    assert my_army.warlord is False
    assert my_army.move_units() is False
    my_army.add_units(Warlord, 1)
    assert my_army.warlord is True

    assert my_army.move_units() is True

    my_army.add_units(Warlord, 1)
    assert len(my_army.units) == 3


def test_the_end_battle_warlord():
    ronald = Warlord()
    heimdall = Knight()

    assert fight(heimdall, ronald) == False

    my_army = Army()
    my_army.add_units(Warlord, 1)
    my_army.add_units(Warrior, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 2)

    enemy_army = Army()
    enemy_army.add_units(Warlord, 3)
    assert len(enemy_army.units) == 1
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 2)
    enemy_army.add_units(Knight, 2)

    my_army.move_units()
    enemy_army.move_units()

    assert type(my_army.units[0]) == Lancer
    assert type(my_army.units[1]) == Healer
    assert type(my_army.units[-1]) == Warlord

    assert type(enemy_army.units[0]) == Vampire
    assert type(enemy_army.units[-1]) == Warlord
    assert type(enemy_army.units[-2]) == Knight

    # 6, not 8, because only 1 Warlord per army could be
    assert len(enemy_army.units) == 6

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True


def test_the_warlords_24():
    army_1 = Army()
    army_2 = Army()

    army_1.add_units(Warrior, 2)
    army_1.add_units(Lancer, 2)
    army_1.add_units(Defender, 1)
    army_1.add_units(Warlord, 3)

    army_2.add_units(Warlord, 2)
    army_2.add_units(Vampire, 1)
    army_2.add_units(Healer, 5)
    army_2.add_units(Knight, 2)

    army_1.move_units()
    army_2.move_units()
    battle = Battle()
    assert battle.fight(army_1, army_2) is False
