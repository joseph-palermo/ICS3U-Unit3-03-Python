#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program checks if the guessed number, imported by the user, is correct
# or incorrect


import constants
import random


def main():
    # This function asks the user to guess the number

    # input
    guess = int(input("Guess the number between 1 & 9 (integer): "))
    print("")

    # process
    if guess == constants.CORRECT_NUMBER:
        # output
        print("Correct!")
    else:
        print("Incorrect!")


if __name__ == "__main__":
    main()
