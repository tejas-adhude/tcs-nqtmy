from fractions import Fraction

# """Creating fractions from numerator and denominator."""
f1 = Fraction(3, 4)  # Represents 3/4

# """Creating fractions from a float."""
f2 = Fraction(0.5)  # Represents 1/2

# """Creating fractions from a string."""
f3 = Fraction('1/3')  # Represents 1/3

# """Creating a fraction from another Fraction."""
f4 = Fraction(f1)  # Creates a new Fraction from an existing one

# """Basic arithmetic operations with fractions."""
result_add = f1 + f2  # 3/4 + 1/2 = 5/4
result_sub = f1 - f2  # 3/4 - 1/2 = 1/4
result_mul = f1 * f2  # 3/4 * 1/2 = 3/8
result_div = f1 / f2  # 3/4 ÷ 1/2 = 3/2

# """Accessing numerator and denominator of a fraction."""
numerator = f1.numerator  # 3
denominator = f1.denominator  # 4

# """Comparing fractions using comparison operators."""
f5 = Fraction(2, 3)
comparison_gt = f1 > f5  # True
comparison_lt = f1 < f5  # False

# """Converting a fraction to a floating-point number."""
float_value = float(f1)  # Converts 3/4 to 0.75

# """Automatic simplification of fractions."""
f6 = Fraction(8, 4)  # This will be simplified to 2
