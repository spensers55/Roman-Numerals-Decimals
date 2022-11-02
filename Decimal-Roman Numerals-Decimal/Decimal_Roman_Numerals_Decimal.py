# this program will convert Roman Numerals to Decimal and Decimal to Roman Numerals
# RN2Dec - It will start counting from the end of the string of RN and add all numbers of equal or greater value
#   it will subtract any numbers of lesser value
# Dec2RN - it will divide the decimal by the highest level of precision to determine the number of characters must be placed
#   it will repeat this with all levels of precision
#   it will refine this numeral by injecting subtractive case where needed (i.e. IIII to IV)
import tkinter
import math

mainScene = tkinter.Tk() #UI created as global
decimalInput=tkinter.IntVar(mainScene) #UI element created as global
romanNumeralInput=tkinter.StringVar(mainScene) #UI element created as global

#Roman Numeral to Decimal
#Accepts romanNumeral: a string containing a roman numeral input by the user
#Returns finalValue: a variable containing a decimal number converted by this function
#Other Returns currentVal: passes forward an error message to the calling function
def rnToDec(romanNumeral): # Roman Numeral to Decimal
    currentLoc=len(romanNumeral)-1 # iterating thru the string starting at the end
    currentVal=0 # the value of the character at currentLoc
    previousVal=0 # the value of the largest previous character
    finalValue = 0 # the result: the decimal number that matches the roman numeral

    while currentLoc != -1: # until checked the whole string
        currentVal = getValOfChar(romanNumeral[currentLoc]) # function call to get numeric value

        if currentVal == romanNumeral[currentLoc]: # if it doesn't have a numerical value
            return romanNumeral[currentLoc] + " is an invalid character" # send problem forward

        if currentVal >= previousVal: # if current value is larger than previous,...
            previousVal=currentVal # match previous to new largest
            finalValue += currentVal # add new value to result

        if currentVal < previousVal: # if current value is less than previous,...
            finalValue-=currentVal # subtract it off (it is a subtractive)

        currentLoc-=1 # decrement iterator
    #end while loop
    return romanNumeral + " is " + str(finalValue) + " in decimal"
# end of function

#Get value of character
#Accepts char: a variable containing 1 character (I, V, X, L, C, D, or M)
#Returns static value: the numeric value associated with the character entered
#Default Returns char: the character entered is returned as an error message
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

# Decimal to Roman Numeral
# Accepts decimal: a number in base 10 format entered by the user
# Returns numeral: a number in roman numeral format converted by the function
# Uses: math class
def decToRN(decimal):
    originalVal = decimal
    thousands = math.floor(decimal/1000) #use division to find quantity of 1000's
    decimal %= 1000 #use modulus division to remove 1000's level of precision

    fhundreds = math.floor(decimal/500) #find if a 500 exists (there can only be 1)
    decimal %= 500 # remove 500

    ohundreds = math.floor(decimal/100) # detect 100's
    decimal %= 100 #remove 100's

    fifty = math.floor(decimal/50) #detect a 50
    decimal %= 50 #remove 50

    tens = math.floor(decimal/10) #detect 10's
    decimal %= 10 #remove 10's

    five = math.floor(decimal/5) #detect a 5
    decimal %= 5 # remove a 5

    #use string multiplication to generate rough roman numeral
    numeral = (thousands*"M") + (fhundreds*"D") + (ohundreds*"C") + (fifty*"L") + (tens*"X") + (five*"V") + (decimal*"I")
    #refine roman numeral (include subtractives, IV instead of IIII):
    #detect if there are more than 4 of the following in a row
    #C's
    repeatFound = numeral.find("CCCC") #begin post processing on rough numeral by checking for unsubtractive digits in the 100's
    if repeatFound != -1:
        numeral = numeral.replace("DCCCC", "CM") #replace with subtractive digits (starting with 900, then 400)
        numeral = numeral.replace("CCCC", "CD")
    #X's
    repeatFound = numeral.find("XXXX") #post processing part 2: unsubtractive digits in 10's
    if repeatFound != -1:
        numeral = numeral.replace("LXXXX", "XC") #replace with subtractives (starting with 90, then 40)
        numeral = numeral.replace("XXXX", "XL")
    #I's
    repeatFound = numeral.find("IIII") #finish post processing with unsubtractive digits in the 1's
    if repeatFound != -1:
        numeral = numeral.replace("VIIII", "IX") #replace with unsubtractives (starting with 9, then 4)
        numeral = numeral.replace("IIII", "IV")
    return str(originalVal) + " is " + numeral + " in Roman Numerals" #return output string
#end of function

def toRNControl():
    popup=tkinter.Tk() #create tkinter window
    global decimalInput #load global variable
    try:
        input=decimalInput.get() #fish for exceptions to validate input
    except:
        tkinter.Label(popup, text=("Please Enter a valid number")).grid(row=0,column=0) #the window if exception is thrown
        tkinter.Button(popup,text="Ok",command=lambda:quitButton(popup)).grid(row=1,column=0)
        return
    
    tkinter.Label(popup, text=(str(decToRN(input)))).grid(row=0,column=0) #the window if exception is not thrown
    tkinter.Button(popup,text="Ok",command=lambda:quitButton(popup)).grid(row=1,column=0)
    if input>3999: #disclaimer about number size
        tkinter.Label(popup, text="Your number is larger than standard Roman Numerals can display. It may have a lot of M's.").grid(row=2,column=0)
#end of function

def toDecControl():
    global romanNumeralInput #load global variable
    input=romanNumeralInput.get()
    popup=tkinter.Tk() #create tkinter window
    tkinter.Label(popup, text=(str(rnToDec(input)))).grid(row=0,column=0) #populate window
    tkinter.Button(popup,text="Ok",command=lambda:quitButton(popup)).grid(row=1,column=0)
#end of function

def quitButton(window): # pass in a scene to close
    window.destroy() # close passed in scene

def main(): # main driver, contains UI logic
    global mainScene
    global decimalInput
    global romanNumeralInput
    mainScene.title("Decimal-Roman Numeral Converter")
    tkinter.Label(mainScene, text="Enter Numbers Below").grid(row=0,column=0)
    tkinter.Label(mainScene, text="Put Decimal here").grid(row=1,column=0)
    tkinter.Label(mainScene, text="Put Roman Numeral here").grid(row=1,column=1)
    tkinter.Entry(mainScene, textvariable = decimalInput).grid(row=2,column=0)
    tkinter.Entry(mainScene, textvariable = romanNumeralInput).grid(row=2,column=1)
    tkinter.Button(mainScene, text="Convert to Roman Numeral",command=lambda:toRNControl()).grid(row=3,column=0)
    tkinter.Button(mainScene, text="Convert to Decimal",command=lambda:toDecControl()).grid(row=3,column=1)
    tkinter.Button(mainScene, text="Quit",command=lambda:quitButton(mainScene)).grid(row=4,column=0)
    mainScene.mainloop()
# end of function

main()