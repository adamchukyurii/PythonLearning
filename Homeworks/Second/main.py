def middle_three(string: str) -> list:
   middle = int(len(string) / 2 - 1)
   if len(string) <= 3:
      return string
   return string[middle - 1 : middle + 2]

# print(middle_three("sequencee"))

def even_indexed_element(numbers: list) -> list:
   return [numbers[i] for i in range(len(numbers)) if i % 2 == 0]

nums = [1, 2, 3, 4, 5]
print(even_indexed_element(nums))

def word_reverse(string: str) -> str:
   words = string.split()
   reversed_sentence = ''
   for word in words:
      reversed_sentence += word[::-1] + " "
   return reversed_sentence
print(word_reverse("Hello World"))

def second_smallest(numbers: list) -> int:
   smallest = min(numbers)
   
   second_smallest = min([num for num in numbers if num != smallest])
   return second_smallest
   
print(second_smallest(nums))

def remove_duplicate(numbers: list) -> list:
   res = []
   for num in numbers:
      if num not in res:
         res.append(num)
   return res

print(remove_duplicate(nums))

def rotate_list(numbers: list, index: int) -> list:
   mid_res = ()
   res = ()
   for i in range(index):
      mid_res += numbers[i],
   res += tuple(numbers[index:]) + mid_res
   return list(res)
print(rotate_list(nums, 2))

# def longest_palindromic_substring(srting: str) -> str:
   
def change_string(string: str) -> str:
   new_string = string[1 : -1]
   return string[-1] + new_string + string[0]

print(change_string("Hello"))

def remove_element(items: list, item) -> list:
   res = []
   for i in items:
      if i != item:
         res.append(i)
   return res

def is_palindrome(string: str) -> bool:
   lower_string = string.lower()
   
   left, right = 0, len(string) - 1
   
   while left < right:
      while not lower_string[left] and left < right:
         left += 1
      while not lower_string[right] and left < right:
         right -= 1
      if lower_string[left] != lower_string[right]:
         return False
      
      left += 1
      right -= 1
   return True

print(is_palindrome("Detartrated"))