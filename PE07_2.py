# PE07_2 - Operator Overloading
# Adding full comments as required

class Number:
    """Class that supports operator overloading for +, -, *, /."""

    def __init__(self, value):
        self.value = value

    # task: overload +
    def __add__(self, other):
        """Add two Number objects."""
        return Number(self.value + other.value)

    # task: overload -
    def __sub__(self, other):
        """Subtract two Number objects."""
        return Number(self.value - other.value)

    # task: overload *
    def __mul__(self, other):
        """Multiply two Number objects."""
        return Number(self.value * other.value)

    # task: overload /
    def __truediv__(self, other):
        """Divide two Number objects."""
        if other.value == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Number(self.value / other.value)

    def __str__(self):
        return str(self.value)


# ----------- Test Code -----------
n1 = Number(20)
n2 = Number(5)

print("n1 + n2 =", n1 + n2)
print("n1 - n2 =", n1 - n2)
print("n1 * n2 =", n1 * n2)
print("n1 / n2 =", n1 / n2)
