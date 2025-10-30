"""
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module contains functions that calculate baking times
for Guido's gorgeous lasagna recipe.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2     # in minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    This function takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of lasagna layers being prepared.
    :return: int - total preparation time (in minutes).

    Each layer of lasagna takes `PREPARATION_TIME` minutes to prepare.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param number_of_layers: int - number of lasagna layers being prepared.
    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - total time spent (in minutes).

    This function returns the sum of the preparation time and the time
    the lasagna has already spent baking in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
