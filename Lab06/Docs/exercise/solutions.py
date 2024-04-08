# Cmpe 150 Lab 6 Questions

# Question 1 - SpOnGeBoB MeMe
# Write a function that takes a string and returns it by converting it into a spongebob meme.
# Every letter with odd index should be lowercase and every letter with even index should be uppercase.

# Example Test Case 1: "stop making sponge bob memes" -> "StOp mAkInG SpOnGe bOb mEmEs"
# Example Test Case 2: "CMPE will be fun in the next few years" -> "CmPe wIlL Be fUn iN ThE NeXt fEw yEaRs"

def SpOnGeBoB_MeMe(original_str):
    SpOnGeBoB_MeMe_str = ""
    for i in range(len(original_str)):
        if i % 2 == 0:
            SpOnGeBoB_MeMe_str += original_str[i].upper()
        else:
            SpOnGeBoB_MeMe_str += original_str[i].lower()
    return SpOnGeBoB_MeMe_str

print(SpOnGeBoB_MeMe("stop making sponge bob memes"))
print(SpOnGeBoB_MeMe("CMPE will be fun in the next few years"))

# Question 2 - Convert string to camel case
# There are different naming conventions: lowercase lower_case_with_under_scores UPPERCASE CamelCase.
# Write a function that converts dash/underscore delimited words into camel casing. Every word should
# start with a uppercase letter and continue with lowercase letters. (known as Upper Camel Case or Pascal Case.)

# Example Test Case 1: "to_camel_case" -> "ToCamelCase"
# Example Test Case 2: "Hard_exam-pLe" -> "HardExamPle"
# Example Test Case 3: "unnecessarily-LONG-Example" -> "UnnecessarilyLongExample"

def camel_case(original_str):
    camel_case_str = ""
    index = 0
    while index < len(original_str):
        if index == 0:
            camel_case_str += original_str[index].upper()
        elif original_str[index] == "-" or original_str[index] == "_":
            camel_case_str += original_str[index+1].upper()
            index += 1
        else:
            camel_case_str += original_str[index].lower()
        index += 1
    return camel_case_str

print(camel_case("to_camel_case"), camel_case("to_camel_case") == "ToCamelCase")
print(camel_case("Hard_exam-pLe"), camel_case("Hard_exam-pLe") == "HardExamPle")
print(camel_case("unnecessarily-LONG-Example"), camel_case("unnecessarily-LONG-Example") == "UnnecessarilyLongExample")

# Question 3 - Abbreviate
# Write a function called abbreviation() that takes a string st.
# If st has strictly more than 14 characters: returned string:
# has the same first and last two characters as st.
# the characters in the middle should be replaced by the number of characters being replaced.
# (if you are replacing 15 characters return value should look like ww15ww)
# Else return st as is.

# Example Test Case 1: "çekoslovakyalılaştıramadıklarımızdan" -> "çe32an"
# Example Test Case 2: "helo" -> "helo"

def abbreviation(st):
    if len(st) <= 14:
        return st
    return st[:2] + str(len(st) - 4) + st[-2:]

print(abbreviation("çekoslovakyalılaştıramadıklarımızdan"), abbreviation("çekoslovakyalılaştıramadıklarımızdan") == "çe32an")
print(abbreviation("helo"), abbreviation("helo") == "helo")
print(abbreviation("helo4326434331"))
print(abbreviation("helo43264343431"))

# Question 4 - Stop gninnipS My sdroW!
# Write a function that takes a string of one or more words, and returns
# the same string, but with all five or more letter words reversed.

# Example Test Case 1:
# "This is another test" -> "This is rehtona test"

# Example Test Case 2:
# "You know you’re in love when you can’t fall asleep because reality is finally better than your dreams."
# ->
# You know er’uoy in love when you t’nac fall peelsa esuaceb ytilaer is yllanif retteb than your .smaerd

# Example Test Case 3:
# "Difficulties are what make life interesting and overcoming them is what makes life meaningful."
# ->
# "seitluciffiD are what make life gnitseretni and gnimocrevo them is what sekam life .lufgninaem"

def spin(original_str):
    spinned_str = ""
    words = original_str.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            spinned_str += words[i][::-1]
        else:
            spinned_str += words[i]
        if i != len(words) - 1:
            spinned_str += ' '
    return  spinned_str

print(spin("This is another test") == "This is rehtona test")
print(spin("You know you’re in love when you can’t fall asleep because reality is finally better than your dreams.") ==
      "You know er’uoy in love when you t’nac fall peelsa esuaceb ytilaer is yllanif retteb than your .smaerd")
print(spin("Difficulties are what make life interesting and overcoming them is what makes life meaningful.") ==
      "seitluciffiD are what make life gnitseretni and gnimocrevo them is what sekam life .lufgninaem")

# Question 5 - Requirements
# Write a function which takes a password as parameter and return whether the password is
# valid or not. The password has the following requirements:
# The password must be at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, one uppercase letter, and one number.

# Example Test Case 1: "Covid19" -> True
# Example Test Case 2: "123456" -> False

def check_pwd(pwd):
    return check_length(pwd) and check_has_lowercase(pwd) and check_has_uppercase(pwd) and check_has_number(pwd)

def check_length(pwd):
    return len(pwd) >= 6 and len(pwd) <= 20

def check_has_lowercase(pwd):
    has_lowercase = False
    for i in range(len(pwd)):
        if pwd[i] >= 'a' and pwd[i] <= 'z':
            has_lowercase = True
    return has_lowercase

