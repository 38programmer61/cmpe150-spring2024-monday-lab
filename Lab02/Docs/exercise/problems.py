# Cmpe 150 Lab 2 Questions

# Q1: Take two integers from the user, and print them

# ToDo

# Q2: Take two integers from the user (a, b), and then print their sum, difference, product, power and remainder.
# Example test case: 13 5 -> 18 8 65 371293 3

# ToDo

# Q3: # Write a program that takes 3 integers from the user and then prints the sum, mean and multiple of the numbers.
# Example test case: 13 27 14	-> 54 18.00 4914

# ToDo

# Q4: There is a cash machine with an infinite supply of 5tl banknotes and 1tl coins inside it.
# Write a function that takes an integer representing the amount of money requested by a customer.
# The function then prints the number of banknotes and coins given to the customer.
# (Machine must prefer giving away banknotes instead of coins if possible)

# Example test case 1:
# 57 ->
# 5tl banknotes: 11
# 1tl coins: 2

# Example test case 2:
# 269 ->
# 5tl banknotes: 53
# 1tl coins: 4

# ToDo

# Q5: Write a function that takes a radius and returns the volume of the sphere.
# 4 over 3 multiplied by pi (3.14) and radius cubed
# Example test case 1: 3 -> 113.0399
# Example test case 2: 6 -> 904.3199

# ToDo

# Q6: Write a function called power that takes two integer parameter as number and n.
# The function should return the nth power of number.
# Example test case 1: 5 2 -> 25
# Example test case 2: 3 2 -> 9
# Example test case 3: 4 3 -> 64

# ToDo


# Q7: Write a program that asks the user their height in centimeters (integer) and their weight in kilograms (float).
# Calculate the user's body mass index (BMI) with the formula given below.
# BMI = weight(kg) / height(m)^2
# Example test case 1: 72 180 -> 	22.22
# Example test case 2: 79.5 172 -> 	26.87
# Example test case 3: 53.4 160 -> 	20.86
# Example test case 4: 81.2 165 -> 	29.83

# ToDo

# Q8: When you multiply an integer by itself, the result is a square number.
# Write a function that takes an integer and determines whether it is a square number or not.
# Do NOT use if or for since we haven't covered them yet.
# Example test case 1: 25 -> 	True
# Example test case 2: 23 -> 	False
# Example test case 3: 0  -> 	True
# Example test case 4: -1 -> 	False

# ToDo

# Q9: A chemical mixture has 2 components, namely Component X and Component Y.
# Ask the user for the amount of X and Y in the mixture and then calculate
# the percentages of X and Y in the total solution.

# Example test case 1: 10 10   -> 	50.00% 50.00%
# Example test case 2: 10.5 21 -> 	33.33% 66.67%
# Example test case 3: 0.1 0.9 -> 	10.00% 90.00%

# ToDo

# Q10: Emir wants to learn the wi-fi password. He asks the waiter, and the waiter says
# "The password is the x-1 times of the two least significant bases of 5^5628".
# Could you write a code that takes x as input and gives the wi-fi password as output?
# Example test case 1:  4 -> 75
# Example test case 2: 19 -> 450

# ToDo

# Q11: In mathematics and computer science, the floor function is the function that takes as input a real number x,
# and gives as output the greatest integer less than or equal to x, denoted as ⌊x⌋.
# The fractional part is the sawtooth function, denoted by {x} for real x and defined by the formula {x} = x - ⌊x⌋.
#
# Write a program that takes 3 positive floats from the input and prints out the fractional part of each value
# respectively. Do not use float-to-int type casting.
# Hint: Integer division by 1 can be helpful to find ⌊x⌋.

# Example test case 1:  4.8 6.4 3.5  -> 	0.8 0.4 0.5
# Example test case 2:  67.32 23.53 13.98  -> 	0.32 0.53 0.98
# Example test case 3:  65.12 49.32 30.09  -> 	0.12 0.32 0.09

# ToDo

# Q12: We want to simulate a division operation. In order to do that, write a function that takes two integers,
# dividend and divisor respectively, perform the division operation and print out the quotient and the remainder.
# Example test case 1:  9 2      ->   quotient = 4 remainder = 1
# Example test case 2:  156 13   ->   quotient = 12 remainder = 0
# Example test case 3:  84 16    ->   quotient = 5 remainder = 4

# ToDo

# Q13: You are in a biology lab observing reproducing bacteria. Every daughter cell grows up
# for a given time (t1) and becomes a parent cell, immediately dividing into two new daughter cells.
# These daughter cells then start the same process all over again.
# Given three integers, one representing the initial number of bacteria, one representing the time it takes
# daughter cells to become parent cells (t1), and one representing the total timewise length of the experiment.
# Write a function that returns the total number of bacteria at the end of the experiment.
# Example test case 1: 1 1 2 -> 	4
# Example test case 2: 5 3 8 -> 	20

# ToDo

# Q14: Write a function that takes four integers representing (x, y) coordinates of two points and calculates
# the distance between these two points. First two integers are x and y coordinates of a point on a 2D plane.
# Next 2 integers are coordinates of another point on the same plane.
# Call this function with the following inputs and print the results:
# Example test case 1: 5 10 10 22  ->  13.00
# Example test case 2: -5 -10 -10 -22 ->  13.00

# ToDo

# Q15: Two runners run around a circular track. The first runner runs x1 meters in a minute.
# The second runner runs x2 meters in a minute. Write a function that takes 4 parameters:
# radius r in meters, x1, x2 and total time elapsed in minutes. The function first calculates the circumference of
# the circular track. Then calculate the completed number of laps so far (integer) by each runner and return them.
# Take π = 3.14.
# Call this function with following inputs and print the number of laps in the format below:
# Example test case 1: 100 300 400 30  -> 	First runner = 14 laps - Second runner = 19 laps
# Example test case 2: 25 150 250 15  -> 	First runner = 14 laps - Second runner = 23 laps
# Example test case 3: 35 550 400 10  -> 	First runner = 25 laps - Second runner = 18 laps

# ToDo

# Q16: A telephone directory has 20 lines on each page, and each page has exactly 5 columns.
# Assume there is an entry in each column. Write a function that determines/returns on which page, column,
# and line the Xth entry is present. (Assume that page, line, column numbers, and X all start from 1.)
# Example test case 1: 156   -> 	2 12 1
# Example test case 1: 2348   -> 	24 10 3

# ToDo

# Q17: In football, there is a statistic for quarterbacks called the passer rating. It is calculated as follows:
# (a) C is the “completions per attempt” times 100 − 30 all divided by 20.
# (b) Y is the “yards per attempt” − 3 all divided by 4.
# (c) T is the “touchdowns per attempt” times 20.
# (d) I is 2.375 minus (“interceptions per attempts” times 35).
# (e) The passer rating is the sum of C, Y, T, and I all divided by 6 and then multiplied by 100.
# Write a function that takes five parameters: pass completions, pass attempts, total passing yards,
# touchdowns and interceptions and returns the passer rating.

# Example test case 1: 183 267 2064 17 3  -> 	106.08
# Example test case 1: 117 172 1587 12 3  -> 	110.30

# ToDo