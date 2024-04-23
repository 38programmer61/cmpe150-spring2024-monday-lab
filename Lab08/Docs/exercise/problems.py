# Cmpe 150 Lab 8 Questions

# Question 1 - Large
# Write a program that reads an integer N from the user, then
# reads N more integers from the user and store them in a list.
# Then prints elements larger than the average of numbers held in the array.

# Example Test Case 1:
# 10 1 2 3 4 5 6 7 8 9 10 -> 6 7 8 9 10

# Example Test Case 2:
# 4 4 1 3 8 -> 8

# ToDo

# Question 2 - Let's Count
# Write a function that takes a list and find frequency of each element in the list
# then prints. Assume the numbers in the list will be between 0 and 100 (inclusive).

# Example Test Case:
# 5 10 2 5 50 5 10 1 2 2 ->
# 1 --> 1 2 --> 3 5 --> 3 10 --> 2 50 --> 1

# ToDo

# Question 3 - Fifth Powers
# List comprehensions might enable you to turn loop-based codes into one line elegant
# expressions.  Write a program that takes 5 integers as input and prints a new list
# consisting of the fifth power of each number. Try to construct and print the new
# list in just one line.

# Example Test Case 1:
# [1, 2, 3, 5, 0] -> [1, 32, 243, 3125, 0]

# Example Test Case 2:
# [4, 1, 6, -2, -3] -> [1024, 1, 7776, -32, -243]

# Example Test Case 3:
# [-3, -6, 2, 9, 0] -> [-243, -7776, 32, 59049, 0]

# ToDo

# Question 4 - To the left
# Write a function which takes a list of numbers and an integer k and shifts the numbers
# to the left circularly by k and return the shifted list.

# Example Test Case 1:
# [1, 2, 3, 4, 5] 2	-> [3, 4, 5, 1, 2]

# Example Test Case 2:
# [2, 18, 6, 0] 3 -> [0, 2, 18, 6]

# ToDo

# Question 5 - Reverse
# Write a function which takes a list as a parameter
# a. Then print elements to the screen in reverse order.
# b. Then reverse the order of these integers in the array and print the array.

# Example Test Case 1:
# 3 1 -4 5 2 -> 2 5 -4 1 3

# Example Test Case 2:
# 15 7 2 89 8 12 -> 12 8 89 2 7 15

# ToDo

# Question 6 - Remove X
# Write a function that accepts a list and variable X and removes all occurrence of
# X from the list.

# Example Test Case:
# [5, 20, 15, 20, 25, 50, 20], 20 -> [5, 15, 25, 50]

# ToDo

# Question 7 - Remove Duplicates
# Write a function that takes a list of integers then returns without all duplicates.

# Example Test Case 1:
# [1, 1, 1, 1, 1, 2, 2, 2, 3, 2, 2, 4, 5] -> [1, 2, 3, 4, 5]

# Example Test Case 2:
# [0,0,0,0,0,0,0] -> [0]

# ToDo

# Question 8 - Odd Occurrences
# Write a function that takes a list and prints the elements that occur 2n+1 times.
# If there is no element with odd number of occurrences then it should not print anything.

# Example Test Case 1:
# [1, 1, 2, 3, 4, 2, 'apple', 'banana', 'banana'] -> 3 4 apple

# Example Test Case 2:
# [2, 2, 3, 3, 2] -> 2

# Example Test Case 3:
# [ 'a' , 'b' , 'c' , 'c' , 'b' , 'a' ] ->

# ToDo

# Question 9 - Fractions
# Fractions can be expressed as as tuple: (numerator, denominator).
# Write a function that adds two fractions that are passed as tuples.

# Example Test Case 1:
# (1, 3) (4, 5) -> (17, 15)

# Example Test Case 2:
# (3, 5) (1, 2) -> (11, 10)

# ToDo

# Question 10 - Points
# Points can be expressed as a tuple: (x, y).

# Question 10a - Distance
# Write a function distance which takes two tuples (points) and returns Euclidian distance between
# these points.

# Example Test Case 1:
# (3, 0) (0, 4) -> 5.0

# Example Test Case 2:
# (5, 8) (10, 20) -> 13.0

# ToDo

# Question 10b - Closest
# Write a function which takes two tuples (points) and returns the point closest to the origin.
# Use the distance function.

# Example Test Case 1:
# (3, 0) (0, 4) -> (3, 0)

# Example Test Case 2:
# (11, 7) (6, 8) -> (6, 8)

# ToDo

# Question 10c - Farthest
# Write a program which takes an integer N and reads N points (given by their x and y coordinates)
# and determines the pair that is the farthest apart.

# Example Test Case 1:
# 3
# 3 0
# 0 0
# 0 4
# ->
# (0, 4)
# (3, 0)

# Example Test Case 2:
# 5
# 10 5
# 4 8
# 0 8
# 4 5
# -1 2
# ->
# (-1, 2)
# (10, 5)

# ToDo

# Bonus Question
# Question 11 - Bubble Sort
# Write a function that sorts elements of the list in ascending order.

# INPUT	OUTPUT
# 4 2 8 6 7 3 1 5	1 2 3 4 5 6 7 8
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent
# elements if they are in wrong order.

# Example:

# First Pass:

# ( 5 1 4 8 2 ) –> ( 1 5 4 8 2 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
# ( 1 5 4 8 2 ) –> ( 1 4 5 8 2 ), Swap since 5 > 4
# ( 1 4 5 8 2 ) –> ( 1 4 5 8 2 ), since these elements are already in order (8 > 5), no swap.
# ( 1 4 5 8 2 ) –> ( 1 4 5 2 8 ), Swap since 8 > 2.
# The largest element is at the end.

# Second Pass:

# ( 1 4 5 2 8 ) –> ( 1 4 5 2 8 )
# ( 1 4 5 2 8 ) –> ( 1 4 5 2 8 )
# ( 1 4 5 2 8 ) –> ( 1 4 2 5 8 ), Swap since 5 > 2
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
# Third Pass:
#
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
# ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

# Now, the array is already sorted, but our algorithm does not know if it is completed.
# The algorithm needs one whole pass without any swap to know it is sorted.

# Fourth Pass:

# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )

# ToDo

