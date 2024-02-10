# variables types and conditions 

# fullname = name + " " + lastname
# fullname = "{} {}".format(name, lastname)
# fullname = "{lastname} {name}".format(name=name, lastname=lastname);
# fullname = f"{name} {lastname}"
# Practice

# fullname = f"You are {input("Enter your Name: ")} {input("Enter your last name: ")}, and you are {int(input("Enter your age: ")) + 5} old"
# print(fullname)

# user_radius = int(input("Enter here your radius: "))
# print(f"The square of circle is {math.pi * user_radius**2}")

# user_age = int(input("Enter here your age: "))
# user_name = input("Enter here your name: ")


# flag = True if 'a' in user_name.lower() else False

# if (flag):
#    print("Poshel od suda")
#    exit()
# else:
#    print("You have passed")

# if (user_age < 18):
#    print("Poshel od suda shkolota")
# elif (user_age > 100):
#    print("Ce kidalovo")
# else:
#    print("You are welcome")
   
# print("Even" if user_age % 2 == 0 else "Odd")
   
# if (user_age % 2 == 0 and ('v' in user_name) or ('V' in user_name)):
#    print("You have won a prize")
   
user_name = input("Enter here your name: ")
user_age = int(input("Enter here your age"))
user_sex = input("Enter here your gender in format male or female: ")

if 'c' not in user_name.lower() or 't' not in user_name.lower():
   if user_age < 15 :
      print("You can play tenis")
   else:
      if user_sex == "male":
         print("You can play football")
      elif user_sex == "female":
         print("You can play basketball")
else:
   print("You have not passed")