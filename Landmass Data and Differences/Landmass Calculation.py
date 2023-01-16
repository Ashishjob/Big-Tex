import math

landmass = open('UpdatedLandmassDataFile.csv', 'r')

Texas = 695663

countryDict = {}


for lines in landmass:
    lines = lines.replace("ï»¿" , '')
    lines = lines.split(',')
    countryDict[lines[0]] = float(lines[1])

chosenCountry = input("Select country:")

if Texas > countryDict[chosenCountry]:
    sizeDifference = Texas / countryDict[chosenCountry]
    print("{:.2f} {} \bs would fit inside Texas".format(sizeDifference, chosenCountry))

elif countryDict[chosenCountry] > Texas:
    otherSizeDifference =  countryDict[chosenCountry] / Texas
    print("Texas would fit inside {} {:.2f} times".format(chosenCountry, otherSizeDifference))