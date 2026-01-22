from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, name):
        super().__init__(name)
        # Baratheon.__init__(self, name)
        # Lannister.__init__(self, name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def set_eyes(self, color):
        self.eyes = color

    def get_eyes(self):
        return self.eyes

    def set_hairs(self, color):
        if hasattr(self, "hair"):
            del self.hair
        self.hairs = color

    def get_hairs(self):
        return self.hairs

# Joffrey = King("Joffrey")
# print("Sound be : \n{'first_name': 'Joffrey', \
# 'is_alive': True, 'family_name': 'Baratheon', 'eyes': \
# 'brown', 'hair': 'dark'}")
# print(Joffrey.__dict__)
# Joffrey.set_eyes("blue")
# Joffrey.set_hairs("light")
# print(Joffrey.get_eyes())
# print(Joffrey.get_hairs())
# print("Should be : \n{'first_name': 'Joffrey', 'is_alive': \
# True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}")
# print(Joffrey.__dict__)
