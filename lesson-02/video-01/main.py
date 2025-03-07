# Single, Specific, Short, and Surround

# Python method using list to filter and return even numbers
def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Python method using a lambda function to filter and return even numbers
def even_numbers_lambda(numbers):
    return list(filter(lambda num: num % 2 == 0, numbers))

# Python method with a for loop to filter and return even numbers
def even_numbers_loop(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Python method to filter even numbers from a list, handle non-integer values, and raise errors
def even_numbers_safe(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers")
    return [num for num in numbers if num % 2 == 0]

# Assert statements
assert even_numbers([1, 2, 3, 4, 5]) == [2, 4]
assert even_numbers_lambda([1, 2, 3, 4, 5]) == [2, 4]
assert even_numbers_loop([1, 2, 3, 4, 5]) == [2, 4]
assert even_numbers_safe([1, 2, 3, 4, 5]) == [2, 4]

# Test with non-integer values to ensure error handling works
try:
    even_numbers_safe([1, 2, '3', 4, 5])
except ValueError as e:
    assert str(e) == "All elements in the list must be integers"

