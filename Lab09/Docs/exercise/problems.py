# Cmpe 150 Lab 9 Questions

# Question 1 - Letter Count

# Write a program that takes a string, then obtain a dictionary which has letters as keys and
# the counts of that letters as values.

# Example Test Case:
# What we think, we become. ->
# a -> 0.05263157894736842
# b -> 0.05263157894736842
# c -> 0.05263157894736842
# e -> 0.21052631578947367
# h -> 0.10526315789473684
# i -> 0.05263157894736842
# k -> 0.05263157894736842
# m -> 0.05263157894736842
# n -> 0.05263157894736842
# o -> 0.05263157894736842
# t -> 0.10526315789473684
# w -> 0.15789473684210525

# ToDo

# Question 2 - Different Types
# Write a program that takes list of different types, and defines a dictionary which has each
# different  type as keys and the list of elements of that type as as value. Then display all
# elements of each type like in the example.

# Example Test Case:
# [10, 4.20, False, 'Word', 'CMPE150', 30, 3.5, 9.99, 'oblivion', True, 68, 88, "88"]
# ->
# <class 'int'> -> [10, 30, 68, 88]
# <class 'float'> -> [4.2, 3.5, 9.99]
# <class 'bool'> -> [False, True]
# <class 'str'> -> ['Word', 'CMPE150', 'oblivion', '88']

# ToDo

# Question 3 - Zip Two Lists
# Write a function that takes 2 lists, then returns a dictionary which has keys from the
# first one, values from the second one.
# Assume that the lists have the same length

# Example Test Case:
# list1 = ["melih", "burak", "ahmet", "recep", "melis"] list2 = [1,2,3,4,5]
# ->
# {'melih': 1, 'burak': 2, 'ahmet': 3, 'recep': 4, 'melis': 5}

# ToDo

# Question 4 - Dictionary Merge
# Write a function that takes one or more dictionaries and combines them in one result dictionary.
# The keys in the given dictionaries can overlap. In that case you should combine all values in a list.
# Duplicate values should be preserved.

# Example Test Case 1:
# {"A": 1, "B": 2} {"A": 3} -> {"A": [1, 3]}, "B": [2]}

# Example Test Case 2:
# {"A": 1, "B": 2, "C": 3} -> {"A": [1], "B": [2], "C": [3]}

# Example Test Case 3:
# {"A": 1, "B": 2, "C": 3} {"A": 4, "D": 5} {"A": 4}
# ->
# {"A": [1, 4, 4], "B": [2], "C": [3], "D": [5]}

# ToDo

# Question 5 - Data Collection
# Write a program that reads lines from the input. Each line will be composed of 4 words,
# name of the game, genre of the game, year of release and the producer respectively.
# If a line is equal to "exit", stop reading. Store the games in a dictionary. Their
# values should also correspond to dictionaries composed of their genre, release_data
# and producer.

# Example Test Case:

# RDR2 Action 2018 Rockstar
# Fifa14 Sports 2013 EA
# Borderlands Shooter 2009 Gearbox
# Skyrim RPG 2011 Bethesda
# Wall-E Platform 2008 THQ
# exit
# ->
# {'RDR2': {'genre': 'Action', 'release_date': '2018', 'producer': 'Rockstar'},
# 'Fifa14': {'genre': 'Sports', 'release_date': '2013', 'producer': 'EA'},
# 'Borderlands': {'genre': 'Shooter', 'release_date': '2009', 'producer': 'Gearbox'},
# 'Skyrim': {'genre': 'RPG', 'release_date': '2011', 'producer': 'Bethesda'},
# 'Wall-E': {'genre': 'Platform', 'release_date': '2008', 'producer': 'THQ'}}

# ToDo

# Question 6 - Sorting Dictionary
# Write a function that returns a sorted list of (key, value) tuples. The list must be sorted by
# the value and be sorted largest to smallest.

# Examples Test Case 1:
# {3:1, 2:2, 1:3} -> [(1,3), (2,2), (3,1)]

# Example Test Case 2:
# {'a' :5, 'b' :10, 'c' :2, 'd' :3, 'e' :8} -> [('b',10), ('e',8), ('a',5), ('d',3), ('c',2)]

# ToDo

# Question 7 - Word Frequency
# Write a program that prompts the user for a sentence. Split the sentence into words and store
# the frequency of each word (number of occurrences). Then print the words in a sorted manner
# from most common to the least common. If there is a tie, print the word that comes first in
# the original sentence.
# Hint: You can use sorted(dict_, key=dict_.get) function to sort a dictionary according to the
# values. In order to get the reversed version of this, add reverse = True parameter.

# Example Test Case 1:
# "one two two three three three four four four four" -> "four three two one"

# Example Test Case 2:
# "fair is fair and" -> "fair is and"

# Example Test Case 3:
# "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
# ->
# "a woodchuck chuck How much wood would if could wood? "

# ToDo

# Question 8 - Anagrams
# Anagram is a word formed by rearranging the letters of a different word (heart, earth).
# Write a function that takes a word list and prints out all the anagrams in the word list.

# Example Test Case:
# ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"] -> ['percussion', 'supersonic', 'car', 'arc']

# ToDo

# Question 9 - Set Operations
# Write a function that takes two sets then prints union, intersection and
# difference operations between them.

# Example Test Case:
# A = {1, 2, 3, 4, 5, 6} B = {1, 1, 2, 7, 11}
# ->
# A ∪ B = {1, 2, 3, 4, 5, 6, 7, 11} A ∩ B = {1, 2} A / B = {3, 4, 5, 6} B / A = {11, 7}

# ToDo

# Question 10 - Eligible to graduate?
# You are given 2 sets one of which is the set of all courses that has to be taken to graduate
# from CmpE department. Other one is the courses that has been taken by a student so far.
# Write a function indicating whether student can graduate or not.

# Example Test Case
# {"CmpE150","CmpE160","CmpE220","CmpE250","CmpE260"}, {"Cmpe150"} -> Not Eligible

# ToDo

# Question 11 - How good friends can they be?
# People need to have common things to be friends. Let's say we have a set for every person
# consisting of the ID's of their personality traits. Two people can make as better friendship
# as the sum of their common personality trait IDs. Write a function that calculates the sum
# of common personality trait IDs.

# Example Test Case:
# {1,2,3,4,5} {4,5,6,7} -> 9

# ToDo

# Question 12 - Distinct
# A distinct string is a string whose all characters occurs only once.
# Write a function that takes a string as an argument and checks whether given string is
# distinct or not.

# Example Test Case 1:
# dwarf -> True

# Example Test Case 2:
# violate -> True

# Example Test Case 3:
# violation -> False

# ToDo
