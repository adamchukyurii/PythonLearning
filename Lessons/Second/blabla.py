from random import randint

# Lists

# some_string = "Hello, World"
# # copy_string = some_string[:]

# # print(some_string[::-1], copy_string)



# # count = 0

# # while count < 5:
# #    print(count)
# #    count += 1
# # Practice
# res = 0

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in num_list:
#    print(num**2)
#    res += num
   
# print(res)

# for char in some_string:
#    print(char)
   
# print(some_string[:5], some_string[5:])

# list_of_nums = list(range(1, 21))

# for num in list_of_nums:
#    if num % 3 == 0:
#       print(num)
   
# res = 0   
# count = 0   
# list_of_nums = list(range(1, 101))
# while count < len(list_of_nums):
#    res += list_of_nums[count]
#    count += 1
   
# print(res)

# while True:
#    usr_input = input("Enter here you number or if you want to quit type '0' 'exit': ")
#    if (usr_input == "exit" or int(usr_input) == 0):
#       break
#    else:
#       print(int(usr_input)**2)
      
# words = ["Hello", "bye", "one", "Hello", "one", "two", "bye"]
# acurrences = []

# for word in words:
#    if word not in acurrences:
#       acurrences.append(word)
# print(acurrences)

# # List Comperchensions
# # all() check if all is true all(not x % 2 for x in my_list[2, 4, 6,8, 22, 26, 27]) true true true true true true false - false
# # any() check if one of colecitons is true any(not x % 2 for x in my_list) true true true true true true false - true  
# my_list = [x for x in range(10) if x%2]
# print(my_list)

# # Matix

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# diagonal = [matrix[i][i] for i in range(len(matrix))]
# print(diagonal)


num_list1 = [randint(-10, 10) for _ in range(10)]
num_list2 = [randint(-10, 10) for _ in range(10)]
acurrences = []
print(num_list1, num_list2)
for i in range(10):
   if num_list1[i] in num_list2 and num_list1[i] not in acurrences:
      acurrences.append(num_list1[i])
print(f"There is numbers that the same in two lists - {acurrences}")

acurrences = []

for i in range(10):
   if num_list1[i] not in num_list2 and (num_list1[i] not in acurrences):
      acurrences.append(num_list1[i])
   if num_list2[i] not in num_list1 and (num_list2[i] not in acurrences):
      acurrences.append(num_list2[i])
print(f"There if numbers that not the same in two lists - {acurrences}")



# num_list2 = [2, -2, 4, -4, 8, -8]


# print(f"Does list have positive number - {any(x > 0 for x in num_list1)}")
# print(f"Does all numbers in list is even - {all(x % 2 == 0 for x in num_list2)}")

# if sum(num_list1) > sum(num_list2):
#    print("First list-sum is bigger")
# else:
#    print("Second list-sum is bigger")

# fizz buzz

# first_num = 2
# second_num = 3
# end = 11

# list = []

# for i in range(1, end + 1):
#    if i % first_num == 0 and i % second_num == 0:
#       list.append('FB')
#    elif i % first_num == 0:
#       list.append('F')
#    elif i % second_num == 0:
#       list.append("B")
#    else:
#       list.append(i)
# print(list)

