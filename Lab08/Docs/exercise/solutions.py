# Cmpe 150 Lab 8 Questions

# Question 1 - Large
# Write a program that reads an integer N from the user, then
# reads N more integers from the user and store them in a list.
# Then prints elements larger than the average of numbers held in the array.

# Example Test Case 1:
# 10 1 2 3 4 5 6 7 8 9 10 -> 6 7 8 9 10

# Example Test Case 2:
# 4 4 1 3 8 -> 8

N = int(input())
List = []
for i in range(N):
    num = int(input())
    List.append(num)
avg = sum(List) / len(List)
for i in range(len(List)):
    if List[i] > avg:
        print(List[i], end=' ')

# Question 2 - Let's Count
# Write a function that takes a list and find frequency of each element in the list
# then prints. Assume the numbers in the list will be between 0 and 100 (inclusive).

# Example Test Case:
# 5 10 2 5 50 5 10 1 2 2 ->
# 1 --> 1 2 --> 3 5 --> 3 10 --> 2 50 --> 1

def find_freq(List):
    freqs = [0] * 101 # 0 and 100 (inclusive)
    for i in range(len(List)):
        freqs[List[i]] += 1
    for i in range(len(freqs)):
        if freqs[i] != 0:
            print(i, '-->', freqs[i], end='\t\t')

find_freq([5, 10, 2, 5, 50, 5, 10, 1, 2, 2])

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

List = []
for i in range(5):
    num = int(input())
    List.append(num)
transformerd_list = [x ** 5 for x in List]
print(transformerd_list)
# Or with a single line
print([x ** 5 for x in List])

# Question 4 - To the left
# Write a function which takes a list of numbers and an integer k and shifts the numbers
# to the left circularly by k and return the shifted list.

# Example Test Case 1:
# [1, 2, 3, 4, 5] 2	-> [3, 4, 5, 1, 2]

# Example Test Case 2:
# [2, 18, 6, 0] 3 -> [0, 2, 18, 6]

def shift_to_left_by_k(List, k):
    shift_amount = k % len(List)
    return List[shift_amount:] + List[:shift_amount]

print(shift_to_left_by_k([1, 2, 3, 4, 5], 2))
print(shift_to_left_by_k([2, 18, 6, 0], 3))
print(shift_to_left_by_k([2, 18, 6, 0], 0))

# Question 5 - Reverse
# Write a function which takes a list as a parameter
# a. Then print elements to the screen in reverse order.
# b. Then reverse the order of these integers in the array and print the array.

# Example Test Case 1:
# 3 1 -4 5 2 -> 2 5 -4 1 3

# Example Test Case 2:
# 15 7 2 89 8 12 -> 12 8 89 2 7 15

def reverse(List):
    reversed_list = []
    for el in reversed(List):
        print(el, end=' ')
        reversed_list.append(el)
    print()
    return reversed_list

reversed_list = reverse([3, 1, -4, 5, 2])
print(reversed_list)
reversed_list = reverse([15, 7, 2, 89, 8, 12])
print(reversed_list)

# Question 6 - Remove X
# Write a function that accepts a list and variable X and removes all occurrence of
# X from the list.

# Example Test Case:
# [5, 20, 15, 20, 25, 50, 20], 20 -> [5, 15, 25, 50]

def remove_x(List, x):
    list_without_x = []
    for i in range(len(List)):
        if List[i] != x:
            list_without_x.append(List[i])
    return list_without_x

print(remove_x([5, 20, 15, 20, 25, 50, 20], 20))
print(remove_x([343] * 10, 343))

# Question 7 - Remove Duplicates
# Write a function that takes a list of integers then returns without all duplicates.

# Example Test Case 1:
# [1, 1, 1, 1, 1, 2, 2, 2, 3, 2, 2, 4, 5] -> [1, 2, 3, 4, 5]

# Example Test Case 2:
# [0,0,0,0,0,0,0] -> [0]

def remove_duplicates(List):
    seen_unique_elements = []
    for i in range(len(List)):
        if not List[i] in seen_unique_elements:
            seen_unique_elements.append(List[i])
    return seen_unique_elements

print(remove_duplicates([1, 1, 1, 1, 1, 2, 2, 2, 3, 2, 2, 4, 5]))
print(remove_duplicates([0,0,0,0,0,0,0]))

