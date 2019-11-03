#!/usr/bin/env checkio --domain=py run 3-chefs

# https://py.checkio.org/mission/3-chefs/

# You are the owner of a cafe where 3 chefs work: a JapaneseCook, RussianCook and ItalianCook. Each of them can prepare the national food and beverage:
# - JapaneseCook: Sushi and Tea;
# - RussianCook: Dumplings and Compote;
# - ItalianCook: Pizza and Juice.
# Your task is to create 3 different subclasses (one for each chef) which are the children of an AbstractCook and have these methods:
# - add_food(food_amount, food_price), which add to the client's order the value of the food which he had chosen;
# - add_drink(drink_amount, drink_price), which add to the client's order the value of the drink which he had chosen;
# - total(), which returns a string like: 'Foods: 150, Drinks: 50, Total: 200', and for the each chef instead of the Foods and Drinks will be the national food and drink that he’s used.
# Every client can choose only one chef.In this mission theAbstract Factorydesign pattern could help.
# 
# Example:
# client_1 = JapaneseCook()
# client_1.add_food(2, 20)
# client_1.add_drink(5, 4)
# client_1.total() == "Sushi: 40, Tea: 20, Total: 60"
# 
# client_2 = RussianCook()
# client_2.add_food(1, 40)
# client_2.add_drink(5, 20)
# client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"
# 
# client_3 = ItalianCook()
# client_3.add_food(2, 20)
# client_3.add_drink(2, 10)
# client_3.total() == "Pizza: 40, Juice: 20, Total: 60"
# 
# 
# 
# All data here will be correct and you don't need to implement the value checking.
# 
# Input:Statements and expressions of the 3 chefs’ classes.
# 
# Output:The behaviour as described.
# 
# Precondition:All data is correct.
# 
# 
# END_DESC
import abc
from collections import defaultdict
from functools import partialmethod, partial
from typing import Dict, Callable


class AbstractCook(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def _name_maps(self) -> Dict[str, str]:
        pass

    def __init__(self, ):
        self._total = defaultdict(int)

    def __add(self, type_, count, price):
        self._total[type_] += count * price
        self._total['total'] += count * price

    add_food: Callable = partialmethod(__add, 'food')
    add_drink: Callable = partialmethod(__add, 'drink')

    def total(self):
        order = ('food', 'drink', 'total')
        return ", ".join(
            f'{self._name_maps.get(x, x).title()}: {self._total[x]}'
            for x in order
        )


class JapaneseCook(AbstractCook):
    @property
    def _name_maps(self) -> Dict[str, str]:
        return dict(food='sushi', drink='tea')


class RussianCook(AbstractCook):
    @property
    def _name_maps(self) -> Dict[str, str]:
        return dict(food='dumplings', drink='compote')


class ItalianCook(AbstractCook):
    @property
    def _name_maps(self) -> Dict[str, str]:
        return dict(food='pizza', drink='juice')


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
