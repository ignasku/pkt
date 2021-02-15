#568 Just the Facts
#Ignas Ku
import math
import sys

class InOut():
        #method to read info from data.txt
        def readInfo(self):
                dataFile = open("data.txt", "r")
                numbers = []
                for number in dataFile:
                        numbers.append(int(number))
                return numbers

        #method to print data to result.txt
        def printAns(self, numbers, answer):
                result = open("result.txt", "w")
                for x in range(len(numbers)):
                        result.write(str(numbers[x]) + " -> " + answer[x] + "\n")
                result.close()



#numbers = base array
numbers = InOut().readInfo()

#method to find factorial of numbers[] array using math module
def factorial(number):
        return math.factorial(number)
    
#this method creates new array and finds factorial of 
#numbers array and converts to string array
def bigForCycle(numbers):
        factorial_array = [] 
        for number in numbers:                              
                factorial_array.append(str(factorial(number)))
        return factorial_array

#factorialsArray = converted factorial numbers to string array
factorialsArray = bigForCycle(numbers)

#simple split function to split string into chars
def split(string): 
    return [char for char in string]  

#function that scrolls through splitted char array and finds
#the first digit from reversed array and returns digit array
def digit(factorialsArray):
        answer = []
        for i in factorialsArray:
                #splitting and iterating reverse at the same time
                for j in reversed(split(i)):
                    if j != '0':
                            answer += j
                            break
        return answer

answer = digit(factorialsArray)
#printing answer
InOut().printAns(numbers, answer)