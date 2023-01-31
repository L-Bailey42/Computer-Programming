#Task 1
print("Hello, World")


#Task 2
print("\nHello, Luke")


#Task 3
cTemp = 38.4
fTemp = (cTemp*(9/5)) + 32
print("\nTemperature in Yorkshire")
print("Celsius: ",cTemp)
print("Farenheit: ",fTemp)


#Task 4
matches = 609
totalInnings = 1014
notOut = 162
totalRuns = 48426
battingAverage = (48426/(1014-162))
print("\nBatting Average: ",battingAverage,"\n")

#Task 5
labSize = 24
studentNum = [113,175,12]
for count in range (0,len(studentNum)):
    groupNum = int(studentNum[count]) // labSize
    extraStudent = int(studentNum[count]) % labSize
    print("There will be ",groupNum," full group(s), and ",extraStudent," extra student(s) in a smaller group")
