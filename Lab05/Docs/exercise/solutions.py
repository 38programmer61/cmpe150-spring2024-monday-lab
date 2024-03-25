# Cmpe 150 Lab 5 Questions

# Question 1 - Fibonacci
# Write a program which reads a positive integer number N and prints the Nth fibonacci number. 0, 1, 1, 2, 3, 5, ...
# F0 = 0
# F1 = 1
# Fn = Fn-2 + Fn-1

# Example Test Case 1: 2 -> 1
# Example Test Case 2: 3 -> 2
# Example Test Case 3: 6 -> 8

N = int(input())
count = 2
current_val = 1
prev_val = 0
while count <= N:
    new_val = prev_val + current_val
    prev_val = current_val
    current_val = new_val
    count = count + 1

print('fibonacci(', N, '):', current_val)

# Question 2 - Second Largest
# Write a program that will take nonnegative integers as inputs until the user enters 0.
# Then prints the difference between of largest two numbers among given inputs.

# Example Test Case 1: 12 25 3 8 0 -> 13
# Example Test Case 2: 15 1 2 3 8 5 0 -> 7

greatest_num = -1
second_greatest_num = -2
while True:
    current_num = int(input())
    if current_num == 0:
        break
    if current_num >= greatest_num:
        second_greatest_num = greatest_num
        greatest_num = current_num
    elif current_num >= second_greatest_num:
        second_greatest_num = current_num

print(greatest_num - second_greatest_num)

# Question 3 - Digiiiits
# Write a function that takes a positive number as a parameter and returns its total digit count and sum of even digits.

# Example Test Case 1: 542175 -> 6 6
# Example Test Case 2: 24680 -> 5 20
# Example Test Case 3: 135 -> 3 0

def digiiits(num):
    sum_of_even_digits = 0
    n_digits = 0
    while num > 0:
        n_digits += 1
        if (num % 10) % 2 == 0:
            sum_of_even_digits += num % 10
        num = num // 10
    return n_digits, sum_of_even_digits

print(digiiits(542175))
print(digiiits(24680))
print(digiiits(135))

# Question 4 - Positive Mental Attitude
# Write a function that will take integers as inputs until the user enters a negative number.
# Then prints the user the sum of all ODD non-negative numbers that is entered.

# Example Test Case 1: 4 7 45 9 2 0 0 5 8 -4 -> 66
# Example Test Case 2: 1 1 0 1 -1 -> 3

def sum_all_odd_nonnegative():
    sum_of_all_odd_nonnegatives = 0
    current_num = int(input())
    while current_num >= 0:
        if current_num % 2 == 1:
            sum_of_all_odd_nonnegatives += current_num
        current_num = int(input())
    print(sum_of_all_odd_nonnegatives)

sum_all_odd_nonnegative()

# Question 5 - NoBig
# Write a function that reads numbers until the entered number is greater than the previous entered number.
# Then return the average of all entered numbers except the last one. Assume that at least two numbers will be entered.

# Example Test Case 1: 5 4 3 3 8 -> 3.75
# Example Test Case 2: 1 2 -> 1.0
# Example Test Case 3: 100 54 46 2 3 -> 50.5

def NoBig():
    prev_num = int(input())
    current_num = int(input())
    summation = prev_num
    count = 1
    while current_num <= prev_num:
        summation += current_num
        count += 1
        prev_num = current_num
        current_num = int(input())
    return summation / count

print(NoBig())

# Question 6 - Guess
# Generate a random number between 1 and 100 (including 1 and 100). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right. Also print the number of tries.
# Hint: You can use random.randint() but do not forget to say random.seed(5434) before calling to make the code
# reproducible (5434 is an arbitrary number)

# Example Test Case:
# 35 Too low!
# 67 Too low!
# 73 Too high!
# 71 You got it! And it only took you 4 tries!

import random           # We have to import random library to use randint function belonging to it.

# random.seed(5434)         When you change 5434 to something else it will generate a different number.
#                           If it is not uncommented, it will generate a different number each time, so hard to debug
number = random.randint(1, 100)
# print(number)   # To help debug the code
n_guesses = 0
while True:
    guess = int(input())
    n_guesses += 1
    if guess == number:
        if n_guesses == 1:
            print('You got it! And it only took you', n_guesses, 'try!')
            break
        else:
            print('You got it! And it only took you', n_guesses, 'tries!')
            break
    elif guess < number:
        print('Too low!')
    else:
        print('Too high!')

