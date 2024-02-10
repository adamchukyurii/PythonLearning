# Functions recursions
import random
# def calc(num1:int, num2:int) -> int:
#    return num1 + num2


# # Changable num string giving copy
# # NotChangable list dict giving link
# # First named args than nonamed

# def foo(*args, **kwargs):
#    print(args, kwargs)

# def test(name, *args, age, **kwargs):
#    return f"Hello {name}, you are {args} old"

# # print(test("python", 45, True, name='Emily', age=45)

# def pow(num:int, exponent:int = 2):
#    return num ** exponent

# print(pow(25), pow(3, 3))

# first, second, *li = (1, 2, 3, 4, 5, 6, 7, 8)

# print(first, second, li)

# # anonim functions lambda - square = lambda x: x**2

# numbers = [1, 2, 3, 4, 5, 6]

# result = list(map(lambda x: x**2, numbers))
# print(result)

# # zip making one colection from another two

# def factorial(n):
#    if n == 0 or n == 1:
#       return 1
#    else:
#       print(n)
#       return n * factorial(n - 1)
   
# print(factorial(5))

# def quick_sort(numbers: int) -> list:
#    if (not numbers):
#       return []
#    if len(numbers) == 1:
#       return numbers 
#    base = numbers[0]
#    left = [num for num in numbers[1:] if num < base]
#    right = [num for num in numbers[1:] if num > base]
#    return quick_sort(left) + [base] + quick_sort(right)

# nums = [random.randint(1, 10000000) for _ in range(10000000)]
# print(quick_sort(nums))

def calc_sum(num1: int, num2: int) -> int:
   return num1 + num2

def calc_avarage(numbers: list) -> int:
   return sum(numbers) / len(numbers)

def fact(n: int) -> int:
   res = 1;
   for i in range(1, n + 1):
         res *= i
   return res

   
def filter_even(numbers: list) -> list:
   return filter(lambda x: x % 2 == 0, numbers)

def is_palindrome(string: str) -> str:
   return string[::-1]

def square(numbers: list) -> list:
   return list(map(lambda x: x ** 2, numbers))

def fibonaci(n: int) -> int:
   first = 0
   mid_res = 1
   res = [first]
   for i in range(1, n + 1 + res[-1], 1 if res[-1] < 1 else res[-1] + 1):
      mid_res = i
      print(mid_res)
      res.append(mid_res)
      print(res, res[-1])
   return res



def fibonaci_recurs(n: int) -> list:
   if n == 1:
      return [1]
   elif n == 2:
      return [1, 1]
   else:
      fib_list = fibonaci_recurs(n - 1)
      fib_list.append(fib_list[-1] + fib_list[-2])
      return fib_list

print(fibonaci(10))
# print(fibonaci_recurs(10))

# work_mode_with_file = input("Ener here what do you want to do with file")
# file_name = "example.txt"
# if work_mode_with_file == 'r':
#    with open(file_name, work_mode_with_file) as file:
#       for line in file:
#          print(line)
# elif work_mode_with_file == 'w':
#    with open(file_name, work_mode_with_file) as file:
#       user_text = input("Enter here sentence to write in file")
#       file.write(user_text)
# elif work_mode_with_file == 'a':
#    with open(file_name, work_mode_with_file) as file:
#       file