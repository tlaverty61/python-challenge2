# import modules
import os
import csv

# join Budget Data file
csvFilePath = os.path.join("Resources", "budget_data.csv")

# declare variables
totalmo = 0
totalPL = 0
avgChange = 0
increaseDate = ""
increaseMax = 0
decreaseDate = ""
decreaseMax = 0
monthlyChange = 0


# open the Budget File
with open(csvFilePath, "r", encoding="utf-8") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)

    # find totals 
    for row in csvReader:
        # toal months
        totalmo += 1
        
    # calculate average change on PL
    for change in range(len(totalPL)-1):
        monthlyChange.append(totalPL [change+1]-totalPL[change])
    avg - sum(monthlyChange)/len(monthlyChange)



increaseMax = max(monthlyChange)
decreaseMax = min(monthlyChange)   

     

# save results to text file
with open(results, "w") as txt_file:

    results = (f"Financial Analysis \n"
               f"------------------------ \n"
               f"Total Months: {totalmo}\n\n"
               f"Total: {totalPL}\n\n"
               f"Average Change: {avgChange}\n\n"
               f"Greatest Increase in Profits: {increaseDate} ({increaseMax})\n"
               f"Greatest Decrease in Profits: {decreaseDate} ({decreaseMax})")
    print(results, end="")

    txt_file.write(results)

