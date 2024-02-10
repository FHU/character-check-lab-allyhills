#Remove pass and complete the code
def check_character(word, index):
   char = word[index]
   char_type = ''
   if char.isalpha():
      char_type = 'letter'
   elif char == ' ':
      char_type = 'white space'
   elif char.isdigit():
      char_type = 'digit' 
   else:
      char_type = 'unknown'
   
   return char_type

if __name__ == '__main__':
   check_character(word, index)
