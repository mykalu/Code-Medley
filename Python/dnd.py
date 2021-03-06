import numpy as np

class Dice:
    """
    Object and utility class for simulating dice rolls.

    As an example, to roll and add the results of three twenty-sided dice
    (commonly notated as "3d20"):
    >>> from dnd import Dice as d
    >>> 3*d(20)
    23
    >>> 3*d(20)+3
    38

    """
    @staticmethod
    def roll_ability_scores():
        rolls = np.random.randint(1, 7, (6, 4))
        rolls.sort()
        rolls = rolls[:, 1:].sum(axis=-1)
        rolls.sort()
        return tuple(rolls[::-1])

    @staticmethod
    def roll_hit_points(num_faces, con, level):
        if not isinstance(num_faces, int) or num_faces < 1:
            raise ValueError("number of faces must be a positive integer")
        if not isinstance(con, int):
            raise ValueError("constitution modifier must be an integer")
        if not isinstance(level, int) or level < 1:
            raise ValueError("level must be a positive integer")
        return num_faces + con \
             + np.random.randint(1, num_faces+1, level-1).sum() \
             + con*(level-1)

    def __init__(self, num_faces):
        if not isinstance(num_faces, int) or num_faces < 1:
            raise ValueError("number of faces must be a positive integer")
        self.num_faces = num_faces

    def __rmul__(self, num_dice):
        if not isinstance(num_dice, int) or num_dice < 1:
            raise ValueError("number of dice must be a positive integer")
        return _Roll(num_dice, self.num_faces)

class _Roll:
    def __init__(self, num_dice, num_faces, modifier=0):
        self.num_dice = num_dice
        self.num_faces = num_faces
        self.modifier = modifier

    def __repr__(self):
        return str(sum(np.random.randint(1, self.num_faces+1, self.num_dice))
                 + self.modifier)

    def __add__(self, modifier):
        return self.__class__(self.num_dice, self.num_faces, modifier)

    def __mul__(self, factor):
        raise NotImplementedError

    def __truediv__(self, divisor):
        raise NotImplementedError

    def __floordiv__(self, divisor):
        raise NotImplementedError
