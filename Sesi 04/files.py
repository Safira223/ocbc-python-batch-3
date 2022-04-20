#f = open('Hack8_Sample_Text.txt')
#file = open('Hack8_Sample_Text_Extras.txt')
#f.close()

#try:
   #f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
 #  f = open("Hack8_Sample_Text_Extras.txt", encoding = 'utf-8')
   # perform file operations
#except FileNotFoundError :
    #print('that file is note found')
#finally:
   # f.close()
   #print('already tried')

#with open("sample.txt",'w',encoding = 'utf-8') as f:
 #  f.write("my first file\n")
  # f.write("This file\n\n")
  # f.write("contains three lines\n")
   
f = open("sample.txt", 'r', encoding = 'utf-8')
# print(f.read(4))
# print(f.read(4))
# print(f.read())

# f.seek(0)   # bring file cursor to initial position
# for line in f:
#   print(line, end = '')

with open('sample.txt', 'r') as reader:
     # Read & print the entire file
     print(reader.read())