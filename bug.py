def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list) #This will return 0
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [0,0,0]
average_zero = calculate_average(my_list_with_zero) #This will return 0
print(f"The average of a list with zeros is: {average_zero}")