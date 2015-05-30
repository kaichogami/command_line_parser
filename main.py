"""Main module for command line parser. To enter the interface, just execute this file."""

from __future__ import print_function
from base import base


if __name__ == '__main__':
    while 1:
        print("kaichogami $:~/", end = ' ')
        value = raw_input()
        obj = base(value)
        obj.do()
