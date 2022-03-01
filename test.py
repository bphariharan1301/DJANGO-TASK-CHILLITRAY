from email import charset

from random import randrange
import string


email = ''
def oneFunction():
    global email
    word=randrange(20, 50, 3)
    email = word
    print('email is : ', email)

def anotherFunction():
    for letter in get_word():              
          print("_",end=" ")

def get_word():
      print('EMAIL TAKEN FROM ONE FUNCTION IS ', email)

oneFunction()

get_word()