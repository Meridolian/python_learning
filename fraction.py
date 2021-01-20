import fractions as fr


class Fraction: 

    def __init__(self, numerator, denominator):
        self.fraction = fr.Fraction(numerator, denominator)

    """
    Overload __add__ python method to sum fractions
    """
    def __add__(self, add):
        fr_sum = self.fraction + add.fraction
        return Fraction(fr_sum.numerator, fr_sum.denominator)

    """
    Overload __sub__ python method to substract fractions
    """
    def __sub__(self, sub):
        fr_sub = self.fraction - sub.fraction
        return Fraction(fr_sub.numerator, fr_sub.denominator)

    """ 
    Overload __mul__ python method to multiply fractions
    """
    def __mul__(self, mul):
        fr_mul = self.fraction * mul.fraction
        return Fraction(fr_mul.numerator, fr_mul.denominator)

    """
    Overload __truediv__ python method to divide fractions
    """
    def __truediv__(self, div):
        fr_div = self.fraction / div.fraction
        return Fraction(fr_div.numerator, fr_div.denominator)

    def show(self):
        return f"{self.fraction.numerator} / {self.fraction.denominator}"