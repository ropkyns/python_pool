class calculator:
    """Class for calculation of 2 vectors without instantiation"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """addition of the product of each elements with the same index"""
        res = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is : {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """addition of each elements of the list with the same index"""
        res = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """substraction of each elements of the list with the same index"""
        res = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous vector is : {res}")
