import random as rnd

temperatures = []

for i in range(7):
    temperatures.append(rnd.randint(26, 40))

daysOfTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

goodDaysCount = 0
numOfEvenDays = 0

highestTemp = temperatures[0]
highestTempDay = None

lowestTemp = temperatures[0]
lowestTempDay = None

sumOfWeekTemp = 0

aboveAvg = []

for i in range(7):
    sumOfWeekTemp += temperatures[i]

    if temperatures[i] > highestTemp:
        highestTemp = temperatures[i]
        highestTempDay = daysOfTheWeek[i]

    if temperatures[i] < lowestTemp:
        lowestTemp = temperatures[i]
        lowestTempDay = daysOfTheWeek[i]

    if temperatures[i] % 2 == 0:
        numOfEvenDays += 1

    print(daysOfTheWeek[i], temperatures[i])

avgWeekTemp = sumOfWeekTemp / 7

for a in range(7):
    if temperatures[a] > avgWeekTemp:
        aboveAvg.append(daysOfTheWeek[a])

print("\nShelly has", numOfEvenDays, "even days.")
print("\nThe hottest temperature was", highestTemp, "on", highestTempDay)
print("The lowest temperature was", lowestTemp, "on", lowestTempDay)
print("\nThe average temprature was:",avgWeekTemp)
print("The days with above average tempratures were:",aboveAvg)

organizedTempList = []

for yay in range(6):
    currentLowestTemp = temperatures[0]
    for temp in temperatures:
        if temp < currentLowestTemp:
            currentLowestTemp = temp
    organizedTempList.append(currentLowestTemp)
    temperatures.remove(currentLowestTemp)       

print(organizedTempList)