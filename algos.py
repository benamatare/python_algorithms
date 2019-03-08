# Reverse a string
def reverse_string(input_string):
    return input_string[::-1], input_string

# Check if a string is a Palindrome or not
def check_palindrome(input_string):
  temp_base = input_string.lower().replace(' ', '')
  reversed_temp_base = temp_base[::-1]
  if temp_base == reversed_temp_base:
    return True
  else:
    return False
    
# Count # of characters in a string
def count_chars(input_string):
  store = {}
  for letter in input_string:
    if letter not in store:
      store[letter] = 1
    else:
      store[letter] += 1
  return store

def bubble_sort(arr, sorted = False):
  while not sorted:
    sorted = True
    for i in range(len(arr) - 1):
      if arr[i] > arr[i+1]:
        # if you're bigger than your neighbor, swap
        # you're not sorted, when the list is 'sorted' this if won't be triggered
        sorted = False
        arr[i], arr[i+1] = arr[i+1], arr[i]
