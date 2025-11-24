#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Nov 23rd, 2025
# this program uses nested loops
# to print out all the valid RGB colours.


def main():

    for r in range(0, 255, 1):  # Red component
        for g in range(0, 255, 1):  # Green component
            for b in range(0, 255, 1):  # Blue component
                # ANSI escape code to set text color
                print(f"\033[38;2;{r};{g};{b}mRGB({r}, {g}, {b})\033[0m")
                # Reset to default color after printing
    print("\nDone printing all RGB colours.")


if __name__ == "__main__":
    main()
# Example code to print text in RGB color:
# r = 255
# g = 0
# b = 0
