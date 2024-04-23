# Cmpe 150 Lab 10 Questions

# Critical Note: Please solve the examples 1-5 below using recursion
# although they can be solved by using a for loop or a while loop.

# Question 1
# Write a recursive function to find the factorial of a given number.

# Example Test Case:
# 6 -> 720

# ToDo

# Question 2:
# Implement a recursive function (`get_fib`) that returns the n'th number
# in the Fibonacci sequence.
# Each number is the sum of the two preceding ones, starting from 0 and 1.

# Example Test Case:
# 5 -> 3

# ToDo

# Question 3:
# Write a recursive function reverse_string(s) that takes a string s as
# an input and returns its reverse.

# Example Test Case:
# "hhow" -> "wohh"

# ToDo

# From https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
# Question 4
# Write a Python function to calculate the sum of a list of numbers using recursion.

# Example Test Case:
# [4, 654, 2, 321] -> 981

# ToDo


# Question 5
# Write a Python function to determine the number of digits for a given positive integer using recursion.

# Example Test Case:
# 734732 -> 6

# ToDo


# Question 6
# Write a program that takes an integer n and then prints related hailstone sequence
# until 1. If number is even, divide it by 2. If number is odd, multiply it by 3 and add 1.

# Example Test Case 1:
# 20 -> 20 10 5 16 8 4 2 1

# Example Test Case 2:
# 12 -> 12 6 3 10 5 16 8 4 2 1

# ToDo

# Question 7
# Given a positive integer N, calculate the sum of the series that consist of N numbers and
# goes like: N, NN, NNN... For example if N is 2, we calculate 2 + 22; if N is 5
# we calculate 5 + 55 + 555 + 5555 + 55555

# Example Test Case 1:
# 2 -> 24

# Example Test Case 2:
# 6 -> 740736

# Example Test Case 3:
# 3 -> 369

# ToDo

# Question 8
# Binary search is a searching algorithm that finds an element n in a sorted list L of size s.
# Firstly it compares n to L[s//2]. If n is bigger than L[s//2], it means that n is in upper
# half of the list. Likewise, if n is smaller than L[s//2], it means n is in lower half of the list.
# Then, the half of list which does not contain n is discarded. This process repeated until k th step
# where L[s//2**k] equals to n or list is empty.
# Write a function which implements binary search to find whether or nor a float exists in a
# list of floats.

# Example Test Case 1:
# L = [ 1 , 3 , 4 , 5 , 6] , num = 5 -> 5 exists in list

# Example Test Case 2:
# L = [ 21 , 13 , 4.4 , 85 , 60] , num = 16 -> 16 does not exist in list

# ToDo

# Question 9
# A number is said to be "Disarium" if the sum of its digits raised to their respective positions
# is the number itself. Write a program that determines whether a number is a Disarium or not.
# 75 -> False
# 7^1 + 5^2 = 7 + 25 = 32
# 135 -> True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

# Example Test Case 1:
# 544 -> False

# Example Test Case 2:
# 518 -> True

# Example Test Case 3:
# 466 -> False

# Example Test Case 4:
# 8 -> True

# ToDo

# Question 10
# In number theory, Euler's Totient function counts the positive integers up to a given integer
# n that are relatively prime to n. Write three functions, respectively gcd(a, b),
# relatively_prime(a, b) and euler_totient(a). To find euler_totient(a), count the number of integers
# between 1 and n that are relatively prime with n. A number a is relatively prime with b iff gcd(a, b) = 1.
# To implement gcd(a, b), follow the steps below. Given an integer n, print out the euler_totient(n).
# To find the greates common divisor between a and b:
# Repeatedly replace (a,b) with (b,a % b) until the second integer in the pair is zero.
# Return the first integer in the pair as the gcd.

# Example Test Case 1:
# 10 -> 4

# Example Test Case 2:
# 342 -> 108

# Example Test Case 3:
# 76 -> 36

# ToDo

# Question 11
# Consider that you need to fill containers to a bulk carrier.
# You want to choose containers such that total profit of ships cargo is maximized.
# However, there is a mass limit the of the cargo.
# Write a function that inputs the ships mass capacity and 2 arrays: weight and profit.
# weight[i] indicates the mass of container[i] and profit[i] is the profit earned from
# container[i]. Note: Each container[i] indicates a unique container.
# Note: Assume that the limit is less than or equal to the sum of the total weights

# Example Test Case:
# weight = [10, 20, 30], profit = [4 , 5 , 60] , limit = 30 -> Max Profit = 60

# ToDo

