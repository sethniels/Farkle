#!/bin/python

import argparse

def PositiveInt (num):
    intval = int(num)
    if intval <= 0:
        raise ValueError(f"{num} is not a positive integer")
    return intval

def dice_combo_generator (numdice : int):
    curr_combo = [1] * numdice
    all_sixes = [6] * numdice
    while curr_combo != all_sixes:
        yield curr_combo
        curr_combo[0] += 1
        for i, die in enumerate(curr_combo):
            if die > 6:
                curr_combo[i+1] += 1
                curr_combo[i] = 1
    yield curr_combo

def get_points (dice):
    total = 100.0*dice.count(1) + 50.0*dice.count(5)
    print(f"{dice=}; {total=}")
    return total

def farkle (numdice : int):
    scoring_rolls = []
    for dice_combo in dice_combo_generator(numdice):
        points = get_points(dice_combo)
        print(f"{points=}; {scoring_rolls=}")
        if points:
            scoring_rolls.append(points)

    num_farkles = 6**numdice - len(scoring_rolls)
    break_even_score = sum(scoring_rolls) / num_farkles
    print(f"Current score must be less than or equal to {break_even_score} before rolling {numdice} dice")
    print(f"{num_farkles=}; ")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculates the probability "
            "of outcomes for the game Farkle")
    parser.add_argument("numdice", type=PositiveInt, help="The number of dice "
            "to roll")
    args = parser.parse_args()

    farkle(**vars(args))
