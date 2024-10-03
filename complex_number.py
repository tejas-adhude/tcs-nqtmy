# """Creating complex numbers using complex literals."""
z1 = 3 + 4j  # Represents the complex number 3 + 4i
z2 = 2 - 5j  # Represents the complex number 2 - 5i

# """Creating complex numbers using the complex() constructor."""
z3 = complex(2, 3)  # Represents the complex number 2 + 3i
z4 = complex(5)     # Represents the complex number 5 + 0i (real part only)

# """Basic arithmetic operations with complex numbers."""
sum_result = z1 + z2  # Addition: (3 + 4j) + (2 - 5j) = 5 - j
difference_result = z1 - z2  # Subtraction: (3 + 4j) - (2 - 5j) = 1 + 9j
product_result = z1 * z2  # Multiplication: (3 + 4j) * (2 - 5j) = 23 - 2j
quotient_result = z1 / z2  # Division: (3 + 4j) / (2 - 5j)

# """Accessing the real and imaginary parts of a complex number."""
real_part = z1.real  # 3.0
imaginary_part = z1.imag  # 4.0

# """Using the abs() function to calculate the magnitude (modulus) of a complex number."""
magnitude_z1 = abs(z1)  # |z1| = sqrt(3^2 + 4^2) = 5.0

# """Using the conjugate() method to find the conjugate of a complex number."""
conjugate_z1 = z1.conjugate()  # 3 - 4j

# """Comparing complex numbers."""
comparison_equal = z1 == z3  # True if z1 is equal to z3 (3 + 4j == 2 + 3j)
comparison_not_equal = z1 != z2  # True if z1 is not equal to z2

# """Working with complex number functions from the cmath module."""
import cmath

# Using cmath to calculate the phase (angle) of a complex number
phase_z1 = cmath.phase(z1)  # Angle of the complex number
# Using cmath to calculate the exponential of a complex number
exp_z1 = cmath.exp(z1)  # Exponential function for complex numbers
