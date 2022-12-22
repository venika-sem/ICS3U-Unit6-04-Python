#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Dec 2022
# This program adds all numbers in a 2d array

import random


def add_numbers_in_2d_arrays(array):
    # Adds all of the numbers in a 2d array

    sum = 0
    for number in array:
        for number_alt in number:
            sum += number_alt

    return sum


def main():
    # Gets input, generates numbers and calls functions

    array_2d = []

    try:
        rows_text = input("\nEnter the amount of rows: ")
        rows_integer = int(rows_text)
        columns_text = input("Enter the amount of columns: ")
        columns_integer = int(columns_text)
        print("")
        for counter in range(0, rows_integer):
            column = []
            for counter_alt in range(0, columns_integer):
                random_number = random.randint(1, 50)
                column.append(random_number)
                print("{0} ".format(random_number), end="")
            array_2d.append(column)
            print("")
        sum_of_all_numbers = add_numbers_in_2d_arrays(array_2d)
        print("\nThe sum of these numbers is {}.".format(sum_of_all_numbers))
    except ValueError:
        print("\nInvalid Integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
