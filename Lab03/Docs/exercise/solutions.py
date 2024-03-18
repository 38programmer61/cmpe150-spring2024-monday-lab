# Cmpe 150 Lab 3 Questions

# Question 1 - Stars
# Question 1a
# Write a program that prints 1 star ('*') to the screen.

print('*')

# Question 1b
# Write a program that prints 10 stars ('*') next to each other to the screen.

for i in range(10):
    print('*', end='')

# Question 1c
# Write a function that takes an integer N as a parameter and prints N stars ('*') vertically to the screen.

def print_N_stars_vertically(N):
    for i in range(N):
        print('*')

print_N_stars_vertically(5)
print()
print_N_stars_vertically(15)
print()
print_N_stars_vertically(10000)

# Question 1d
# Write a function that takes an integer N as a parameter and prints N stars ('*') next to each other to the screen.

def print_N_stars_horizontally(N):
    for i in range(N):
        print('*', end='')

print_N_stars_horizontally(5)
print()
print_N_stars_horizontally(15)
print()
print_N_stars_horizontally(10000)

# Question 2 - Numbeeeers

# Write a function that takes an integer N as a parameter and prints numbers from 1 to N to the screen.

# Example test case 1: 5 -> 1 2 3 4 5
# Example test case 2: 2 -> 1 2

def print_one_to_N(N):
    for i in range(1, N+1):
        print(i, end='')
        print(' ', end='')

print_one_to_N(5)
print()
print_one_to_N(2)
print()
print_one_to_N(10000)

# Question 3 - Hooping Numbers

# Question 3a
# Write a function that takes 3 integers A, B and t as parameters.
# Then prints numbers from A to B with increment of t. Assume that B > A.

# Example test case 1: 7 16 3 -> 7 10 13 16
# Example test case 2: 2 30 6 -> 2 8 14 20 26

def print_incrementally(A, B, t):
    for i in range(A, B+1, t):
        print(i, end=' ')

print_incrementally(7, 16, 3)
print()
print_incrementally(2, 30, 6)

# Question 3b
# Write a function that takes 3 integers A, B and t as parameters.
# Then prints numbers from B to A with decrement of t. Assume that B > A.

# Example test case 1: 7 16 3 -> 16 13 10 7
# Example test case 2: 2 30 6 -> 30 24 18 12 6

def print_decrementally(A, B, t):
    for i in range(B, A-1, -t):
        print(i, end=' ')

print_decrementally(7, 16, 3)
print()
print_decrementally(2, 30, 6)

# Question 4 - Numbeeeers

# Write a function that takes two integers A and B as parameters.
# Then returns the sum of numbers between A and B (excluding A and B).
# Assume that B > A.

# Example test case 1: 3 8 -> 22
# Example test case 2: 2 13 -> 75
# Example test case 3: 3 5 -> 4

def sum_between_a_and_b(A, B):
    summation_result = 0
    for i in range(A+1, B):
        summation_result = summation_result + i
    return summation_result

print(sum_between_a_and_b(3, 8))
print(sum_between_a_and_b(2, 13))
print(sum_between_a_and_b(3, 5))
print(sum_between_a_and_b(4, 5323))

# Question 5 - Average Team
# Write a program that reads a number N, then reads N more numbers. Calculate the average of those N numbers.

# Example test case 1:
# 4
# 4 9 5 2
# ->
# 5.0

# Example test case 2:
# 1
# 8
# ->
# 8.0

N = int(input())
summation_result = 0
for i in range(N):
    number = int(input())
    summation_result += number
print('Average:', summation_result / N)

# Question 6 - POW
# Write a function that takes 2 integers a and b as parameters, then returns the result of a^b (a*a*a...*a*a).
# Do NOT use ** instead try to use a for loop

# Example test case 1: 3 4 -> 81
# Example test case 2: 2 10 -> 1024

def calculate_power(a, b):
    product_result = 1
    for i in range(b):
        product_result = product_result * a
    return product_result

print(calculate_power(3, 4), 3 ** 4)
print(calculate_power(2, 10), 2 ** 10)
print(calculate_power(4, 87), 4 ** 87)

# Question 7 - Factorial
# Write a function that takes an integer n as a parameter and then returns n!.

# Example test case 1: 5 -> 120
# Example test case 2: 10 -> 3628800

def factorial(n):
    factorial_result = 1
    for i in range(1, n+1):
        factorial_result *= i
    return factorial_result

