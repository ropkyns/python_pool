from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing Joffrey"""
    def __init__(self, first_name, is_alive=True):
        """King subclass """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    @property
    def get_eyes(self):
        """Return the color of the eyes"""
        return self.eyes

    @get_eyes.setter
    def get_eyes(self, new_color):
        """Setting eyes to the new color"""
        self.eyes = new_color

    @property
    def get_hairs(self):
        """Return the color of the hairs"""
        return self.hairs

    @get_hairs.setter
    def get_hairs(self, new_color):
        """Setting hairs to the new color"""
        self.hairs = new_color

    def set_hairs(self, new_color):
        """Setting hairs to the new color"""
        self.hairs = new_color

    def set_eyes(self, new_color):
        """Setting eyes to the new color"""
        self.eyes = new_color

    def get_hairs(self):
        """Return the color of the hairs"""
        return self.hairs

    def get_eyes(self):
        """Return the color of the eyes"""
        return self.eyes
