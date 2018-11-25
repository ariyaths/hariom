import math
import collections
import turtle as t


# def path(filename):
#     import os
#     filepath = os.path.realpath(__file__)
#     dirpath = os.path.dirname(filepath)
#     fullpath = os.path.join(dirpath, filepath)
#     return fullpath


def floor(value, size, offset=200):
    return float(((value + offset) // size) * size - offset)


def line(a, b, x, y):
    t.up()
    t.goto(a, b)
    t.down()
    t.goto(x, y)


def square(x, y, size, name):
    t.up()
    t.goto(x, y)
    t.down()
    t.color(name)
    t.begin_fill()
    for count in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


class vector(collections.Sequence):
    precision = 6
    __slots__ = ("_x", "_y", "_hash")

    def __init__(self, x, y):
        self._hash = None
        self._x = round(x, self.precision)
        self._y = round(y, self.precision)

    # means getter
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if self._hash is not None:
            raise ValueError("Cannot set x after hashing")
        self._x = round(value, self.precision)

    # means getter
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError("Cannot set y after hashing")
        self._y = round(value, self.precision)

    def __hash__(self):
        # v.__hash__() -> hash(v)
        # v = vector(1, 2)
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError

    def copy(self):
        type_self = type(self)
        return type_self(self.x, self.y)

    def __eq__(self, other):
        # v = w if v vector(1, 2) = w = vector(1, 2)
        if isinstance(other, vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, vector):
            return self.x != other.x and self.y != other.y
        return NotImplemented

    def __iadd__(self, other):
        # v.__iadd__(w) -> v += w
        if self._hash is not None:
            raise ValueError("Cannot add vector after hashing")
        elif isinstance(other, vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

    def __add__(self, other):
        # v.__add__(w) -> v + w
        copy = self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(self, other):
        # this is going to move the vector (in place)
        # eg: v = vector(1,2), w = vector(3,4)... v.move(w) v ==> vector(4,6)
        self.__iadd__(other)

    def __isub__(self, other):
        # v.__isub__(w) -> v -= w
        if self._hash is not None:
            raise ValueError("Cannot subtract vector after hashing")
        elif isinstance(other, vector):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

    def __sub__(self, other):
        # v.__sub__(w) -> v - w
        copy = self.copy()
        return copy.__isub__(other)

    def __imul__(self, other):
        # v.__imul__(w) => v *= w
        if self._hash is not None:
            raise ValueError("Cannot multiply vector after hashing")
        elif isinstance(other, vector):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self

    def __mul__(self, other):
        # v.__mul__(w) => v * w
        copy = self.copy()
        return copy.__imul__(other)

    __rmul__ = __mul__

    def scale(self, other):
        self.__imul__(other)

    def __itruediv__(self, other):
        # v.__itruediv__(w) => v /= w
        if self._hash is not None:
            raise ValueError("Cannot divide vector after hashing")
        elif isinstance(other, vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.x /= other
        return self

    def __truediv__(self, other):
        # v.__truediv__(w) => v / w
        copy = self.copy()
        return copy.__itruediv__(other)

    def __neg__(self):
        # v.__neg__(w) => -v
        copy = self.copy()
        copy.x = -copy.x
        copy.y = -copy.y
        return copy

    def __abs__(self):
        # vector(3, 4) => 5
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def rotate(self, angle):
        if self._hash is not None:
            raise ValueError("Cannot rotate vector after hashing")
        radians = angle * math.pi / 180.0
        cosine = math.cos(radians)
        sine = math.sin(radians)
        x = self.x
        y = self.y
        self.x = x * cosine - y * sine
        self.y = y * cosine + x * sine

    def __repr__(self):
        # v.__repr__() => repr(v)
        type_self = type(self)
        name = type_self.__name__
        return "{}({!r}, {!r})".format(name, self.x, self.y)
