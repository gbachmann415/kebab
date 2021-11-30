"""
A dataclass that represents "spots" on the skewer and functions that work
with it.

author: RITCS
author: Gunnar Bachmann
"""

from dataclasses import dataclass
from typing import Union
from food import Food

@dataclass
class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a Food 'item',
        and a reference to the 'next' spot.
    """
    item: Food
    next: Union[None, 'KebabSpot']


def spot_create(item, next):
    """
    Create a new food item spot on the skewer
    :param item (Food): new food item
    :param next: next spot
    :return: new spot
    """
    return KebabSpot(item, next)


def spot_name(spot):
    """
    Return the name of the food item in this spot.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: food name
    """
    return spot.item.name


def spot_size(spot):
    """
    Return the number of elements from this KebabSpot instance to the end
    of the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: the number of elements (int)
    """
    if spot == None:
        return 0
    else:
        count = 0
        while spot is not None:
            count += 1
            spot = spot.next
    return count


def spot_has(spot, name):
    """
    Return whether there are is a food item from this spot to the end of
    the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :param name: the name (string) being searched for.
    :return True if any of the spots hold a Food item that equals the
    name, False otherwise.
    """
    if spot == None:
        return False
    elif spot.item.name == name:
        return True
    else:
        return spot_has(spot.next, name)


def spot_string_em(spot):
    """
    Return a string that contains the list of items in the skewer from
    this spot down, with a comma after each entry.
    :param: spot (KebabSpot): the current spot on the skewer
    :return A string containing the names of each of the Food items from
    this spot down.
    """
    lst = ""
    while spot is not None:
        if spot.next == None:
            lst += spot.item.name
            spot = spot.next
        else:
            lst += spot.item.name + ", "
            spot = spot.next
    return lst


def total_calories(kebab):
    """
    Calculates the amount of calories the kebab
    contains, and returns that value.
    :param kebab:
    :return:
    """
    if kebab == None:
        return 0
    else:
        calories = 0
        while kebab is not None:
            calories += kebab.item.calories
            kebab = kebab.next
    return calories


def is_vegan(kebab):
    """
    Determines whether the kebab is vegan or not, returning
    True if it is vegan and False if it is not. It is not vegan
    if the kebab contains beef, pork, or chicken.
    :param kebab:
    :return:
    """
    if kebab is None:
        return True
    elif kebab.item.name == 'beef' or kebab.item.name == 'pork' or kebab.item.name == 'chicken':
        return False
    else:
        return True