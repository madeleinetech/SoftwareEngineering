# Starr Holmes
#September 11, 2022
#Stock Ticker- Project #1
# import sense hat emulator

#import yfinance
import yfinance as yf
#import sense hat
from sense_emu import SenseHat
#from time import sleep
import pandas as pd
#import stocksymbol to access API
from stocksymbol import StockSymbol
api_key = '7c398cb5-ff04-4c2e-99f5-08c8f11b0aab'
ss = StockSymbol(api_key)
import random

# symbol_list_spx = ss.get_symbol_list(index="NYA")
# print(symbol_list_spx)
# index_list = ss.index_list
# print(index_list)

# print menu
def main():
    print("Enter 1: Select DJIA Index")
    print("Enter 2: Select NASDAQ Index")
    print("Enter 3: Select NYSE Index")
    #ask for user input selection
    userMenuSel = int(input("What is your selection: "))
    #if user selects 1 go to DJIA index
    if userMenuSel == 1:
        DJIA_Index()
    #if user selects 2 go to NASDAQ index
    elif userMenuSel == 2:
        NASDAQ_Index()
    #if user selects 3 go to NYSE index
    elif userMenuSel == 3:
        NYSE_Index()
    #if user does not select a number within menu print not valid selection
    else:
        print("Not a valid selection")

#DJIA index function
def DJIA_Index():
    #print menu
    print(" ")
    print("Welcome to the Dow Jones Industrial Average Index")
    print(" ")
    print("Enter 1: To Search by symbol")
    print("Enter 2: To Display Random Symbol")
    print("Enter 3: Display all symbols")
    #ask for user input for selection in menu
    choice = int(input("What is your selection in the DJIA Index: "))
    print('')

    #DJI index dictionary
    symbol_list_DJI = ss.get_symbol_list(index="DJI")

    #create an empty list
    DJI_list = []
    #append items with key 'symbol' to empty list
    for i in symbol_list_DJI:
        DJI_list.append(i['symbol'])

    #if user selects 1
    if choice == 1:
        #ask for input and assign user input to my_symbol
        my_symbol = input("Search a symbol:")
        #convert user input to upper case
        my_symbol = my_symbol.upper()

        #if the symbol the user selects is in the DOW30 list go to the function searchBySymbol
        if my_symbol in DJI_list:
            #print("Your selected symbol is: ", my_symbol, "and is in the DJI index...loading more information")
            searchBySymbol(my_symbol)

        else:
            print("")

    #if user selects 2 within the DOW30 Index
    elif choice == 2:
        #random.choice selects a random item within DJI_list
        rand = random.choice(DJI_list)
        #call the function searchyBySymbol to search the random item stock information
        searchBySymbol(rand)

    #if user selects 3
    elif choice == 3:
        #go through the DOW30 list and searchyBySymbol printing out the contents of stock information
        for i in DJI_list:
            searchBySymbol(i)
            print("")


#function for NASDAQA index
def NASDAQ_Index():
    #print menu
    print(" ")
    print("Welcome to the National Association of Securities Dealers Automated Quotations Index")
    print(" ")
    print("Enter 1: To Search by symbol")
    print("Enter 2: To Display Random Symbol")
    print("Enter 3: Display all symbols")
    #ask user for selection
    choice = int(input("What is your selection in the NASDAQ Index: "))
    print(" ")

    #original dictionary
    symbol_list_NASDAQ = ss.get_symbol_list(index="NDX")
    #create an empty list
    NASDAQ_list = []
    #append items with key 'symbol' to empty list
    for i in symbol_list_NASDAQ:
        NASDAQ_list.append(i['symbol'])

    #if user selects 1
    if choice == 1:
        #ask them for a symbol within the NASDAQ index
        my_symbol = input("Search a symbol:")
        #uppercase users symbol
        my_symbol = my_symbol.upper()

        #if users symbol is in the NASDAQ list
        if my_symbol in NASDAQ_list:
            #print("Your selected symbol is: ", my_symbol, "and is in the NASDAQ index...loading more information")
            print("")
            #go to function searchBySymbol to print stock information contents
            searchBySymbol(my_symbol)

        else:
            print("Your selected symbol IS NOT in the NASDAQ index")

    #if user selects 2
    elif choice == 2:
        #store random choice from NASDAQ_list in variable rand
        rand = random.choice(NASDAQ_list)
        #pass rand to searchBySymbol to print stock information contents
        searchBySymbol(rand)

    #if user selects 3
    elif choice == 3:
        #for each item in the NASDAQ_list go to function searchBySymbol to print its stock information contents
        for i in NASDAQ_list:
            searchBySymbol(i)
            print("")

    else:
        print("You did not select an accepted option")

