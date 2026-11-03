#variables 
user_input = input("Guess a number: ")
print("user_input",user_input)

print(type(user_input))

user_input_int = int(user_input)
print(type(user_input_int))

my_var = 2 
print(id(user_input_int))
print(id(my_var))