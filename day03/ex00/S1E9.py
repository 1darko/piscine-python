from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    def __init__(self, name, is_alive=True) -> None:
        """Your docstring for Method"""
        self.name = name
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
