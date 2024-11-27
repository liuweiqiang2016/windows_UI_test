# This is a sample Python script.
import logging
import os
import sys
import time

class Hello:
    a = ''

    def init_data(self):
        self.a = 'xxxx'

    def get_data(self):
        print("==============" + self.a)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Hello()
    obj.init_data()
    obj.get_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
