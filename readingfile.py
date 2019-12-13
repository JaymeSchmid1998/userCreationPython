from pathlib import *
# coding: utf-8
my_file=Path('UserCreation.txt')
mylines = []
# this checks if the file exists
if my_file.exists():
#if it does hthen open it and append the lines to the array
    objText = open('UserCreation.txt', "r")
    for line in objText:
        mylines.append(line)

    
  #  lstLines = objText.readlines()
   # print (lstLines)
    mytext=mylines[0].rstrip('AuthCode:')
    print(mytext)
#this just gets the raw code =, it doesth is by replacing the text auth code with nothing    

    mytext1 = mytext.replace("AuthCode: ", "")

    print(mytext1)
    
    objText.close()
    print('file found')
else:
    print('no file found')
