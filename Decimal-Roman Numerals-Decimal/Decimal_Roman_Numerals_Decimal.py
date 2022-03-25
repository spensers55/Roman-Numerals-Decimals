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

def toNearest(val, nearest):
    valCalc = val # create calculcation version of val
    nearestVal = 0 # create return value for nearest

    negative = False # negative checking to determine if we need to add or subtract
    if val < 0:
        negative = True
        valCalc*=-1

    if nearest == 1000: # if searching for nearest 1000, execute
        while valCalc >= 900: # below 900, rn uses 500 value
            nearestVal+=1000
            valCalc -= 1000
        print(valCalc)
    # end nearest 1000
    elif nearest == 500: # if searching for nearest 500
        while valCalc >= 400 and not negative: # below 400, rn uses 100 value
            nearestVal += 500
            valCalc -=500
        print(valCalc)
    # end nearest 500
    elif nearest == 100: # if searching for 100
        while valCalc >= 90 or (negative and valCalc >= 40): # below 90, rn uses 50 value
            nearestVal += 100
            valCalc -=100
        print(valCalc)
    # end nearest 100
    elif nearest == 50 and not negative: # if searching for nearest 50
        while valCalc >= 40: # below 40, rn uses 10 value
            nearestVal += 50
            valCalc -=50
        print(valCalc)
    # end nearest 50
    elif nearest == 10 or (negative and valCalc >= 4): # if searching for nearest 10
        while valCalc >= 9: # below 9, rn uses 5 value
            nearestVal += 10
            valCalc -=10
        print(valCalc)
    # end nearest 10
    elif nearest == 5: # if searching for nearest 5
        while valCalc >= 4: # below 4, rn uses 1 value
            nearestVal += 5
            valCalc -=5
        print(valCalc)
    if negative:
        return (nearestVal*-1)
    else:
        return nearestVal
# end of function

def decToRN(decimal): # Decimal to Roman Numeral [STUB]
    RomanNumeral=""
    nearest = toNearest(decimal, 1000)
    while nearest != 0:
        nearest -= 1000
        decimal -= 1000
        RomanNumeral += "M"
    # end of 1000 while loop

    nearest = toNearest(decimal, 500)
    while nearest != 0:
        if nearest > 0:
            nearest -= 500
            decimal -= 500
            RomanNumeral += "D"
        else:
            nearest += 500
            decimal += 500
            RomanNumeral = "D" + RomanNumeral
    # end of 500 while loop

    nearest = toNearest(decimal, 100)
    while nearest != 0:
        if nearest > 0:
            nearest -= 100
            decimal -= 100
            RomanNumeral += "C"
        else:
            nearest += 100
            decimal += 100
            RomanNumeral = "C" + RomanNumeral
    # end of 100 while loop

    nearest = toNearest(decimal, 50)
    while nearest != 0:
        if nearest > 0:
            nearest -= 50
            decimal -= 50
            RomanNumeral += "L"
        else:
            nearest += 50
            decimal += 50
            RomanNumeral = "L" + RomanNumeral
    # end of 50 while loop

    nearest = toNearest(decimal, 10)
    while nearest != 0:
        if nearest > 0:
            nearest -= 10
            decimal -= 10
            RomanNumeral += "X"
        else:
            nearest += 10
            decimal += 10
            RomanNumeral = "X" + RomanNumeral
    # end of 10 while loop

    nearest = toNearest(decimal, 5)
    while nearest != 0:
        if nearest > 0:
            nearest -= 5
            decimal -= 5
            RomanNumeral += "V"
        else:
            nearest += 5
            decimal += 5
            RomanNumeral = "V" + RomanNumeral
    # end of 5 while loop

    while decimal != 0:
        if decimal > 0:
            decimal -= 1
            RomanNumeral += "I"
        else:
            decimal += 1
            RomanNumeral = "I" + RomanNumeral
    return RomanNumeral
# end of function

def UI(): # UI logic [STUB]
    mainScene = tkinter.tk()
    # UI Elements go here
    mainScene.mainloop()
    pass
#end of function

def main(): # main driver [testing STUB]
    dec = int(input("Enter Decimal number: "))
    print("That is {0} in Roman Numerals.".format(decToRN(dec)))
# end of function

main()