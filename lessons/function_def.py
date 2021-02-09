"""An Example function definition."""


def my_max(a: int, b: int) -> int: #signature line/"contract"#
    """Returns the largest argument.""" #docstring/how you should use it#
    if a >= b: #body block#
        return a
    else: 
        return b

print(my_max(10 + 1, 10))
print(my_max(-50, 100))
result: int = my_max(-50, 100)
print(result)

###################################

x: int = 6
y: int = 5 + 2
z: int + my_max(y, x)
print(z)