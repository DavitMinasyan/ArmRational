from math import copysign


def gcd(a, b):
    """Computes greatest common divisor of two values"""
    if b == 0:
        return a
    return gcd(b, a % b)


class Rational:
    """Representation of rational number
    >>> Rational(1,2)
    1/2
    >>> Rational(2,4)
    1/2
    >>> Rational(1,2) + Rational(3,4)
    5/4
    >>> Rational(-1,2)
    -1/2
    >>> Rational(5)
    5
    >>> float(Rational(3,4))
    0.75
    """

    def __init__(self, top=1, bottom=1):
        """Initializes Rational instance"""

        # do not allow 0 d
        if bottom == 0:
            raise ZeroDivisionError("Cannot have 0 d")

        # assign attribute values
        self.n = abs(top)
        self.d = abs(bottom)
        self.sign = copysign(1, top * bottom)

    def __add__(self, other):
        """
        Add two rational numbers.
        """
        x=int(self.sign*self.n*other.d+self.d*other.sign*other.n)
        y=self.d*other.d
        return Rational(x,y)

    def __sub__(self, other):
        """
        Sub two rational numbers.
        """
        x=int(self.sign*self.n*other.d-self.d*other.sign*other.n)
        y=self.d*other.d
        return Rational(x,y)

    def __mul__(self, other):
        """
        Mul two rational numbers.
        """
        x=int(self.sign*self.n*other.sign*other.n)
        y=self.d*other.d
        return Rational(x,y)

    def __divmod__(self, other):
        """
        Divmod two rational numbers.
        """
        x=int(self.sign*self.n*other.sign*other.d)
        y=self.d*other.n
        return Rational(x,y)

    def __str__(self):
        if self.sign < 0:
            return "{}{}/{}".format("-", self.n, self.d)
        return "{}/{}".format(self.n, self.d)



    __repr__ = __str__

    def __float__(self):
        pass


if __name__ == '__main__':
    import doctest

    # doctest.testmod()
    t = Rational(-1, 6)
    v = Rational(1, 3)
#    w = t+v

    print(t+v)
    print(t-v)
    print(t*v)
    print(t/v)

