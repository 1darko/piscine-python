from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    def __init__(self, name, is_alive=True) -> None:
        """Your docstring for Method"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def is_alive(self) -> bool:
        """Your docstring for Method"""
        pass

    @abstractmethod
    def die(self) -> None:
        """Your docstring for Method"""
        pass


class Stark(Character):
    """Your docstring for Class"""
    def is_alive(self) -> bool:
        """Your docstring for Method"""
        return self.is_alive

    def die(self) -> None:
        """Your docstring for Method"""
        self.is_alive = False

# Ned = Stark("Ned")
# print(Ned.__dict__)
# print(Ned.is_alive)
# Ned.die()
# print(Ned.is_alive)
# print(Ned.__doc__)
# print(Ned.__init__.__doc__)
# print(Ned.die.__doc__)
# print("---")
# Lyanna = Stark("Lyanna", False)
# print(Lyanna.__dict__)
