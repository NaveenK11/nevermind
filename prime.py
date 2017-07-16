# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 20:35:16 2017

@author: naveen
"""
def prime_or_not():
     x=int(input("Enter a number: "))
     y=x-1

     while(y>1):
         if((x%y!=0)):
             print(x , "is not divisible by",  y)
        
         else:
             print(x, "is divisible by", y)
             print("Ooops!.....It is not a prime")
             break
         y=y-1
 
     if(y==1):
         print("Yay!...it is a prime")
         
prime_or_not()