numbers = [3, 1, 4, 1, 5, 9, 2]

# Predict the values without running the code

# numbers[0]
# Prediction: 3

# numbers[-1]
# Prediction: 2

# numbers[3]
# Prediction: 1

# numbers[:-1]
# Prediction: [3, 1, 4, 1, 5, 9]

# numbers[3:4]
# Prediction: [1]

# 5 in numbers
# Prediction: True

# 7 in numbers
# Prediction: False

# "3" in numbers
# Prediction: False

# numbers + [6, 5, 3]
# Prediction: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1]=1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)