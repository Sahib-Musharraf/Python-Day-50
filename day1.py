# -*- coding: utf-8 -*-
"""Day1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c-pZYVWQIv5ou77pXl75NqxsAa_Q-Dyh
"""

# Write the python code to add two number

A = 34
B = 80

if A>B:
  print("A is greater")
else:
  print("B is greater")

  print(type(A))

num1 = int(input("the first number is "))
num2 = int(input("the second number is "))

sum = num1 + num2

print("The sum of",num1,"and",num2,"is",sum)

# Write the python code when A number is devided by z

A = int(input("enter the number A :"))
Z= int(input("enter the diviser Z :"))

remainder= A % Z

print("the remainder when",A,"is","is devided by",Z,"is", remainder)