# Cmpe 150 Lab 2 Questions

# Q1: Take two integers from the user, and print them

number1 = input()
number2 = input()
print(number1, number2)

# Q2: Take two integers from the user (a, b), and then print their sum, difference, product, power and remainder.
# Example test case: 13 5 -> 18 8 65 371293 3

number1 = input()
number2 = input()
number1 = int(number1)
number2 = int(number2)
print('Sum:', number1 + number2)
print('Difference:', number1 - number2)
print('Product:', number1 * number2)
print('Power:', number1 ** number2)
print('Remainder:', number1 % number2)

# Q3: # Write a program that takes 3 integers from the user and then prints the sum, mean and multiple of the numbers.
# Example test case: 13 27 14	-> 54 18.00 4914

number1 = int(input())
number2 = int(input())
number3 = int(input())
sum = number1 + number2 + number3
print('Sum:', sum)
print('Mean:', sum / 3)
print('Multiplication:', number1 * number2 * number3)


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

def cash_machine(amount):
    n_banknotes = amount // 5
    n_coins = amount % 5
    print('Number of banknotes needed:', n_banknotes)
    print('Number of coins needed:', n_coins)

cash_machine(57)
cash_machine(269)
cash_machine(532623)

# Q5: Write a function that takes a radius and returns the volume of the sphere.
# 4 over 3 multiplied by pi (3.14) and radius cubed
# Example test case 1: 3 -> 113.0399
# Example test case 2: 6 -> 904.3199

def volume(radius):
    return (4 / 3) * 3.14 * (radius ** 3)

print(volume(3))
print(volume(6))
print(volume(5.734))

# Q6: Write a function called power that takes two integer parameter as number and n.
# The function should return the nth power of number.
# Example test case 1: 5 2 -> 25
# Example test case 2: 3 2 -> 9
# Example test case 3: 4 3 -> 64

def power(number1, number2):
    return number1 ** number2

print(power(5, 2))
print(power(3, 2))
print(power(4, 3))


# Q7: Write a program that asks the user their height in centimeters (integer) and their weight in kilograms (float).
# Calculate the user's body mass index (BMI) with the formula given below.
# BMI = weight(kg) / height(m)^2
# Example test case 1: 72 180 -> 	22.22
# Example test case 2: 79.5 172 -> 	26.87
# Example test case 3: 53.4 160 -> 	20.86
# Example test case 4: 81.2 165 -> 	29.83

weight_as_kilograms = float(input('Please enter your weight in terms of kilograms'))
height_as_centimeters = int(input('Please enter your height in terms of centimeters'))
height_as_meters = height_as_centimeters / 100
BMI = weight_as_kilograms / (height_as_meters ** 2)
print('BMI:', BMI)

# Q8: When you multiply an integer by itself, the result is a square number.
# Write a function that takes an integer and determines whether it is a square number or not.
# Do NOT use if or for since we haven't covered them yet.
# Example test case 1: 25 -> 	True
# Example test case 2: 23 -> 	False
# Example test case 3: 0  -> 	True
# Example test case 4: -1 -> 	False

def is_squared_number(number):
    # (number ** 0.5) is the square root of the given number
    # (int(number ** 0.5)) is just the integer part of the square root of the given number
    return (number >= 0) and (number ** 0.5 == int(number ** 0.5))

print('25', is_squared_number(25))
print('23', is_squared_number(23))
print('0', is_squared_number(0))
print('-1', is_squared_number(-1))
print('134258569', is_squared_number(134258569))
print('134258567', is_squared_number(134258567))


# Q9: A chemical mixture has 2 components, namely Component X and Component Y.
# Ask the user for the amount of X and Y in the mixture and then calculate
# the percentages of X and Y in the total solution.

# Example test case 1: 10 10   -> 	50.00% 50.00%
# Example test case 2: 10.5 21 -> 	33.33% 66.67%
# Example test case 3: 0.1 0.9 -> 	10.00% 90.00%

amount_of_X = float(input())
amount_of_Y = float(input())
total_amount = amount_of_X + amount_of_Y
print('Percentage of X:', (amount_of_X / total_amount) * 100, '%')
print('Percentage of Y:', (amount_of_Y / total_amount) * 100, '%')

# Q10: Emir wants to learn the wi-fi password. He asks the waiter, and the waiter says
# "The password is the x-1 times of the two least significant bases of 5^5628".
# Could you write a code that takes x as input and gives the wi-fi password as output?
# Example test case 1:  4 -> 75
# Example test case 2: 19 -> 450

print(5 ** 5628) # See that last two digits are 2 and 5, so we will use 25
x = int(input())
print('Password:', (x - 1) * 25)

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

