# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# function for asking 4 numbers
def get_numbers():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("Third number: "))
    d = int(input("Fourth number: "))
    return a, b, c, d


# Ask for 4 numbers
a, b, c, d = get_numbers()

# If a is the highest number
if c < a > b and a > d and c < b > d and c > d:
    print(f"The arrangement of the given numbers from highest to lowest is: {a}, {b}, {c}, {d}")
elif c < a > b and a > d and c < b > d and d > c:
    print(f"The arrangement of the given numbers from highest to lowest is: {a}, {b}, {d}, {c}")
elif c < a > b and a > d and b < c > d and b > d:
    print(f"The arrangement of the given numbers from highest to lowest is: {a}, {c}, {b}, {d}")
elif c < a > b and a > d and b < c > d and d > b:
    print(f"The arrangement of the given numbers from highest to lowest is: {a}, {c}, {d}, {b}")
elif c < a > b and a > d and b < d > c and b > c:
    print(f"The arrangement of the given numbers from highest to lowest is: {a}, {d}, {b}, {c}")
elif c < a > b and a > d and b < d > c and c > b:
    print(f"The arrangement of the given numbers from highest to lowest is: {a}, {d}, {c}, {b}")

# If b is the highest number
if c < b > a and b > d and c < a > d and c > d:
    print(f"The arrangement of the given numbers from highest to lowest is: {b}, {a}, {c}, {d}")
elif c < b > a and b > d and c < a > d and d > c:
    print(f"The arrangement of the given numbers from highest to lowest is: {b}, {a}, {d}, {c}")
elif c < b > a and b > d and a < c > d and a > d:
    print(f"The arrangement of the given numbers from highest to lowest is: {b}, {c}, {a}, {d}")
elif c < b > a and b > d and a < c > d and d > a:
    print(f"The arrangement of the given numbers from highest to lowest is: {b}, {c}, {d}, {a}")
elif c < b > a and b > d and a < d > c and a > c:
    print(f"The arrangement of the given numbers from highest to lowest is: {b}, {d}, {a}, {c}")
elif c < b > a and b > d and a < d > c and c > a:
    print(f"The arrangement of the given numbers from highest to lowest is: {b}, {d}, {c}, {a}")

# If c is the highest number
if a < c > b and c > d and b < a > d and b > d:
    print(f"The arrangement of the given numbers from highest to lowest is: {c}, {a}, {b}, {d}")
elif a < c > b and c > d and b < a > d and d > b:
    print(f"The arrangement of the given numbers from highest to lowest is: {c}, {a}, {d}, {b}")
elif a < c > b and c > d and a < b > d and a > d:
    print(f"The arrangement of the given numbers from highest to lowest is: {c}, {b}, {a}, {d}")
elif a < c > b and c > d and a < b > d and d > a:
    print(f"The arrangement of the given numbers from highest to lowest is: {c}, {b}, {d}, {a}")
elif a < c > b and c > d and b < d > a and a > b:
    print(f"The arrangement of the given numbers from highest to lowest is: {c}, {d}, {a}, {b}")
elif a < c > b and c > d and b < d > a and b > a:
    print(f"The arrangement of the given numbers from highest to lowest is: {c}, {d}, {b}, {a}")

# If d is the highest number
if c < d > b and d > a and c < b > a and c > a:
    print(f"The arrangement of the given numbers from highest to lowest is: {d}, {b}, {c}, {a}")
elif c < d > b and d > a and c < b > a and a > c:
    print(f"The arrangement of the given numbers from highest to lowest is: {d}, {b}, {a}, {c}")
elif c < d > b and d > a and b < c > a and b > a:
    print(f"The arrangement of the given numbers from highest to lowest is: {d}, {c}, {b}, {a}")
elif c < d > b and d > a and b < c > a and a > b:
    print(f"The arrangement of the given numbers from highest to lowest is: {d}, {c}, {a}, {b}")
elif c < d > b and d > a and b < a > c and b > c:
    print(f"The arrangement of the given numbers from highest to lowest is: {d}, {a}, {b}, {c}")
elif c < a > b and d > a and b < a > c and c > b:
    print(f"The arrangement of the given numbers from highest to lowest is: {d}, {a}, {c}, {b}")