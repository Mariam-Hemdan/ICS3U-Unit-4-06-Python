#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This program using a continue statement


def main():
    # this program uses a nested loop

    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                print("RGB({0}, {1}, {2})".format(red, green, blue))


if __name__ == "__main__":
    main()
