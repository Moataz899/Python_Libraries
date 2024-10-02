# Math in Python

Python’s `math` module provides access to a wide range of mathematical functions and constants. Below is an overview of key concepts and commonly used functions.

## Constants

- `pi (π)`: Approximately 3.14159.
- `e`: Approximately 2.71828 (Euler’s number).
- `inf`: Represents positive infinity.
- `nan`: Stands for "Not a Number," used to indicate an invalid or undefined result.

## Functions

### 1. Trigonometric Functions
- `sin(x)`: Returns the sine of `x` (in radians).
- `cos(x)`: Returns the cosine of `x` (in radians).
- `tan(x)`: Returns the tangent of `x` (in radians).

### 2. Hyperbolic Functions
- `sinh(x)`: Returns the hyperbolic sine of `x`.
- `cosh(x)`: Returns the hyperbolic cosine of `x`.
- `tanh(x)`: Returns the hyperbolic tangent of `x`.

### 3. Exponential and Logarithmic Functions
- `exp(x)`: Returns the exponential of `x` (e^x).
- `log(x)`: Returns the natural logarithm of `x`.
- `log10(x)`: Returns the base-10 logarithm of `x`.

### 4. Power and Root Functions
- `pow(x, y)`: Returns `x` raised to the power `y`.
- `sqrt(x)`: Returns the square root of `x`.
- `cbrt(x)`: Returns the cube root of `x` (not part of the standard math module but can be implemented as `x ** (1/3)`).

### 5. Rounding and Ceiling Functions
- `ceil(x)`: Rounds `x` up to the nearest integer.
- `floor(x)`: Rounds `x` down to the nearest integer.
- `trunc(x)`: Truncates `x` to an integer (removes the fractional part).

### 6. Miscellaneous Functions
- `fsum(iterable)`: Computes the sum of an iterable of floating-point numbers with precision.
- `gcd(a, b)`: Returns the greatest common divisor of `a` and `b`.
- `hypot(x, y)`: Returns the Euclidean norm (magnitude) of the vector `(x, y)`.

## Example Usage

Here are some examples demonstrating how to use the `math` module:

```python
import math

# Constants
print(math.pi)  # Output: approximately 3.14159
print(math.e)   # Output: approximately 2.71828

# Trigonometric Functions
print(math.sin(math.pi / 2))  # Output: 1.0 (sine of 90 degrees)

# Exponential and Logarithmic Functions
print(math.exp(1))  # Output: e (approximately 2.71828)

# Rounding Functions
print(math.ceil(3.7))  # Output: 4 (round up)
print(math.floor(3.2))  # Output: 3 (round down)
