# -*- coding: utf-8 -*-
# a function to call
def prime_or_not():
     x = int(input("Enter a number: "))   # input a number
     y = x-(x-2)                              # subtract with one because we know that the number is divisible by itself

     while(y < x):                        # initiate while loop, since the numder is divisible by 1,skip it
         if(x % y!= 0):                  # checks if x is not divisible by y and returns the following
             print(x , "is not divisible by",  y)
        
         else:
             print(x, "is divisible by", y)
             print("Ooops!.....It is not a prime")
             break
         y = y+1
 
         if(y==x):
             print("Yay!...it is a prime")
         
prime_or_not()
