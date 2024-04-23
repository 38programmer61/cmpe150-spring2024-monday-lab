# Cmpe 150 Lab 10 Questions

# Critical Note: Please solve the examples 1-5 below using recursion
# although they can be solved by using a for loop or a while loop.

# Question 1
# Write a recursive function to find the factorial of a given number.

# Example Test Case:
# 6 -> 720

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)

print(factorial(0))
print(factorial(1))
print(factorial(6))
print(factorial(10))

# Question 2:
# Implement a recursive function (`get_fib`) that returns the n'th number
# in the Fibonacci sequence.
# Each number is the sum of the two preceding ones, starting from 0 and 1.

# Example Test Case:
# 5 -> 3

def fib(N):
    if N > 0 and N < 3:
        return N-1
    return fib(N-1) + fib(N-2)

print(fib(5))
print(fib(1))
print(fib(2))
print(fib(15))
for i in range(1, 31):
    print('Fib(', i, '):', fib(i))

# Question 3:
# Write a recursive function reverse_string(s) that takes a string s as
# an input and returns its reverse.

# Example Test Case:
# "hhow" -> "wohh"

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hhow"))
print(reverse_string("This is another 1 string to try if It WORKS"))

# From https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
# Question 4
# Write a Python function to calculate the sum of a list of numbers using recursion.

# Example Test Case:
# [4, 654, 2, 321] -> 981

def sum_list(List):
    if len(List) == 0:
        return 0
    return List[0] + sum_list(List[1:])

print(sum_list([4, 654, 2, 321]))
print(sum_list([4, 654, 2, -321]))

# Question 5
# Write a Python function to determine the number of digits for a given positive integer using recursion.

# Example Test Case:
# 734732 -> 6

def n_digits(num):
    if num == 0:
        return 0
    return 1 + n_digits(num // 10)

print(n_digits(734732))
print(n_digits(734730))

# Question 6
# Write a program that takes an integer n and then prints related hailstone sequence
# until 1. If number is even, divide it by 2. If number is odd, multiply it by 3 and add 1.

# Example Test Case 1:
# 20 -> 20 10 5 16 8 4 2 1

# Example Test Case 2:
# 12 -> 12 6 3 10 5 16 8 4 2 1

num = int(input())
while num != 1:
    print(int(num), end=' ')
    if num % 2 == 0:
        num = num / 2
    else:
        num = 3 * num + 1
print(1)

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

def calculate_sum_of_series(N):
    res = 0
    for i in range(1, N+1):
        res += int(str(N) * i)
    return res

print(calculate_sum_of_series(2))
print(calculate_sum_of_series(6))
print(calculate_sum_of_series(3))
print(calculate_sum_of_series(10))
print(calculate_sum_of_series(0))
print(calculate_sum_of_series(1))

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

def binary_search(List, target_num):
    List = sorted(List)
    min_limit, max_limit = -1, len(List) # Limits are exclusive
    cur_index = (min_limit + max_limit) // 2
    while max_limit - min_limit > 1:
        if List[cur_index] == target_num:
            return str(target_num) + ' exists in the list. Sorted index: ' + str(cur_index)
        elif List[cur_index] < target_num:
            min_limit = cur_index
        else:
            max_limit = cur_index
        cur_index = (min_limit + max_limit) // 2
    return str(target_num) + ' does not exists in the list.'

print(binary_search([ 1 , 3 , 4 , 5 , 6], 5))
print(binary_search([ 21 , 13 , 4.4 , 85 , 60], 16))
print(binary_search([ 21 , 13 , 4.4 , 85 , 60, -3.2], -3.2))
print(binary_search([ 21 , 13 , 4.4 , 85 , 60, -3.2], 22.543))


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

def check_is_disarium(num):
    num_str = str(num)
    sum = 0
    for i in range(len(num_str)):
        sum += int(num_str[i]) ** (i+1)
    return sum == num

print(check_is_disarium(544))
print(check_is_disarium(518))
print(check_is_disarium(466))
print(check_is_disarium(8))

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

def gcd(a, b):
    # The following two lines does the following: If one of the numbers is zero, returns the other one.
    if a * b == 0:
        return a + b
    return gcd(max(a,b) % min(a, b), min(a, b))

print(gcd(11, 22))
print(gcd(99, 100))
print(gcd(4, 1024))
print()

def relatively_prime(a, b):
    return gcd(a, b) == 1

print(relatively_prime(66, 33))
print(relatively_prime(8, 99))
print(relatively_prime(111, 11))
print()

def euler_totient(a):
    count = 0
    for i in range(1, a):
        if relatively_prime(i, a):
            count += 1
    return count

print(euler_totient(10))
print(euler_totient(342))
print(euler_totient(76))
print()

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

def carrier(weight, profit, limit):
    profit_by_unit_weight = []
    for i in range(len(weight)):
        profit_by_unit_weight.append(profit[i] / weight[i])
    cur_weight, max_profit = 0, 0
    while True:
        remaining_weight = limit - cur_weight
        most_profitable_weight_index = find_most_profitable_weight_index(profit_by_unit_weight)
        if weight[most_profitable_weight_index] < remaining_weight:
            max_profit += weight[most_profitable_weight_index] * profit_by_unit_weight[most_profitable_weight_index]
            cur_weight += weight[most_profitable_weight_index]
            profit_by_unit_weight[most_profitable_weight_index] = 0 # To disallow the selection of the already used ones.
        else:
            max_profit += remaining_weight * profit_by_unit_weight[most_profitable_weight_index]
            return max_profit

def find_most_profitable_weight_index(profit_by_unit_weight):
    max_val = max(profit_by_unit_weight)    # You can call max function by giving a list as well.
    return profit_by_unit_weight.index(max_val)

print(carrier([10, 20, 30], [4 , 5 , 60], 30))
print(carrier([10, 20, 30], [4 , 5 , 60], 50))
print(carrier([10, 20, 30], [4 , 5 , 60], 60))
print(carrier([30, 20, 40, 10, 70], [20, 30, 40, 70, 10], 200))


