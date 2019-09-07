def binary_array_to_number(arr):
  # your code
  str_arr = []
  print(arr)
  for i in arr:
      str_arr.append(str(i))
  join_arr = ''.join(str_arr)
  print(join_arr)
  answer = int(join_arr, 2)
  print(answer)
  return answer
