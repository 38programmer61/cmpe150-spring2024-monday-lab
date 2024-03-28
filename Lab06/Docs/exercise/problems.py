# Cmpe 150 Lab 6 Questions

# Question 1 - SpOnGeBoB MeMe
# Write a function that takes a string and returns it by converting it into a spongebob meme.
# Every letter with odd index should be lowercase and every letter with even index should be uppercase.

# Example Test Case 1: "stop making sponge bob memes" -> "StOp mAkInG SpOnGe bOb mEmEs"
# Example Test Case 2: "CMPE will be fun in the next few years" -> "CmPe wIlL Be fUn iN ThE NeXt fEw yEaRs"

# ToDo

# Question 2 - Convert string to camel case
# There are different naming conventions: lowercase lower_case_with_under_scores UPPERCASE CamelCase.
# Write a function that converts dash/underscore delimited words into camel casing. Every word should
# start with a uppercase letter and continue with lowercase letters. (known as Upper Camel Case or Pascal Case.)

# Example Test Case 1: "to_camel_case" -> "ToCamelCase"
# Example Test Case 2: "Hard_exam-pLe" -> "HardExamPle"
# Example Test Case 3: "unnecessarily-LONG-Example" -> "UnnecessarilyLongExample"

# ToDo

# Question 3 - Abbreviate
# Write a function called abbreviation() that takes a string st.
# If st has strictly more than 14 characters: returned string:
# has the same first and last two characters as st.
# the characters in the middle should be replaced by the number of characters being replaced.
# (if you are replacing 15 characters return value should look like ww15ww)
# Else return st as is.

# Example Test Case 1: "çekoslovakyalılaştıramadıklarımızdan" -> "çe32an"
# Example Test Case 2: "helo" -> "helo"

# ToDo

# Question 4 - Stop gninnipS My sdroW!
# Write a function that takes a string of one or more words, and returns
# the same string, but with all five or more letter words reversed.

# Example Test Case 1:
# "This is another test" -> "This is rehtona test"

# Example Test Case 2:
"You know you’re in love when you can’t fall asleep because reality is finally better than your dreams."
# ->
# You know er’uoy in love when you t’nac fall peelsa esuaceb ytilaer is yllanif retteb than your .smaerd

# Example Test Case 3:
# "Difficulties are what make life interesting and overcoming them is what makes life meaningful."
# ->
# "seitluciffiD are what make life gnitseretni and gnimocrevo them is what sekam life .lufgninaem"

# ToDo

# Question 5 - Requirements
# Write a function which takes a password as parameter and return whether the password is
# valid or not. The password has the following requirements:
# The password must be at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, one uppercase letter, and one number.

# Example Test Case 1: "Covid19" -> True
# Example Test Case 2: "123456" -> False

# ToDo

# Question 6 - Length
# Write a function to find shortest and largest word in a given string.

# Example Test Case 1: "the house is a long way from here" -> a house
# Example Test Case 2: "This room is exclusively for women" -> is exclusively

# ToDo

# Question 7 - Alphabetical order
# Write a function that accepts a comma separated sequence of words as input and
# returns the words in sorted form (alphanumerically).

# Example Test Case:
# red, white, black, red, green, black -> black, black, green, red, red, white

# ToDo

# Question 8 - Not poor
# Write a function to find the first appearance of the substring 'not' and 'poor'
# from a given string, if 'not' is followed by the 'poor', replace the whole 'not'...'poor'
# substring with **'good'. ** and return the resulting string.

# Example Test Case 1: "The lyrics is not that poor!" -> "The lyrics is good!"
# Example Test Case 2: "The lyrics is poor!" -> "The lyrics is poor!"

# ToDo

# Question 9 - Find and replace
# Write a function that takes 3 strings input, a and b and replaces all the instances of a in input with b.

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

# ToDo

# Question 10: Prefix
# Given a string in the format "operator number number", return the result of the operation
# Numbers will not include minus signs. Operators will be from the set {+, -, *, /}
# Example Test Case 1: - 5 33 -> -28
# Example Test Case 2: * 30 3 -> 90

# ToDo
