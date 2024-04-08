# Cmpe 150 Lab 7 Questions

# Question 1 - Reverse Lines
# Write a program that prompts for a file name and reverses each line of the file
# and writes the resulting list of lines to a new file.
# Assume that given file name exists in the same repository with your code file.

# Example Test Case:
# Input File
# Eating raw fish didn't sound like a good idea
# "It's a delicacy in Japan," didn't seem to make it any more appetizing
# Raw fish is raw fish, delicacy or not

# Output File
# aedi doog a ekil dnuos t'ndid hsif war gnitaE
# gniziteppa erom yna ti ekam ot mees t'ndid ",napaJ ni ycaciled a s'tI"
# ton ro ycaciled ,hsif war si hsif waR

file_name = input()
f_in = open('./' + file_name, 'r')
f_out = open('./output.txt', 'w')
for line in f_in.readlines():
    f_out.write(line.strip()[::-1])
    f_out.write('\n')
f_in.close()
f_out.close()

# Question 2 - Pluralize
# Write a program which takes a file name and reads file that has one word each line.
# It should pluralize only the words that is made up only letters and will print out
# the pluralized form of these words in to an output file called pluralWords.txt.
# If the last letter of a word is 'y', drop 'y' and add 'ies' (cherry to cherries).
# In other cases add 's' to that word (orange to oranges).
# Hint: Using x.isalpha() function which checks if all characters of the string is
# from the alphabet.

# Example Test Case:
# input.txt
# lady
# CMPE150
# phone
# Mr.Nobody
# area51
# 8ship
# student
# secretary
# Dr.ErolBey
# python_variable
# Hello!
# system

# output.txt
# ladies
# phones
# students
# secretaries
# systems

file_name = input()
f_in = open(file_name, 'r')
f_out = open('output.txt', 'w')
for line in f_in.readlines():
    if line.strip().isalpha():
        if line.strip()[-1] == 'y':
            f_out.write(line.strip()[:-1] + 'ies' + '\n')
        else:
            f_out.write(line.strip() + 's' + '\n')
f_in.close()
f_out.close()

# Question 3 - Correct Grades
# Write a program which reads the file named grades.txt which has Midterm 1 grades on the first line,
# Midterm 2 grades on the second line and Final grades on the third line. Assume that each line has
# the same number of grades. Correct the grades such that nonnegative grades will be replaced by 0.
# Write the resulting grades to corrected.txt.
# Hint: You can change the value of elements in a list. e.g. x_list[5] = ...

# Example Test Case:
# grades.txt
# 70 85 0 -5 20 100
# 100 50 45 30 -10 90
# -3 50 30 25 60 85

# corrected.txt
# 70 85 0 0 20 100
# 100 50 45 30 0 90
# 0 50 30 25 60 85

f_in = open('grades.txt', 'r')
f_out = open('corrected.txt', 'w')
for line in f_in.readlines():
    grades = line.split()
    for i in range(len(grades)):
        if grades[i][0] == '-':
            grades[i] = '0'
    f_out.write(' '.join(grades) + '\n')
f_in.close()
f_out.close()

# Question 4 - Read Lines Incrementally
# Write a function which takes the path of the file to be read as a parameter.
# Then at the beginning, prints the first line. After putting a new line,
# print the first 2 lines. Then 3 and so on until printing all the lines.

# Example Test Case:
# input.txt
# Days of the week
# There are seven days of the week, or uniquely named 24-hour periods
# Monday is viewed by many to be the "worst" day of the week
# Tuesday is the second day of the week, and is in many ways similar
# Wednesday is the third day of the week, and serves as the "middle"

# Output
# Days of the week
#
# Days of the week
# There are seven days of the week, or uniquely named 24-hour periods
#
# Days of the week
# There are seven days of the week, or uniquely named 24-hour periods
# Monday is viewed by many to be the "worst" day of the week
#
# Days of the week
# There are seven days of the week, or uniquely named 24-hour periods
# Monday is viewed by many to be the "worst" day of the week
# Tuesday is the second day of the week, and is in many ways similar
#
# Days of the week
# There are seven days of the week, or uniquely named 24-hour periods
# Monday is viewed by many to be the "worst" day of the week
# Tuesday is the second day of the week, and is in many ways similar
# Wednesday is the third day of the week, and serves as the "middle"

