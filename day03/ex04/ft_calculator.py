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

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            print("Error: Vectors must be of the same length")
            return
        ret = 0
        for i in range(len(V1)):
            ret += V1[i] * V2[i]
        print(f'Dot product is: {ret}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            print("Error: Vectors must be of the same length")
            return
        ret = [V1[i] + V2[i] for i in range(len(V1))]
        print(f'Add Vector is: {ret}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            print("Error: Vectors must be of the same length")
            return
        ret = [V1[i] - V2[i] for i in range(len(V1))]
        print(f'Sous Vector is {ret}')

# a = [5, 10, 2]
# b = [2, 4, 3]
# calculator.dotproduct(a,b)
# calculator.add_vec(a,b)
# calculator.sous_vec(a,b)
