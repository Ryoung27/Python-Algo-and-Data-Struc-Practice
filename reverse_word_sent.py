def reverse_words(text):
  #go for it
  reverse_word_list = []
  li = list(text.split(" "))
  for i in li:
      i = i[::-1]
      reverse_word_list.append(i)
#   print(reverse_word_list)
  back_to_string = ' '.join(reverse_word_list)
  return(back_to_string)
