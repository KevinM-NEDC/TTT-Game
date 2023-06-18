class Card:
    """
    A class to represent a card in the game.
    """


class Weapon(Card):
    """
    A subtype of Card representing a weapon.
    """
    def __init__(self, *, name: str, damage: int, durability: int):
        self._name = name
        self._damage = damage
        self._durability = durability

        if self._damage < 0:
            raise ValueError('damage cannot be negative')
        if self._durability < 0:
            raise ValueError('durability cannot be negative')
    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage

    @property
    def durability(self):
        return self._durability

    def use(self):
        """Subtract a single durability from the weapon when used."""
        if self.durability == 0:
            raise AttributeError(f'this {self.name} has no uses')
        self._durability -= 1

    def is_broken(self):
        """Checks whether the weapon is broken"""
        return self.durability == 0

    def __repr__(self):
        return self.name


class Action(Card):
    """A subtype of Card representing an action"""
    def __repr__(self):
        return 'Action'


class BS(Card):
    """A subtype of Card representing BS cards"""
    def __init__(self, *, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self.name