def read_incrementally(path):
    f = open(path, 'r')
    n_lines = len(f.readlines())
    f.close()
    for i in range(1, n_lines+1):
        print_first_n_lines(path, i)
        print()

def print_first_n_lines(path, i):
    f = open(path, 'r')
    count = 0
    while count < i:
        print(f.readline(), end='')
        count += 1
    f.close()

read_incrementally('./input.txt')

# Question 5 - Write Odd Numbers
# Write a function called write_odd_numbers which takes a string parameter
# corresponding to the path of the output file. Then it reads numbers
# from the user until 0 is entered. It writes all the odd numbers entered
# into a new line of the file.

# Example Test Case
# Input
# 5 7 4432 34 -3 -532 3 5 0
# odd_numbers.txt
# 5
# 7
# -3
# 3
# 5

def write_odd_numbers(output_path):
    f_out = open(output_path, 'a')
    while True:
        num = int(input())
        if num == 0:
            break
        if num % 2 == 1:
            f_out.write(str(num) + '\n')
    f_out.close()

write_odd_numbers('odd_numbers.txt')

# Question 6 - Write Odd Numbers Multiple Times
# Call the function you defined in the previous question multiple times.
# If you call it 3 times, for instance, all the odd numbers should be existing
# in the final file. Be careful about which mode to open the file for this goal.

write_odd_numbers('odd_numbers.txt')
write_odd_numbers('odd_numbers.txt')
write_odd_numbers('odd_numbers.txt')

# Be careful to use 'a' instead of 'w' to be able to append.

# Question 7 - lower
# Implement the lower function defined for strings. It should take a single string
# parameter and return its lowercase version.
# Hint: You can use chr(index) function which gives the corresonding character for
# the given ascii index and ord(char) function that gives the corresonding integer for
# the given character

def lower(string):
    lower_str = ''
    for i in range(len(string)):
        if 'a' <= string[i] and string[i] <= 'z':
            lower_str += string[i]
        elif 'A' <= string[i] and string[i] <= 'Z':
            lower_str += chr(ord(string[i]) + ord('a') - ord('A'))    # To shift an upper case character by necessary amount
        else:
            lower_str += string[i]
    return lower_str

print(lower('ArKaDa 2 yaramaz oynuyordu.'))

# Question 8 - upper
# Implement the upper function defined for strings. It should take a single string
# parameter and return its uppercase version.
# Hint: You can use chr(index) function which gives the corresonding character for
# the given ascii index and ord(char) function that gives the corresonding integer for
# the given character

def upper(string):
    upper_string = ''
    for i in range(len(string)):
        if 'A' <= string[i] and string[i] <= 'Z':
            upper_string += string[i]
        elif 'a' <= string[i] and string[i] <= 'z':
            upper_string += chr(ord(string[i]) + ord('A') - ord('a'))  # To shift a lower case character by necessary amount
        else:
            upper_string += string[i]
    return upper_string

print(upper('ArKaDa 2 yaramaz oynuyordu.'))

# Question 9 - * for str and int
# Implement the * function defined for string and int pairs. It should take a string and a non-negative integer as
# parameters and return repeated version.

def star(string, integer):
    res = ''
    for i in range(integer):
        res += string
    return res

print(star('Example str', 5))
print('Example str' * 5 == star('Example str', 5))


# Question 10 - isalpha
# Implement the isalpha function defined for strings. It should take a single string
# parameter and return True if all of its characters are from the alphabet. Otherwise,
# it ought to return False

def isalpha(string):
    is_alpha = True
    for i in range(len(string)):
        if not check_is_alpha_for_character(string[i]):
            is_alpha = False
    return is_alpha

def check_is_alpha_for_character(character):
    return ('a' <= character and character <= 'z') or ('A' <= character and character <= 'Z')

print(isalpha("Thisstring"), "Thisstring".isalpha())
print(isalpha("This is a string"), "This is a string".isalpha())
print(isalpha("This is a string with a number 432"), "This is a string with a number 432".isalpha())
print(isalpha("This is a string with puncutation:"), "This is a string with puncutation:".isalpha())

