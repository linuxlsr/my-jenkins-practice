#!/usr/bin/python
import sys
from pprint import pprint
pprint(sys.argv)

stringParameter = sys.argv[1]
firstNumber = sys.argv[2]
secondNumber = sys.argv[3]
thisSum = ''

print("this is a test of the python script build")
print(stringParameter)
print("The first number is " + firstNumber)
print("The second number is " + secondNumber)
thisSum = firstNumber + secondNumber
print("the sum of " + firstNumber + "and " + secondNumber + " is " + thisSum)
print("That is all, Happy New Year!")