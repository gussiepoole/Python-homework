import os
import csv

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")
budget_data_csv_path ="//Users//gussiepoole//UBHM//PyBank//Resources//budget_data.csv"

#open and read csv

with open(budget_data_csv_path, 'r') as csv_file:
    csv_reader= csv.reader(csv_file)
    csv_header=next(csv_reader, None)


    new_list=[]
    new_profit=[]
    column={}
    change_list = []

    for h in csv_header:
        column[h]=[]



    for row in csv_reader:
        for h,e in zip(csv_header,row):
            column[h].append(e)
            
    
    new_list = column['Date']
    new_profit = column['Profit/Losses']

    print("Total Months: " + str(len(new_list)))

    int_profit = list(map(int, new_profit))
    print("Total: $" + str(sum(int_profit)))

    profit_total = sum(list(int_profit))
    profit_num = (sum(int_profit))

    prev_profit = new_profit[0]
    for i in new_profit[1:]:
        change = int(i) - int(prev_profit)
        prev_profit = int(i)
        change_list.append(change)
        average_change = sum(change_list)/len(change_list)
    
print("Average change: " + str(average_change))

print("Greatest increase in profits: " + str(max(change_list)))
print("Greatest decrease in profits: " + str(min(change_list)))


         
         









         

