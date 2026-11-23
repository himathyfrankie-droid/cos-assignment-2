import statistics

# Create a list of numbers
numbers = [2, 4, 4, 6, 8, 8, 8, 10]

# Function 1: Calculate the sum of the numbers
def sum_numbers(numbers):
    return sum(numbers)


# Function 2: Calculate the average of the numbers
def average_numbers(numbers):
    return sum(numbers) / len(numbers)


# Function 3: Calculate the median and mode
def median_and_mode(numbers):
    median = statistics.median(numbers)
    mode = statistics.multimode(numbers)
    return median, mode


# Display the results
print("List of numbers:", numbers)
print("Sum:", sum_numbers(numbers))
print("Average:", average_numbers(numbers))

median, mode = median_and_mode(numbers)

print("Median:", median)
print("Mode:", mode)