number1 = float(input())
number2 = float(input())
number3 = float(input())
print(number1 - (number1 // 1), number2 - (number2 // 1), number3 - (number3 // 1), )


# Q12: We want to simulate a division operation. In order to do that, write a function that takes two integers,
# dividend and divisor respectively, perform the division operation and print out the quotient and the remainder.
# Example test case 1:  9 2      ->   quotient = 4 remainder = 1
# Example test case 2:  156 13   ->   quotient = 12 remainder = 0
# Example test case 3:  84 16    ->   quotient = 5 remainder = 4

def division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    print('Quotient:', quotient, 'Remainder:', remainder)

division(9, 2)
division(156, 13)
division(84, 16)

# Q13: You are in a biology lab observing reproducing bacteria. Every daughter cell grows up
# for a given time (t1) and becomes a parent cell, immediately dividing into two new daughter cells.
# These daughter cells then start the same process all over again.
# Given three integers, one representing the initial number of bacteria, one representing the time it takes
# daughter cells to become parent cells (t1), and one representing the total timewise length of the experiment.
# Write a function that returns the total number of bacteria at the end of the experiment.
# Example test case 1: 1 1 2 -> 	4
# Example test case 2: 5 3 8 -> 	20

def n_bacteria(initial_n, time_needed_for_growing, total_time):
    return initial_n * (2 ** (total_time // time_needed_for_growing))

print(n_bacteria(1, 1, 2))
print(n_bacteria(5, 3, 8))
# Notice below that exponential functions grow really fast
print(n_bacteria(38, 7, 218))
print(n_bacteria(38, 7, 2183))
print(n_bacteria(38, 7, 21834))


# Q14: Write a function that takes four integers representing (x, y) coordinates of two points and calculates
# the distance between these two points. First two integers are x and y coordinates of a point on a 2D plane.
# Next 2 integers are coordinates of another point on the same plane.
# Call this function with the following inputs and print the results:
# Example test case 1: 5 10 10 22  ->  13.00
# Example test case 2: -5 -10 -10 -22 ->  13.00

def euclidian_distance(x1, y1, x2, y2):
    return ( ( (x1 - x2) ** 2 ) + ( (y1 - y2) ** 2) ) ** 0.5

print(euclidian_distance(5, 10, 10 , 22))
print(euclidian_distance(-5, -10, -10 , -22))
print(euclidian_distance(5.723, 43.865, 3.76 , 243.067))


# Q15: Two runners run around a circular track. The first runner runs x1 meters in a minute.
# The second runner runs x2 meters in a minute. Write a function that takes 4 parameters:
# radius r in meters, x1, x2 and total time elapsed in minutes. The function first calculates the circumference of
# the circular track. Then calculate the completed number of laps so far (integer) by each runner and return them.
# Take π = 3.14.
# Call this function with following inputs and print the number of laps in the format below:
# Example test case 1: 100 300 400 30  -> 	First runner = 14 laps - Second runner = 19 laps
# Example test case 2: 25 150 250 15  -> 	First runner = 14 laps - Second runner = 23 laps
# Example test case 3: 35 550 400 10  -> 	First runner = 25 laps - Second runner = 18 laps


def calculate_information_for_runners(r, x1, x2, time_elapsed):
    circumference = 2 * 3.14 * r
    laps_by_the_first_runner = (time_elapsed * x1) // circumference
    laps_by_the_second_runner = (time_elapsed * x2) // circumference
    print('First runner =', laps_by_the_first_runner, 'laps - Second runner =', laps_by_the_second_runner, 'laps')

calculate_information_for_runners(100, 300, 400, 30)
calculate_information_for_runners(25, 150, 250, 15)
calculate_information_for_runners(35, 550, 400, 10)
calculate_information_for_runners(18.3, 47.76, 325.16, 7854)


# Q16: A telephone directory has 20 lines on each page, and each page has exactly 5 columns.
# Assume there is an entry in each column. Write a function that determines/returns on which page, column,
# and line the Xth entry is present. (Assume that page, line, column numbers, and X all start from 1.)
# Example test case 1: 156   -> 	2 12 1
# Example test case 1: 2348   -> 	24 10 3

def find_entry_position(entry_order):
    page = (entry_order // (20 * 5)) + 1
    line = ( (entry_order % (20 * 5)) // 5) + 1
    column = ( (entry_order % (20 * 5)) % 5)
    return page, line, column

page, line, column = find_entry_position(156)
print(page, line, column)
page, line, column = find_entry_position(2348)
print(page, line, column)


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

def calculate_passer_rating(pass_completions, pass_attempts, total_passing_yards, touchdowns, interceptions):
    C = ( ( (pass_completions / pass_attempts) * 100 ) - 30 ) / 20
    Y = ( (total_passing_yards / pass_attempts) - 3) / 4
    T = (touchdowns / pass_attempts) * 20
    I = 2.375 - ((interceptions / pass_attempts) * 35)
    passer_rating = ( (C + Y + T + I) / 6 ) * 100
    return passer_rating

print(calculate_passer_rating(183, 267, 2064, 17, 3))
print(calculate_passer_rating(117, 172, 1587, 12, 3))
