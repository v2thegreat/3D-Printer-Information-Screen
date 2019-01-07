"""
This is the main module, where the code is finally run

This module is saved as a .pyw so as to not show the terminal as it is
expected to start at runtime and the terminal can't be shown/should remain
in the background

================================================================================

This module imports Backend and creates an object, and runs it's show() function

As most of the code needed for running this is written there already, it is made
simple here
"""

from Backend import Backend


def main():
    Backend().show()


if __name__ == '__main__':
    main()
