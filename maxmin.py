def find_highest_and_lowest(numbers):
  # Check if the list is empty
  if not numbers:
    return None, None  # Return None for both highest and lowest if the list is empty
  
  # Initialize highest and lowest with the first element of the list
  highest = numbers[0]
  lowest = numbers[0]

  # Loop through each number in the list
  for number in numbers:
    # Check if the current number is greater than the highest found so far
    if number > highest:
      highest = number  # Update the highest number
    # Check if the current number is less than the lowest found so far
    if number < lowest:
      lowest = number  # Update the lowest number

  # Return the highest and lowest numbers found
  return highest, lowest

# Example usage:
numbers_list = [3, 5, 1, 2, 8, 4, 10, -3, 0]
highest, lowest = find_highest_and_lowest(numbers_list)
print(f"The highest number in the list is: {highest}")
print(f"The lowest number in the list is: {lowest}")