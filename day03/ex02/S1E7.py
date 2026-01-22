from S1E9 import Character


class Baratheon(Character):
    first_name = None
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"
    """Your docstring for Class"""
    def is_alive(self) -> bool:
        """Your docstring for Method"""
        return self.is_alive

    def die(self) -> None:
        """Your docstring for Method"""
        self.is_alive = False

    def __str__(self) -> str:
        """Your docstring for Method"""
        return f"{self.first_name} {self.eyes} {self.hairs}"

    def __repr__(self) -> str:
        """Your docstring for Method"""
        return f'Vector: (\'\
            {self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'


class Lannister(Character):
    first_name = None
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"
    """Your docstring for Class"""
    def is_alive(self) -> bool:
        """Your docstring for Method"""
        pass

    def die(self) -> None:
        """Your docstring for Method"""
        pass

    def __str__(self) -> str:
        """Your docstring for Method"""
        return f"{self.first_name} {self.eyes} {self.hairs}"

    def __repr__(self) -> str:
        """Your docstring for Method"""
        return f'Vector: (\'\
            {self.family_name}\', \'{self.eyes}\', \'{self.hairs}\')'

    # decorator
    @classmethod
    def create_lannister(cls, name, is_alive=True):
        """Your docstring for Method"""
        instance = cls(name, is_alive)
        instance.family_name = "Lannister"
        instance.is_alive = is_alive
        return instance

# Robert = Baratheon("Robert")
# print(Robert.__dict__)
# print(Robert.__str__)
# print(Robert.__repr__)
# print(Robert.is_alive)
# Robert.die()
# print(Robert.is_alive)
# print(Robert.__doc__)
# print("---")
# Cersei = Lannister("Cersei")
# print(Cersei.__dict__)
# print(Cersei.__str__)
# print(Cersei.is_alive)
# print("---")
# J = Lannister.create_lannister("J", True)
# print(f"Name : {J.first_name, type(J).__name__}, Alive : {J.is_alive}")
