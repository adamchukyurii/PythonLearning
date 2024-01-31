# 1
all_inputs = []

# while True:
#    user_input = input("Enter here your number, if you want to quit type '0': ")
#    if  int(user_input) == 0:
#       res = sum(all_inputs)
#       print(f"There is a sum of all typed numbers: {res}")
#       break
#    else:
#       all_inputs.append(int(user_input))   
#       print(all_inputs)

# 2

# while True:
#    user_input = input("Enter here your number, if you want to quit type '0': ")
#    if  int(user_input) == 0:
#       res = sum(all_inputs) / len(all_inputs)
#       print(f"There is a middle value of all numbers: {res}")
#       break
#    else:
#       all_inputs.append(int(user_input))   
#       print(all_inputs)
      
# 3

# while True:
#    if sum(all_inputs) >= 100:
#       res = sum(all_inputs)
#       print(f"The sum of entered numbers is - {res}, and its more than 100, so get a fuck out here")
#       break
#    else:
#       user_input = input("Enter here your number: ")
#       all_inputs.append(int(user_input))   
#       print(all_inputs)

#4

# user_input = input("Enter here your sentence: ").split(" ")
# print(f"The amount of words in this sentence is {len(user_input)}")

#5

user_input = int(input("Enter here how big you want a diamond with odd numbers: "))

if not user_input % 2 == 0:
   for i in range(1, user_input + 1, 2):
      spaces_in_row = user_input - i
      left_spaces = right_spaces = int(spaces_in_row / 2)
      for j in range(left_spaces):
         print(" ", end="")
      for k in range(i):
         print("*", end="")
      for l in range(right_spaces):
         print(" ", end="")
      print()
   for i in range(user_input - 2, 0, -2):
      spaces_in_row = user_input - i
      left_spaces = right_spaces = int(spaces_in_row / 2)
      for j in range(left_spaces):
         print(" ", end="")
      for k in range(i):
         print("*", end="")
      for l in range(right_spaces):
         print(" ", end="")
      print()