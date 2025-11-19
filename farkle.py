#!/bin/python

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculates the probability of outcomes for the game Farkle")
    parser.add_argument("numdice", type=int, help="The number of dice to roll")
    args = parser.parse_args()
    print(args)
