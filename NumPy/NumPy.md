# NumPy in Python

NumPy is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and many mathematical functions to perform operations on these arrays efficiently.

## Key Features of NumPy

1. **N-dimensional Array Object**: The core of NumPy is its `ndarray` or N-dimensional array object, which supports fast element-wise operations and complex mathematical functions.
2. **Broadcasting**: Enables operations on arrays of different shapes, allowing for efficient computations without making copies of data.
3. **Linear Algebra Support**: NumPy includes functions for working with linear algebra, Fourier transforms, random numbers, etc.

## Commonly Used Constants

- `numpy.pi`: Represents the value of π (approximately 3.14159).
- `numpy.e`: Represents Euler’s number (approximately 2.71828).
- `numpy.inf`: Positive infinity.
- `numpy.nan`: "Not a Number", used to represent undefined results.

## Array Creation Functions

1. **Basic Array Creation**
   - `numpy.array(object)`: Create an array from a list or tuple.
   - `numpy.zeros(shape)`: Create an array filled with zeros.
   - `numpy.ones(shape)`: Create an array filled with ones.
   - `numpy.arange([start,] stop, [step,])`: Create an array with values in a given range.
   - `numpy.linspace(start, stop, num)`: Generate `num` evenly spaced samples between `start` and `stop`.

2. **Random Number Generation**
   - `numpy.random.rand(d0, d1, ..., dn)`: Generate random numbers in a given shape.
   - `numpy.random.randint(low, high, size)`: Generate random integers from `low` to `high` with given `size`.

## Array Operations

1. **Mathematical Operations**
   - `numpy.add(x, y)`: Add arrays element-wise.
   - `numpy.subtract(x, y)`: Subtract arrays element-wise.
   - `numpy.multiply(x, y)`: Multiply arrays element-wise.
   - `numpy.divide(x, y)`: Divide arrays element-wise.
   - `numpy.dot(a, b)`: Dot product of two arrays.

2. **Trigonometric Functions**
   - `numpy.sin(x)`: Compute the sine of elements in an array.
   - `numpy.cos(x)`: Compute the cosine of elements in an array.
   - `numpy.tan(x)`: Compute the tangent of elements in an array.

3. **Exponential and Logarithmic Functions**
   - `numpy.exp(x)`: Calculate the exponential of each element in the array.
   - `numpy.log(x)`: Natural logarithm, element-wise.
   - `numpy.log10(x)`: Base-10 logarithm, element-wise.

4. **Aggregate Functions**
   - `numpy.sum(a)`: Compute the sum of array elements.
   - `numpy.mean(a)`: Compute the arithmetic mean of array elements.
   - `numpy.max(a)`: Return the maximum value in an array.
   - `numpy.min(a)`: Return the minimum value in an array.
   - `numpy.std(a)`: Compute the standard deviation of array elements.

## Linear Algebra Functions

- `numpy.linalg.inv(a)`: Compute the inverse of a matrix.
- `numpy.linalg.det(a)`: Compute the determinant of a matrix.
- `numpy.linalg.eig(a)`: Compute the eigenvalues and right eigenvectors of a square matrix.

## Example Usage

Here are some examples demonstrating how to use NumPy:

```python
import numpy as np

# Creating Arrays
a = np.array([1, 2, 3])
print(a)  # Output: [1 2 3]

b = np.zeros((2, 2))
print(b)
# Output:
# [[0. 0.]
#  [0. 0.]]

# Mathematical Operations
c = np.add(a, 5)
print(c)  # Output: [6 7 8]

# Trigonometric Functions
theta = np.pi / 2
print(np.sin(theta))  # Output: 1.0

# Exponential and Logarithmic Functions
print(np.exp(1))  # Output: e (approximately 2.71828)

# Linear Algebra
matrix = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(matrix)
print(inverse)
# Output:
# [[-2.   1. ]
#  [ 1.5 -0.5]]
