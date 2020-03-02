import sys
import pprint
from notebook import Note, Notebook
from menu import Menu


def show(lst):
    """
    Numerate elements of list to make it
    simpler for user to navigate
    :param lst: list
    :return: list(tuple)
    """
    return [val for val in enumerate(lst, 1)]


def curiosity():
    """
    Function for exploring classes; function has
    keywords "back" and "stop"
    :return: None
    """
    path = []
    class_list = [Menu, Note, Notebook]
    temp = class_list[:]
    pprint.pprint(show(temp))
    path.append(temp)
    while True:
        step = input("What do you want to explore next?(Enter number): ")
        if step == "back":
            path.pop()
            temp = path[-1]
            pprint.pprint(show(temp))
        elif step == "stop":
            sys.exit(0)
        try:
            step = int(step) - 1
        except ValueError:
            continue
        except IndexError:
            continue
        if isinstance(temp, list):
            temp = dir(temp[step])
            path.append(temp)
            pprint.pprint(show(temp))
        else:
            break


if __name__ == '__main__':
    curiosity()
