# Write a computer program which is able to chat with the user at the most basic level like the one given below.
#
# Chatbot: Hi, I'm Cmpe 150 Chatbot, what is your name?
# User: Ahmet (Your name)
# Chatbot: Hi "Ahmet" , how old are you?
# User: 19
# Chatbot: Hmm, you are "19" years old. Older than me. How can I help you? What do you want to do?
# User: Writing some code
# Chatbot: Well, what you want is "Writing some code" , but I don't know much about it to be honest.
# Chatbot: Can't you request something easier?
# User: Then tell a little bit about yourself
# Chatbot: My code was written by "Ahmet" a few minutes ago, and I'm always ready to chat. See you.

print("Hi, I'm Cmpe 150 Chatbot, what is your name?")
username = input()
print("Hi", username, ", how old are you?")
user_age = input()
print("Hmm, you are", user_age, "years old. Older than me. How can I help you? What do you want to do?")
task = input()
print("Well, what you want is", task, ", but I don't know much about it to be honest.")
print("Can't you request something easier?")
easier_task = input()
print("My code was written by", username, "a few minutes ago, and I'm always ready to chat. See you.")