#function for New York Stock Exchange
def NYSE_Index():
    #print menu
    print(" ")
    print("Welcome to the NYSE Index")
    print(" ")
    print("Enter 1: To Search by symbol")
    print("Enter 2: To Display Random Symbol")
    print("Enter 3: Display all symbols")
    #ask user for selection
    choice = int(input("What is your selection in the NYSE Index: "))
    print(" ")

    #NYSE index dictionary
    symbol_list_NYSE = ss.get_symbol_list(index="XMI")
    #create an empty list
    NYSE_list = []

    #append items in dictionary with key 'symbol' to NYSE_list
    for i in symbol_list_NYSE:
        NYSE_list.append(i['symbol'])

    #if user selects 1
    if choice == 1:
        #ask user for symbol
        my_symbol = input("Search a symbol:")
        #uppercase user symbol
        my_symbol = my_symbol.upper()
        #pass symbol to searchBySymbol function to print stock info
        searchBySymbol(my_symbol)

    #if user selects 2
    elif choice == 2:
        #select a random item in NYSE_list and assign to the variable rand
        rand = random.choice(NYSE_list)
        #pass rand to searchBySymbol to print stock info for rand
        searchBySymbol(rand)

    #if user selects 3
    elif choice == 3:
        #for each item in NYSE_list go to function searchBySymbol to print stock info
        for i in NYSE_list:
            searchBySymbol(i)
            print("")
    else:
        print("You did not select an accepted option")


################################

#function for searchBySymbol submenu option
def searchBySymbol(user):
    #create a object for senseHat function
    sense=SenseHat()
    #create variables for colors
    red = [255, 0, 0]
    blue = [0, 0, 255]
    yellow = [255, 255, 0]

    #pass symbol to ticker function to gather information
    answer = yf.Ticker(user)
    #get symbol and display it to raspberry pi
    sense.show_message("Symbol: ", answer.info['symbol'])
    # store opening price in the variable theopen
    theopen = answer.info['open']
    # format for two decimal places and display to raspberry pi
    sense.show_message("  Open: {:.2f}".format(theopen))
    #get previous close value
    thePreClose = answer.info['previousClose']
    #display on raspberry pi
    sense.show_message("   Previous Close: {:.2f}".format(thePreClose))
    #get regular market price value
    reg = float(answer.info['regularMarketPrice'])
    #get previous close value
    pre = float(answer.info['previousClose'])

    # calculate actual change, previousClose - regularMarketPrice
    actCh = pre - reg

    #if actual Change is greater than 1 change it is positive so add "+"
    # display on raspberry pi
    if actCh > 0:
        sense.show_message("  Actual Change: + {:.2f}".format(actCh))

    #if actual Change is less than 1 the ticker will already assign a "-" in front of value
    #display on raspberry pi
    else:
        sense.show_message("  Actual Change:  {:.2f}".format(actCh))

    # percent change calculation
    perctchg = ((actCh / (abs(reg))) * 100)

    # if percent Change is greater than 0 change it is positive so add "+"
    # display on raspberry pi
    if perctchg > 0:
        sense.show_message("  Percentage Change: + {:.2f}".format(perctchg), "%")

    # if percent Change is less than 0 the ticker will already assign a "-" in front of value
    # display on raspberry pi
    else:
        sense.show_message("  Percentage Change:  {:.2f}".format(perctchg), "%")


#call main function
main()