# Question 7 - Sum Facts
# Write a function which takes an integer as a parameter and returns the sum of the factorial of each digit.
# For example, assume that the user enters 572 as the input. For each digit of the integer, you will
# compute the factorial. Then you will compute the sum of these factorials: 5! + 7! + 2! = 120 + 5040 + 2 = 5162.

# Example Test Case 1: 572 -> 5162
# Example Test Case 2: 27 -> 5042

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res

# print(factorial(0))
# print(factorial(4))
# print(factorial(6))
# print(factorial(9))

def sum_facts(num):
    summation = 0
    while num > 0:
        last_digit = num % 10
        summation += factorial(last_digit)
        num = num // 10
    return summation

print(sum_facts(572))
print(sum_facts(27))
print(sum_facts(10))
print(sum_facts(997683))

# Question 8 - Sum of Digits
# Write a function that takes a nonnegative integer num as a parameter and returns sum of all digits. If the result
# has more than one digit, continue to calculate in this way until a single digit number is produced.
# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6

# Example Test Case 1: 942 -> 6
# Example Test Case 2: 17703 -> 9

def sum_of_digits(num):
    while num >= 10:
        summation = 0
        while num > 0:
            summation += num % 10
            num = num // 10
        num = summation     # Forget the actual number just use the summation of digits for the next iteration
    return num

print(sum_of_digits(942))
print(sum_of_digits(17703))
print(sum_of_digits(0))
print(sum_of_digits(2))
print(sum_of_digits(52347))

# Question 9 - Prime factors
# Question 9a
# Write a function that takes an integer N as a parameter and prints all the numbers that can divide N.

# Example Test Case 1: 21 -> 1 3 7 21
# Example Test Case 2: 30 -> 1 2 3 5 6 10 15 30

def all_numbers_dividing_N(N):
    for i in range(1, N+1):
        if N % i == 0:
            print(i, end=' ')
    print()

all_numbers_dividing_N(21)
all_numbers_dividing_N(30)

# Question 9b
# Write a function that takes an integer N as a parameter and prints the prime factorization of N.
# Hint: A non-prime number is always composed of prime numbers smaller than it.

# Example Test Case 1: 21 -> 3 * 7
# Example Test Case 2: 60 -> 2 * 2 * 3 * 5

def prime_factorization_1(N):
    print(N, '=', end=' ')

    has_printed_the_first_prime = False
    current_prime = find_next_prime(N, 1)
    while N > 1:
        while N % current_prime == 0:
            if has_printed_the_first_prime:
                print('*', current_prime, end=' ')
            else:
                print(current_prime, end=' ')
                has_printed_the_first_prime = True
            N = N // current_prime
        current_prime = find_next_prime(N, current_prime)

    print()

def check_is_prime(num):
    if num < 2:
        return False
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):     # range(2, num) would also work, but it is very slow
        if num % i == 0:
            is_prime = False
    return is_prime

# print(check_is_prime(1))
# print(check_is_prime(2))
# print(check_is_prime(3))
# print(check_is_prime(4))
# print(check_is_prime(5))
# print(check_is_prime(19))
# print(check_is_prime(39))
# print(check_is_prime(9673))

def find_next_prime(N, current_val):
    for i in range(current_val+1, N+1):
        if check_is_prime(i) and N % i == 0:
            return i

prime_factorization_1(21)
prime_factorization_1(60)
prime_factorization_1(512)
prime_factorization_1(637864234)

# Question 9c
# Write a function that takes an integer N as a parameter and prints the prime factorization
# of N in the form of exponents.

# Example Test Case 1: 21 -> 3^1 * 7^1
# Example Test Case 2: 60 -> 2^2 * 3^1 * 5^1

def prime_factorization_2(N):
    print(N, '=', end=' ')

    current_prime = find_next_prime(N, 1)
    while N > 1:
        count_factors = 0
        while N % current_prime == 0:
            N = N // current_prime
            count_factors += 1
        print('(', current_prime, '^', count_factors, ')', end=' ')
        current_prime = find_next_prime(N, current_prime)
        if N > 1:
            print('*', end=' ')

    print()

def find_next_prime(N, current_val):
    for i in range(current_val+1, N+1):
        if check_is_prime(i) and N % i == 0:
            return i

def check_is_prime(num):
    if num < 2:
        return False
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):     # range(2, num) would also work, but it is very slow
        if num % i == 0:
            is_prime = False
    return is_prime

prime_factorization_2(21)
prime_factorization_2(60)
prime_factorization_2(512)
prime_factorization_2(637864234)

