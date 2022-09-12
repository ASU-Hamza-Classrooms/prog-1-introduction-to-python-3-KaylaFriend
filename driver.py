#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    #Add code to call each of the functions and print the results
    print("Input string is %s" % (inputStr))
    print("Reverse of string is %s" % (reverseStr(inputStr)))
    print("Does string contain IT? %s" % containsWord(inputStr, "IT"))
    print("Does string contain apple? %s" % containsWord(inputStr, "apple"))
    print("Does string contain data? %s" % containsWord(inputStr, "data"))
    print("Is string a palindrome? %s" % isPalindrome(inputStr))
    print("Uppercase of string is %s" % upperCaseStr(inputStr))
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    #Use the object to call each of the methods in the Worker class
    #Print the result of each call
    obj = worker(inputStr)
    print("Input string is %s" % (inputStr))
    print("Reverse of string is %s" % obj.reverse())
    print("Does string contain IT? %s" % obj.containsStr("IT"))
    print("Does string contain apple? %s" % obj.containsStr("apple"))
    print("Does string contain data? %s" % obj.containsStr("data"))
    print("Is string a palindrome? %s" % obj.palindrome())
    print("Uppercase of string is %s" % obj.upperCase())

    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




