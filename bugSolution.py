def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    if all(x == 0 for x in numbers):
        raise ValueError("Cannot calculate the average of a list containing only zeros.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
try:
    average_empty = calculate_average(my_empty_list)
    print(f"The average of an empty list is: {average_empty}")
except ValueError as e:
    print(f"Error: {e}")

my_list_with_zero = [0,0,0]
try:
    average_zero = calculate_average(my_list_with_zero)
    print(f"The average of a list with zeros is: {average_zero}")
except ValueError as e:
    print(f"Error: {e}")
