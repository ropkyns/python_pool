class calculator:
    """Class for calculation of vector"""
    vector = []

    def __init__(self, value):
        self.vector = value

    def __add__(self, object) -> None:
        """addition of object to each element of vector"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """multilplication of object to each element of vector"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """substraction of object to each element of vector"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """true division of object to each element of vector"""
        assert object != 0, "Can't divide by 0"
        self.vector = [x / object for x in self.vector]
        print(self.vector)
