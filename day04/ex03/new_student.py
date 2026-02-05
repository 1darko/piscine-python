import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = field(init=False, default=True)
    id: str = field(init=False, default_factory=generate_id)
    login: str = field(init=False)

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError(f"Expected a string for \
                            name, got '{type(self.name).__name__}'")
        elif not isinstance(self.surname, str):
            raise TypeError(f"Expected a string for \
                            surname, got '{type(self.surname).__name__}'")
        elif not self.name or not self.surname:
            raise ValueError("Name and surname cannot be empty")
        elif not self.name.isalpha() or not self.surname.isalpha():
            raise ValueError("Name and surname \
                             must contain only alphabetic characters")
        self.login = self.name[0] + self.surname.lower()

# student = Student(name = "o", surname="BERNARD")
# print(student)
