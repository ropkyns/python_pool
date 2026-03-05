from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Abstract class constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method for class"""
        pass


class Stark(Character):
    """Stark subclass"""
    def __init__(self, first_name, is_alive=True):
        """Stark subclass constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Stark Subclass method changing is_alive value to False"""
        self.is_alive = False
        return
