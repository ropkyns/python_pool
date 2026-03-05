from S1E9 import Character


class Baratheon(Character):
    """Representing Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Baratheon subclass """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """New__str__s method """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """New __repr__ method"""
        return f"vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Baratheon submethod changing is_alive to False"""
        self.is_alive = False


class Lannister(Character):
    """Representing Lannister family"""
    def __init__(self, first_name, is_alive=True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Lannister class method to create a Lannister member"""
        lannister = cls(first_name, is_alive)
        return lannister

    def die(self):
        """Lannister submethod changing is_alive to False"""
        self.is_alive = False
        return
