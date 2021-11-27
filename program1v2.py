# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

# function for asking 4 numbers
def get_numbers():
    first_num = float(input("First number: "))
    second_num = float(input("Second number: "))
    third_num = float(input("Third number: "))
    fourth_num = float(input("Fourth number: "))
    return first_num, second_num, third_num, fourth_num


# Ask for 4 numbers
first_num, second_num, third_num, fourth_num = get_numbers()

# If the first number is the highest number
if third_num < first_num > second_num and first_num > fourth_num and third_num < second_num > fourth_num and third_num > fourth_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {first_num}, {second_num}, {third_num}, {fourth_num}")
elif third_num < first_num > second_num and first_num > fourth_num and third_num < second_num > fourth_num and fourth_num > third_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {first_num}, {second_num}, {fourth_num}, {third_num}")
elif third_num < first_num > second_num and first_num > fourth_num and second_num < third_num > fourth_num and second_num > fourth_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {first_num}, {third_num}, {second_num}, {fourth_num}")
elif third_num < first_num > second_num and first_num > fourth_num and second_num < third_num > fourth_num and fourth_num > second_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {first_num}, {third_num}, {fourth_num}, {second_num}")
elif third_num < first_num > second_num and first_num > fourth_num and second_num < fourth_num > third_num and second_num > third_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {first_num}, {fourth_num}, {second_num}, {third_num}")
elif third_num < first_num > second_num and first_num > fourth_num and second_num < fourth_num > third_num and third_num > second_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {first_num}, {fourth_num}, {third_num}, {second_num}")

# If the second number is the highest number
if third_num < second_num > first_num and second_num > fourth_num and third_num < first_num > fourth_num and third_num > fourth_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {second_num}, {first_num}, {third_num}, {fourth_num}")
elif third_num < second_num > first_num and second_num > fourth_num and third_num < first_num > fourth_num and fourth_num > third_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {second_num}, {first_num}, {fourth_num}, {third_num}")
elif third_num < second_num > first_num and second_num > fourth_num and first_num < third_num > fourth_num and first_num > fourth_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {second_num}, {third_num}, {first_num}, {fourth_num}")
elif third_num < second_num > first_num and second_num > fourth_num and first_num < third_num > fourth_num and fourth_num > first_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {second_num}, {third_num}, {fourth_num}, {first_num}")
elif third_num < second_num > first_num and second_num > fourth_num and first_num < fourth_num > third_num and first_num > third_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {second_num}, {fourth_num}, {first_num}, {third_num}")
elif third_num < second_num > first_num and second_num > fourth_num and first_num < fourth_num > third_num and third_num > first_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {second_num}, {fourth_num}, {third_num}, {first_num}")

# If the third number is the highest number
if first_num < third_num > second_num and third_num > fourth_num and second_num < first_num > fourth_num and second_num > fourth_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {third_num}, {first_num}, {second_num}, {fourth_num}")
elif first_num < third_num > second_num and third_num > fourth_num and second_num < first_num > fourth_num and fourth_num > second_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {third_num}, {first_num}, {fourth_num}, {second_num}")
elif first_num < third_num > second_num and third_num > fourth_num and first_num < second_num > fourth_num and first_num > fourth_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {third_num}, {second_num}, {first_num}, {fourth_num}")
elif first_num < third_num > second_num and third_num > fourth_num and first_num < second_num > fourth_num and fourth_num > first_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {third_num}, {second_num}, {fourth_num}, {first_num}")
elif first_num < third_num > second_num and third_num > fourth_num and second_num < fourth_num > first_num and first_num > second_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {third_num}, {fourth_num}, {first_num}, {second_num}")
elif first_num < third_num > second_num and third_num > fourth_num and second_num < fourth_num > first_num and second_num > first_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {third_num}, {fourth_num}, {second_num}, {first_num}")

# If d is the highest number
if third_num < fourth_num > second_num and fourth_num > first_num and third_num < second_num > first_num and third_num > first_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {fourth_num}, {second_num}, {third_num}, {first_num}")
elif third_num < fourth_num > second_num and fourth_num > first_num and third_num < second_num > first_num and first_num > third_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {fourth_num}, {second_num}, {first_num}, {third_num}")
elif third_num < fourth_num > second_num and fourth_num > first_num and second_num < third_num > first_num and second_num > first_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {fourth_num}, {third_num}, {second_num}, {first_num}")
elif third_num < fourth_num > second_num and fourth_num > first_num and second_num < third_num > first_num and first_num > second_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {fourth_num}, {third_num}, {first_num}, {second_num}")
elif third_num < fourth_num > second_num and fourth_num > first_num and second_num < first_num > third_num and second_num > third_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {fourth_num}, {first_num}, {second_num}, {third_num}")
elif third_num < fourth_num > second_num and fourth_num > first_num and second_num < first_num > third_num and third_num > second_num:
    print(f"The arrangement of the given numbers from highest to lowest is: {fourth_num}, {first_num}, {third_num}, {second_num}")