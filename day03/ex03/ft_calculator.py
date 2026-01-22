class calculator:
    array = []

    def __init__(self, input: list) -> None:
        self.array = input

    def print_array(self) -> None:
        print(self.array)

    def __add__(self, object) -> None:
        self.array = [i + object for i in self.array]
        print(self.array)

    def __mul__(self, object) -> None:
        self.array = [i * object for i in self.array]
        print(self.array)

    def __sub__(self, object) -> None:
        self.array = [i - object for i in self.array]
        print(self.array)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: Division by zero")
            return

        self.array = [i / object for i in self.array]
        print(self.array)

# v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v1 + 5
# print("---")
# v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v2 * 3.45
# print("---")
# v3 = calculator([10.0, 15.0, 20.0])
# v3 - 5
# v3 / 0
