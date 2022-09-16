import yfinance as yf
from sense_emu import SenseHat
import csv
s = SenseHat()
NASDAQf = open("NASDAQ.txt", "r")
DowJonesf = open("DowJones.txt", "r")
NYSEf = open("NYSE.txt", "r")

print("Welcome to Stock Ticker!")
print()
print("1. DJIA")
print("2. NASDAQ")
print("3. NYSE")
userChoice = input("Please choose a Stock Library: ")
if userChoice == "1" or userChoice == "2" or userChoice == "3":
    print("Please choose an Option")
    print("1. Search by symbol")
    print("2. Display a random symbol")
    print("3. Display all symbols")
    secondChoice = input()
    if secondChoice == "1":
        if userChoice == "1":
            reader = csv.reader(DowJonesf)
            DowJones = [line[0] for line in reader]
            userStock = input("Enter the name of the stock: ")
            if userStock in DowJones:
                stockInfoPrice = yf.Ticker(userStock).info["regularMarketPrice"]
                stockInfoPreClosePrice = yf.Ticker(userStock).info["regularMarketPreviousClose"]
                s.show_message(stockInfoPreClosePrice)
                #print(stockInfoPreClosePrice)
                #print(stockInfoPrice)
            else:
                print("This Company does not exist within the Dow Jones Stock Library.")
