import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        if not kwargs:
            exit()

        def key_magic(diqtionary):
            return (f"{key} " * (diqtionary[key])).split()

        self.contents = list()
        for key in kwargs.keys():
            self.contents += key_magic(kwargs,key)


def experiment():
    pass


experiment()

bruh = Hat(red=5, blue=3)
print(bruh.contents)
