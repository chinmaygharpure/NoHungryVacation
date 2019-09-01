#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:18:02 2019

@author: yamnihcg
"""
def determineTicker(budget):
    budgetToInt = float(budget)
    if(budgetToInt <= 10):
        return '$'
    elif(budgetToInt > 10 and budgetToInt <= 30):
        return ['$', '$$']
    elif(budgetToInt > 30 and budgetToInt <= 60):
        return ['$', '$$', '$$$']
    else:
        return ['$', '$$', '$$$', '$$$$']
    
def timeStringToMilitaryTime(mealTime):

    mealTime = mealTime.replace(" ", "")

    timeOfDay = mealTime[-2] + mealTime[-1]
    timeOfDayToLowerCase = timeOfDay.lower()

    filteredStr = ''
    a = 1

    for i in range(len(mealTime)):
        try:
            int(mealTime[i])
            filteredStr = filteredStr + mealTime[i]
        except ValueError:
            a = 1
    if timeOfDayToLowerCase == 'pm' and (int(filteredStr) >= 100 and int(filteredStr) <= 1159):
        filteredStr = int(filteredStr)
        filteredStr = filteredStr + 1200
        filteredStr = str(filteredStr)
        return int(filteredStr)
        
    elif timeOfDayToLowerCase == 'am' and (int(filteredStr) >= 1200 and int(filteredStr) <= 1259):
        filteredStr = int(filteredStr)
        filteredStr = filteredStr - 1200
        filteredStr = str(filteredStr)
        filteredStr = '00' + filteredStr
        return int(filteredStr)
        
    elif timeOfDayToLowerCase == 'am' and (int(filteredStr) >= 100 and int(filteredStr) <= 959):
        filteredStr = '0' + filteredStr
        return int(filteredStr)
        
    else:
        return int(filteredStr)
    
def validTime(time, timeLowerBound, timeHigherBound):
    if(time >= timeLowerBound and time <= timeHigherBound):
        return True
    else: 
        return False

def removeDuplicates(duplicateRatingsArray): 
    finalList = [] 
    for num in duplicateRatingsArray: 
        if num not in finalList: 
            finalList.append(num) 
    return finalList

def getListOfWeekdayIndexes(startWeekday, endWeekday):
    weekdayArray = []
    if(startWeekday < endWeekday):
        for i in range(startWeekday, endWeekday + 1):
            weekdayArray.append(i)
    if(startWeekday > endWeekday):
        for j in range(startWeekday, 7):
            weekdayArray.append(j)
        for k in range(0, endWeekday + 1):
            weekdayArray.append(k)
    return weekdayArray

def returnAddressAndNameString(addressArray, name):
    tempAddress = ''
    tempAddress = tempAddress + "Name: " + name + " Address: "
    addressArrayLength = len(addressArray)
    for w in range(addressArrayLength):
        if(w != addressArrayLength - 1):
            tempAddress = tempAddress + addressArray[w] + ', '
        else: 
            tempAddress = tempAddress + addressArray[w]
    return tempAddress

def weekdayInformation(integerWeekday):
    if integerWeekday == 0:
        return "Monday"
    elif integerWeekday == 1:
        return "Tuesday"
    elif integerWeekday == 2: 
        return "Wednesday"
    elif integerWeekday == 3:
        return "Thursday"
    elif integerWeekday == 4:
        return "Friday"
    elif integerWeekday == 5:
        return "Saturday"
    else:
        return "Sunday"
    
def weekdayNames(numericalListOfWeekdays):
    namesArr = []
    for i in range(len(numericalListOfWeekdays)):
        namesArr.append(weekdayInformation(numericalListOfWeekdays[i]))
    return namesArr
        

