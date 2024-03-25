# Cmpe 150 Lab 4 Questions

# Question 1 - Multiple
# Write a program which calculates whether any given two numbers are multiples of one another.

# Example Test Case 1: 2 4 -> Multiple
# Example Test Case 2: 4 2 -> Multiple
# Example Test Case 3: 5 3 -> Not Multiple

# ToDo

# Question 2 - Simple Sort
# Question 2a
# Write a program that takes 2 integers from the user and then prints these integers
# in an ascending order using a single if statement.

# Example Test Case 1: 3 5 -> 3 5
# Example Test Case 2: 5 3 -> 3 5

# ToDo

# Question 2b
# Write a function that takes 3 integers from the user and then prints
# these integers in an ascending order

# Example Test Case 1: 1 3 2 -> 1 2 3
# Example Test Case 2: 3 2 1 -> 1 2 3
# Example Test Case 3: 2 3 1 -> 1 2 3

# ToDo

# Question 3 - Leap
# A leap year is a calendar year that contains an additional day added
# to keep the calendar year synchronized with the astronomical year.
# In the Gregorian calendar, each leap year has 366 days instead of 365,
# by extending February to 29 days rather than the common 28.
# These extra days occur in each year which is an integer multiple of 4,
# except for the years evenly divisible by 100, but not by 400.
# Given a year between 1 and 10000, you will write a function that find
# whether it is a leap year or not.

# Example Test Case 1: 1005	 -> not a leap year
# Example Test Case 2: 4 ->	leap year
# Example Test Case 3: 1000 -> not a leap year
# Example Test Case 4: 4000 -> leap year

# ToDo

# Question 4 - Parking Fee
# A parking lot "Park150" is charging its users as follows:
# <= 15 minutes ---> 15 liras
# After 15 minutes, users pay 10 liras per hour, as well as the first 15 liras.
# Given two integers hour and minute, write a program to calculate and print the total amount the user has to pay.
# For example: An input "1 28" means that the customer's car stayed in "Park150" for an hour and 28 minutes.
# So he has to pay 15 + 2*10 liras. You can assume that hour and minute will always be non-negative integers
# and minute will always be less than 60.

# Example Test Case 1: 0 45	-> 25
# Example Test Case 2: 1 34 -> 35
# Example Test Case 3: 2 0 -> 35
# Example Test Case 4: 4 59 -> 65

# ToDo

# Question 5 - GCD
# In mathematics, the greatest common divisor (GCD) of two or more integers is
# the largest positive integer that divides each of the integers.
# For two integers x, y, the greatest common divisor of x and y is denoted by gcd(x,y).
# For example, gcd(8,12)=4. Without using recursion, write a function that finds GCD of two given integers.

# Example Test Case 1: 14 21 -> 7
# Example Test Case 2: 1 300 ->	1
# Example Test Case 3: 256 16 -> 16
# Example Test Case 4: 109 109 -> 109

# ToDo

# Question 6 - Prime
# Given two integers A and B, find and print all the prime integers that are between
# A and B (including A and B). You can assume that B will always be bigger than or equal to A.

# Example Test Case 1: 1 5 -> 2 3 5
# Example Test Case 2: 50 100 -> 53 59 61 67 71 73 79 83 89 97
# Example Test Case 3: -3 10 -> 2 3 5 7
# Example Test Case 4: 24 28 ->

# ToDo

# Question 7 - Grade
# There are n students enrolled in the CmpE150 course. At the end of the semester students
# can pass the course only if they attended at least 75% of the lectures and have a minimum
# overall score of 50, otherwise they fail.
# A student passes CmpE150
#       with "A" if s/he has an overall score that is greater than or equal to 80,
#       with "B" if s/he has an overall score that is greater than or equal to 65,
#       with "C" if s/he has an overall score that is greater than or equal to 50.
# Write a program that prints the number of students that passed with "A", "B", "C" and
# the students that failed the course by taking n (the number of students), then the attendance
# (as a percentage) and the overall scores of these students.

# Example Test Case 1:
# 4
# 75 90
# 75 60
# 60 60
# 75 40
# ->
# Passed with A: 1
# Passed with B: 0
# Passed with C: 1
# Failed the course: 2

# Example Test Case 2:
# 3
# 5 40
# 80 100
# 98 50
# ->
# Passed with A: 1
# Passed with B: 0
# Passed with C: 1
# Failed the course: 1

# ToDo

# Question 8 - FizzBuzz
# FizzBuzz is a simple game played by 2 people. Players should count in turns, yet
# they are forbidden from saying numbers divisible by 3 or 5. Instead they should say "Fizz"
# instead of numbers divisible by 3,"Buzz" instead of numbers divisible by 5, and "FizzBuzz"
# for numbers divisible by 15.
# A demonstration:
# Player1: 1
# Player2: 2
# Player1: Fizz
# Player2: 4
# Player1: Buzz
# ...
# Player2: 14
# Player1: FizzBuzz
# Write a script that inputs a number and simulates a player's decision for a single number.

# ToDo

# Question 9 - Odd Print
# Given an integer N, prints N line such that i'th line consists of i times
# the number "i" if i is odd, else just print i.

# Example Test Case 1:
# 3
# ->
# 1
# 2
# 333

# Example Test Case 2:
# 5
# ->
# 1
# 2
# 333
# 4
# 55555

# ToDo

# Question 10 - Exponent
# Given two integers A and B, print "Yes" if A is an exponent of B, "No" otherwise.

# Example Test Case 1: 32 2 -> Yes
# Example Test Case 2: 1 13 -> Yes
# Example Test Case 3: 14 3 -> No

# ToDo

# Question 11 - Perfect Numbers
# In number theory, a perfect number is a positive integer that is equal to the sum of
# its positive divisors, excluding the number itself. For instance, 6 has
# divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.
# Given two positive integers N and M, write a function which finds all perfect numbers between N and M.

# Example Test Case 1: N = 1, M=15 -> 6
# Example Test Case 2: N = 1, M=150 -> 6 28
# Example Test Case 3: N = 1, M=1500 ->	6 28 496
# Example Test Case 4: N = 1, M=10000 -> 6 28 496 8128

# ToDo