# Question 8 - Odd Occurrences
# Write a function that takes a list and prints the elements that occur 2n+1 times.
# If there is no element with odd number of occurrences then it should not print anything.

# Example Test Case 1:
# [1, 1, 2, 3, 4, 2, 'apple', 'banana', 'banana'] -> 3 4 apple

# Example Test Case 2:
# [2, 2, 3, 3, 2] -> 2

# Example Test Case 3:
# [ 'a' , 'b' , 'c' , 'c' , 'b' , 'a' ] ->

def odd_occurences(List):
    odd_elements = []
    for i in range(len(List)):
        if List[i] in odd_elements:
            odd_elements.remove(List[i])
        else:
            odd_elements.append(List[i])
    for i in range(len(odd_elements)):
        print(odd_elements[i], end=' ')
    print()
    return odd_elements

print(odd_occurences([1, 1, 2, 3, 4, 2, 'apple', 'banana', 'banana']))
print(odd_occurences([2, 2, 3, 3, 2]))
print(odd_occurences(['a' , 'b' , 'c' , 'c' , 'b' , 'a']))

# Question 9 - Fractions
# Fractions can be expressed as as tuple: (numerator, denominator).
# Write a function that adds two fractions that are passed as tuples.

# Example Test Case 1:
# (1, 3) (4, 5) -> (17, 15)

# Example Test Case 2:
# (3, 5) (1, 2) -> (11, 10)

def fractions(frac1, frac2):
    return (((frac1[0] * frac2[1]) + (frac1[1] * frac2[0])), (frac1[1] * frac2[1]))

print(fractions((1, 3), (4, 5)))
print(fractions((3, 5), (1, 2)))

# Question 10 - Points
# Points can be expressed as a tuple: (x, y).

# Question 10a - Distance
# Write a function distance which takes two tuples (points) and returns Euclidian distance between
# these points.

# Example Test Case 1:
# (3, 0) (0, 4) -> 5.0

# Example Test Case 2:
# (5, 8) (10, 20) -> 13.0

def dist(p1, p2):
    distance_in_x_axis = p1[0]-p2[0]
    distance_in_x_axis_squared = distance_in_x_axis ** 2

    distance_in_y_axis = p1[1] - p2[1]
    distance_in_y_axis_squared = distance_in_y_axis ** 2

    squared_distance = distance_in_x_axis_squared + distance_in_y_axis_squared
    distance = squared_distance ** 0.5
    return distance

    # An alternative way to do the same thing
    # return (((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))**0.5

print(dist((3, 0), (0, 4)))
print(dist((5, 8), (10, 20)))
print(dist((3, 6), (3, 6)))

# Question 10b - Closest
# Write a function which takes two tuples (points) and returns the point closest to the origin.
# Use the distance function.

# Example Test Case 1:
# (3, 0) (0, 4) -> (3, 0)

# Example Test Case 2:
# (11, 7) (6, 8) -> (6, 8)

def closest(p1, p2):
    dist1 = dist(p1, (0, 0))
    dist2 = dist(p2, (0, 0))
    if dist1 < dist2:
        return p1
    else:
        return p2

print(closest((3, 0), (0, 4)))
print(closest((11, 7), (6, 8)))

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

N = int(input())
points = []
farthest_index1, farthest_index2, max_dist = -1, -2, -6
for i in range(N):
    line = input()
    elements = line.split()
    point = (int(elements[0]), int(elements[1]))
    points.append(point)
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = dist(points[i], points[j])
        if distance > max_dist:
            max_dist = distance
            farthest_index1 = i
            farthest_index2 = j

print('Distance:', max_dist)
print('Point 1:', points[farthest_index1])
print('Point 2:', points[farthest_index2])


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

def bubble_sort(List):
    for i in range(len(List)-1):
        for j in range(len(List)-1-i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

print(bubble_sort([4, 2, 8, 6, 7, 3, 1, 5]))
print(sorted([4, 2, 8, 6, 7, 3, 1, 5]))

print(bubble_sort([4, -2, 4, 6, -7, 3, 1, 5]))
print(sorted([4, -2, 4, 6, -7, 3, 1, 5]))


