# this program will convert Roman Numerals to Decimal and Decimal to Roman Numerals
# RN2Dec - It will start counting from the end of the string of RN and add all numbers of equal or greater value
#   it will subtract any numbers of lesser value
# Dec2RN - it will start by taking the least precise value and associating it with a RN value
#   it will then subtract that value from the decimal number and ensure that level of precision is removed
#   if that level of precision persists, it will apply prefixes/suffixes as required
import tkinter

def rnToDec(romanNumeral): # Roman Numeral to Decimal
    currentLoc=len(romanNumeral)-1 # iterating thru the string starting at the end
    currentVal=0 # the value of the character at currentLoc
    previousVal=0 # the value of the largest previous character
    finalValue = 0 # the result: the decimal number that matches the roman numeral
    while currentLoc != -1: # until checked the whole string
        currentVal = getValOfChar(romanNumeral[currentLoc]) # function call to get numeric value
        if currentVal == romanNumeral[currentLoc]: # if it doesn't have a numerical value
            return currentVal # send problem forward
        if currentVal >= previousVal: # if current value is larger than previous,...
            previousVal=currentVal # match previous to new largest
            finalValue += currentVal # add new value to result
        if currentVal < previousVal: # if current value is less than previous,...
            finalValue-=currentVal # subtract it off (it is a prefix)
        currentLoc-=1 # decrement iterator
    return finalValue
# end of function

def getValOfChar(char): # used to convert roman numeral characters to decimal values
    if(char == 'I' or char == 'i'):
        return 1
    elif(char == 'V' or char == 'v'):
        return 5
    elif(char == 'X' or char == 'x'):
        return 10
    elif(char == 'L' or char == 'l'):
        return 50
    elif(char == 'C' or char == 'c'):
        return 100
    elif(char == 'D' or char == 'd'):
        return 500
    elif(char == 'M' or char == 'm'):
        return 1000
    else:
        return char
# end of function

def decToRN(): # Decimal to Roman Numeral [STUB]
    pass
# end of funciton

def UI(): # UI logic [STUB]
    mainScene = tkinter.tk()
    # UI Elements go here
    mainScene.mainloop()
    pass
#end of function

def main(): # main driver [testing STUB]
    rn = input("Enter Roman Numeral: ")
    print("That is {0} in decimal.".format(rnToDec(rn)))
# end of function

main()