print(factorial(5))
print(factorial(10))
print(factorial(67))

# Question 8 - Sum of Products
# Write a function that takes an integer as a parameter and then reads n lines containing two integers from the user.
# The function then multiplies the integers in the same line and sums all the products.

# Example test case 1:
# 3
# 1 2
# 2 3
# 3 4
# ->
# 20

# Example test case 2:
# 2
# 3 4
# 5 10
# ->
# 62

def sum_of_products(n):
    summation = 0
    for i in range(n):
        number1 = int(input())
        number2 = int(input())
        summation = summation + number1 * number2
    return summation

print(sum_of_products(3))
print(sum_of_products(2))

# Nested Loops

# Question 1 - Rectangle

# Question 1a
# Write a function which takes two positive integers N and M as parameters then prints a rectangle with size NxM.

# Example test case 1:
# 3 4
# ->
# ****
# ****
# ****

# Example test case 2:
# 2 6
# ->
# ******
# ******

def print_rectangle_with_asterisk(N, M):
    for i in range(N):
        for j in range(M):
            print('*', end='')
        print()

print_rectangle_with_asterisk(3, 4)
print()
print_rectangle_with_asterisk(2, 6)

# Question 1b
# Write a function which takes two positive integers N and M as parameters then prints a rectangle with
# size NxM which has stars (*) at borders, and lines (-) inside.

# Example test case 1:
# 3 3
# ->
# ***
# *-*
# ***

# Example test case 2:
# 4 5
# ->
# *****
# *---*
# *---*
# *****

def print_bordered_rectangle_with_asterisk_and_dash(N, M):
    print_a_line_with_asterisk(M)
    print_inner_lines(N, M)
    print_a_line_with_asterisk(M)

def print_a_line_with_asterisk(M):
    for j in range(M):
        print('*', end='')
    print()

def print_inner_lines(N, M):
    for i in range(N-2):
        print('*', end='')
        for j in range(M-2):
            print('-', end='')
        print('*')

print_bordered_rectangle_with_asterisk_and_dash(3, 3)
print()
print_bordered_rectangle_with_asterisk_and_dash(4, 5)
print()
print_bordered_rectangle_with_asterisk_and_dash(10, 15)

# Question 2 - TriNumber/
# Question 2a
# Write a function which takes N as a parameter then display a right angle triangle using the number N,
# which will repeat the number for that row, like below.

# Example test case 1:
# 3
# ->
# 1
# 22
# 333

# Example test case 2:
# 5
# ->
# 1
# 22
# 333
# 4444
# 55555

def print_right_triangle_by_repeating_numbers(N):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(i, end='')
        print()

print_right_triangle_by_repeating_numbers(3)
print()
print_right_triangle_by_repeating_numbers(5)
print()
print_right_triangle_by_repeating_numbers(9)

# Question 2b
# Write a function which takes N as a parameter then display a right angle triangle using the number N,
# which will repeat the number for that row, like below.

# Example test case 1:
# 3
# ->
# 1
# 12
# 123

# Example test case 2:
# 5
# ->
# 1
# 12
# 123
# 1234
# 12345

def print_right_triangle_by_incrementing_numbers(N):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(j, end='')
        print()

print_right_triangle_by_incrementing_numbers(3)
print()
print_right_triangle_by_incrementing_numbers(5)
print()
print_right_triangle_by_incrementing_numbers(9)

# Question 2c
# Write a function which takes two integer N and x as parameters and display a right angle triangle with
# N number of rows formed by powers of x as follows:

# Example test case 1:
# 3 4
# ->
# 4
# 4 16
# 4 16 64

# Example test case 2:
# 4 3
# ->
# 3
# 3 9
# 3 9 27
# 3 9 27 81

def print_right_triangle_by_taking_power(N, x):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(x ** j, end=' ')
        print()

print_right_triangle_by_taking_power(3, 4)
print()
print_right_triangle_by_taking_power(4, 3)

# Question 3 - TriHard

# Write a function which takes an integer N as a parameter and prints a right triangle which consists of N many lines.
#
# Example test case 1:
# 3
# ->
# --*
# -**
# ***

# Example test case 2:
# 5
# ->
# ----*
# ---**
# --***
# -****
# *****

def triHard(N):
    for i in range(1, N+1):
        for j in range(N - i):
            print('-', end='')
        for j in range(i):
            print('*', end='')
        print()

triHard(3)
print()
triHard(5)
print()
triHard(100)