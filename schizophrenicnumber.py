# This is a program that prints out the first 1000 digits of a "schizophrenic number," also known as mock rational number.
# You can read about what this is here: https://en.wikipedia.org/wiki/Schizophrenic_number
# 
# Recursive Function : f(n) = 10 f(n - 1) + n
# Specify n as odd integers
# Take the square root of the function

from decimal import *
from math import sqrt

getcontext().prec = 10000

def recursive(n):
    if (n == 0):
        return 0
    return 10 * recursive(n - 1) + n

def schizophrenic(n):
    return Decimal.sqrt(recursive(n))

def formatString(string):
    formatted = ""
    repeatCount = 0
    repeating = 1
    for i in range(0, (len(string) - 1)):
        if string[i] == string[i+1]:
            repeatCount += 1
        
        if repeating == 1 and string[i] != string[i + 1] and string[i] != "." and string[i+1] != ".":
            if repeatCount > 4:
                formatted += string[i] + " "
                repeating *= -1
                repeatCount = 0
        elif repeating == -1 and string[i] == string[i+1] and string[i] != "." and string[i+1] != ".":
            if repeatCount > 4:
                formatted += "\n" + string[i]
                repeating *= -1
                repeatCount = 0
        else:
            formatted += string[i]

    return formatted

x = Decimal(input("Input an odd integer: "))
output = formatString(str(schizophrenic(x)))
print(output)