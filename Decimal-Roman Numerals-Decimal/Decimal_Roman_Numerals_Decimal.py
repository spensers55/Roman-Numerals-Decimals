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

def toNearest(val, nearest): # -+-+- NOTE THIS PART OF THIS PROGRAM DOESN'T WORK YET. MORE PROGRESS SOON -+-+-
    tempCalc = val  # a temporary value to calculate how close we are without compromising the input value
    currentNearest = nearest    # a variable that keeps track of how many of 'nearest' magnitude we need
    negative = False
    if val < 0:
        negative = True
        tempCalc *= -1
    
    # acquire breakdown value of nearest input
    breakdown = 0 # breakdown value shows the unit this magnitude of roman numeral is built on
    if nearest > 100:   # for example, determining prefixes/suffixes of a RN containing 'M' or 'D' requires counting
                        # by 100s. Suffixes for values of this size require 100s to get as close as possible
        breakdown = 100
    elif nearest > 10:  # if the value is greater than 10, that means it is 100 or 50. that requires a bd of 10
        breakdown = 10
    else:               # if the value is greater than 1, that means it is 10 or 5. That requires a bd of 1
        breakdown = 1
    # end if/else
    
    while tempCalc > 0: # while loop to get into ball-park by subtracting numbers of 'nearest' magnitude. stops at 0
        currentNearest += nearest   # add numbers of 'nearest' magnitude to tracker
        tempCalc -= nearest # subtract from copy of input value

    if tempCalc == 0 or tempCalc > (breakdown * -1):   # if it matches or doesn't go below breakdown, instant return
        if negative:
            print("Nearest to {0} is {1}".format(val, currentNearest*-1))
            return currentNearest*-1
        else:
            print("Nearest to {0} is {1}".format(val, currentNearest))
            return currentNeaest
    else:   # if it's not within 1 breakdown of nearest, we went too far
        if negative:
            print("Nearest to {0} is {1}".format(val, (currentNearest-nearest)*-1))
            return (currentNearest - nearest)*-1
        else:
            print("Nearest to {0} is {1}".format(val, currentNearest-nearest))
            return currentNearest - nearest # return previous nearest

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