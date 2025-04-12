def Add_many_number(numbers):
  sum = 0
  for num in numbers:
    sum += num
  return sum
numbers = [3,5,5,7,8,8]
Sum = Add_many_number(numbers)
print(Sum)