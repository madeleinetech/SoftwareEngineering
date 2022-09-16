#Madeleine Brown - Assessment project1
import yfinance as yf
from sense_emu import SenseHat
import csv
import random
from stocksymbol import StockSymbol
import pandas as pd
#sense hat class
s = SenseHat()
#api-key
apiKey = "34e8cda3-3cd5-489a-8aac-0bf124d418fc"
#menu function
ss = StockSymbol(apiKey)
def menu():
    #menu
    print("Welcome to Stock Ticker!")
    print()
    print("1. DJIA")
    print("2. NASDAQ")
    print("3. NYSE")
    #user choice input
    userChoice = input("Please choose a Stock Library: ")
    print()
    # if the user chooses a valid choice
    if userChoice == "1" or userChoice == "2" or userChoice == "3":
        #if the user chooses dow jones
        if userChoice == "1":
            library = ss.get_symbol_list(index="DJI")
        #if the user chooses NASDAQ
        elif userChoice == "2":
            library = ss.get_symbol_list(index="NDX")
        #if the user chooses NYSE
        else:
            library = ss.get_symbol_list(index="XMI")
        #services menu
        print("Services: ")
        print("1. Search by symbol")
        print("2. Display a random symbol")
        print("3. Display all symbols")
        #user service choice
        userOption = input("Please choose an option: ")
        #if the user choice is valid
        if userOption == "1" or userOption == "2" or userOption == "3":
            #if the user chooses to search by symbol
            if userOption == "1":
                bySymbol(library)
            #if the user chooses to display random
            elif userOption == "2":
                byRandom(library)
            #if the user chooses to display all
            else:
                displayAll(library)
        #if the user choice is not valid
        else:
            print("Try again.")
            #start over
            menu()
    #if the user choice is not valid
    else:
        print("Try again.")
        #start over
        menu()
#search by symbol function
def bySymbol(library):
    #creating list of just the symbols
    libraryList = [line["symbol"] for line in library]
    #user stock name input
    userStock = input("Enter the name of the stock: ")
    #if the stock exists in the library
    if userStock in libraryList:
        #display the stock
        displayStock(userStock)
    #if stock is not valid
    else:
        print("This Company does not exist within the chosen Stock Library.")
        #start over
        menu()
#random stock function
def byRandom(library):
    #create a list of just symbols
    libraryList = [line["symbol"] for line in library]
    #grab a random symbol from the list of stocks
    randStock = libraryList[random.randint(0,len(libraryList)-1)]
    #display that symbol
    displayStock(randStock)
#display all stocks function
def displayAll(library):
    #create a list with just the symbols
    libraryList = [line["symbol"] for line in library]
    #for all symbols in the list
    for symbol in libraryList:
        #display the symbol
        displayStock(symbol)
#display stock function
def displayStock(stock):
    #grabbing the new price
    marketPrice = yf.Ticker(stock).info["regularMarketPrice"]
    #grabbing the previous price
    previousClosePrice = yf.Ticker(stock).info["regularMarketPreviousClose"]
    #calculating actual change
    actualChange = marketPrice - previousClosePrice
    #calculating percent change
    percentChange = (actualChange / previousClosePrice) * 100
    #display symbol on sense hat
    s.show_message(stock)
    #display new price on sense hat
    s.show_message("{:.2f}".format(marketPrice))
    #if the actual change is negative
    if actualChange > 0:
        #display a + in from of actual and percent change
        s.show_message("+{:.2f}".format(actualChange))
        s.show_message("+{:.2f}".format(percentChange))
    #if the change is less than or 0
    elif actualChange <= 0:
        #display the actual and percent change as is
        s.show_message("{:.2f}".format(actualChange))
        s.show_message("{:.2f}".format(percentChange))
    #display previous price
    s.show_message("{:.2f}".format(previousClosePrice))
#calling menu
menu()