def check_has_uppercase(pwd):
    has_uppercase = False
    for i in range(len(pwd)):
        if pwd[i] >= 'A' and pwd[i] <= 'Z':
            has_uppercase = True
    return has_uppercase

def check_has_number(pwd):
    has_number = False
    for i in range(len(pwd)):
        if pwd[i] >= '0' and pwd[i] <= '9':
            has_number = True
    return has_number

print(check_pwd("Covid19"))
print(check_pwd("123456"))

# Maybe a nicer solution
def check_pwd_2(pwd):
    return (check_length(pwd) and check_certain_chars(pwd, 'a', 'z') and
            check_certain_chars(pwd, 'A', 'Z') and check_certain_chars(pwd, '0', '9'))

def check_length(pwd):
    return len(pwd) >= 6 and len(pwd) <= 20

def check_certain_chars(pwd, start, end):
    has_char_within_interval = False
    for i in range(len(pwd)):
        if pwd[i] >= start and pwd[i] <= end:
            has_char_within_interval = True
    return has_char_within_interval

print(check_pwd_2("Covid19"))
print(check_pwd_2("123456"))

# Question 6 - Length
# Write a function to find shortest and largest word in a given string.

# Example Test Case 1: "the house is a long way from here" -> a house
# Example Test Case 2: "This room is exclusively for women" -> is exclusively

def find_shortest_and_longest_words(original_str):
    words = original_str.split()
    shortest_str = words[0]
    longest_str = words[0]
    for i in range(1, len(words)):
        if len(words[i]) > len(longest_str):
            longest_str = words[i]
        if len(words[i]) < len(shortest_str):
            shortest_str = words[i]
    return shortest_str, longest_str

print(find_shortest_and_longest_words("the house is a long way from here"))
print(find_shortest_and_longest_words("This room is exclusively for women"))

# Question 7 - Alphabetical order
# Write a function that accepts a comma separated sequence of words as input and
# returns the words in sorted form (alphanumerically).

# Example Test Case:
# red, white, black, red, green, black -> black, black, green, red, red, white

def alphabetical_order(original_str):
    words = original_str.split(', ')
    sorted_words = sorted(words)
    alphabetical_order_str = ', '.join(sorted_words)
    return alphabetical_order_str

print(alphabetical_order("red, white, black, red, green, black"),
      alphabetical_order("red, white, black, red, green, black") == "black, black, green, red, red, white")

# Question 8 - Not poor
# Write a function to find the first appearance of the substring 'not' and 'poor'
# from a given string, if 'not' is followed by the 'poor', replace the whole 'not'...'poor'
# substring with **'good'. ** and return the resulting string.

# Example Test Case 1: "The lyrics is not that poor!" -> "The lyrics is good!"
# Example Test Case 2: "The lyrics is poor!" -> "The lyrics is poor!"

def not_poor(original_str):
    not_start_index, not_end_index = find_start_and_end_indexes(original_str, 'not')
    poor_start_index, poor_end_index = find_start_and_end_indexes(original_str, 'poor')
    if not_start_index != len(original_str) and poor_start_index != len(original_str) and not_start_index < poor_start_index:
        return original_str[:not_start_index] + 'good' + original_str[poor_end_index+1:]
    else:
        return original_str

def find_start_and_end_indexes(original_str, word):
    index = original_str.find(word)
    if index < 0:
        return len(original_str), len(original_str) + 1
    else:
        return index, index + len(word) - 1

print(not_poor("The lyrics is not that poor!"), not_poor("The lyrics is not that poor!") == "The lyrics is good!")
print(not_poor("The lyrics is poor!"), not_poor("The lyrics is poor!") == "The lyrics is poor!")


# Question 9 - Find and replace
# Write a function that takes 3 strings input, a and b and replaces all
# the instances of a in input with b and returns that version.

# Example Test Case 1:
# "This is another test", "is", "is not" -> "This not is not another test"

# Example Test Case 2:
# "I mean, it went badly last time but surely it will go much better this time.",
# "it",	"filling zepplins with hydrogen",
# ->
# "I mean, filling zepplins with hydrogen went badly last time but surely filling
# zepplins with hydrogen will go much better this time."

# Example Test Case 3:
# "Test test TeSt te st TEst teSt crest TEA", "st TE", "test", -> "Test test TeSt te testst teSt cretestA"

def find_replace(original_str, a, b):
    new_str = original_str.replace(a, b)
    return new_str

print(find_replace("This is another test", "is", "is not") == "This not is not another test")
print(find_replace("I mean, it went badly last time but surely it will go much better this time.", "it","filling zepplins with hydrogen")
      == "I mean, filling zepplins with hydrogen went badly last time but surely filling zepplins with hydrogen will go much better this time.")
print(find_replace("Test test TeSt te st TEst teSt crest TEA", "st TE", "test") == "Test test TeSt te testst teSt cretestA")

# Question 10: Prefix
# Given a string in the format "operator number number", return the result of the operation
# Numbers will not include minus signs. Operators will be from the set {+, -, *, /}
# Example Test Case 1: - 5 33 -> -28
# Example Test Case 2: * 30 3 -> 90

def prefix(given_str):
    tokens = given_str.split()
    num1 = int(tokens[1])
    num2 = int(tokens[2])
    if tokens[0] == '+':
        return num1 + num2
    if tokens[0] == '-':
        return num1 - num2
    if tokens[0] == '*':
        return num1 * num2
    if tokens[0] == '/':
        return num1 / num2

print(prefix("- 5 33"))
print(prefix("* 30 3"))
print(prefix("+ 30 3"))
print(prefix("/ 30 3654"))
