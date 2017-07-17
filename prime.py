#!/usr/bin/python
# -*- coding: utf-8 -*-

def prime_or_not():
     x = int(input("Enter a number: "))   # input a number
     y = x-(x-2)                          # subtract  because we know that the number is divisible by itself and one

     while(y < x):                        # initiate while loop, since the numder is divisible by itself,skip it
         if(x % y!= 0):                   # checks if x is not divisible by y and returns the following
             print(x , "is not divisible by",  y)
        
         else:
             print(x, "is divisible by", y)  # else if divisible it breaks the loop
             print("Ooops!.....It is not a prime")
             break
         y = y+1
 
         if(y==x):                            #finally, if the looped y equals x then its proved that 
             print("Yay!...it is a prime")    #it has not been divisible by any other number

def __name__ == "__main__":
     prime_or_not()
