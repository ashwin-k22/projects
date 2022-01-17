import csv

file_name = input("Enter the file name: ")

try:
    user = int(input("Amazon Data Analyzer (Choose one of the options): \n 1) Most expensive item \n 2) Least expensive item \n 3) Total spent (time period) \n 4) Average price (time period) \n"))
except ValueError as ve:
    print(ve)
    exit()
while(user < 1 or user > 4):
    user = int(input("Invalid input, please try again: "))

with open(file_name, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvfile)
    csvfile_size = 0
    for row in csvreader:
        csvfile_size += 1

    data_arr = [0] * csvfile_size
    i = 0
    csvfile.seek(0)
    next(csvfile)
    for row in csvreader:
        data_arr[i] = row
        i += 1
    
min_year = int(data_arr[0][0][6:])
max_year = int(data_arr[-1][0][6:])

if(user == 1):
    #index 29 is prices
    i = 0
    max_index = 0
    max_price = float(data_arr[0][29][1:])
    for i in range(len(data_arr)):
        if(float(data_arr[i][29][1:]) > max_price):
            max_price = float(data_arr[i][29][1:])
            max_index = i
    print("The most expensive item you bought was " + data_arr[max_index][2] + " for " + data_arr[max_index][29] + " on " + data_arr[max_index][0] + ".")

if(user == 2):
    i = 0
    min_index = 0
    min_price = float(data_arr[0][29][1:])
    for i in range(len(data_arr)):
        if(float(data_arr[i][29][1:]) < min_price and float(data_arr[i][29][1:]) > 0.00):
            min_price = float(data_arr[i][29][1:])
            min_index = i
    print("The least expensive item you bought was " + data_arr[min_index][2] + " for " + data_arr[min_index][29] + " on " + data_arr[min_index][0] + ".")

if(user == 3):
    upper_year = int(input("Enter the upper bound year (YY): "))
    while(upper_year < min_year or upper_year > max_year):
        upper_year = int(input("Invalid input, please try again: "))

    lower_year = int(input("Enter the lower bound year (YY): "))
    while(lower_year < min_year or lower_year > max_year or lower_year > upper_year):
        lower_year = int(input("Invalid input, please try again: "))
    
    upper_month = int(input("Enter the upper bound month (MM): "))
    while(upper_month < 1 or upper_month > 12):
        upper_month = int(input("Invalid input, please try again: "))
    
    lower_month = int(input("Enter the lower bound month (MM): "))
    while(lower_month < 1 or lower_month > 12):
        if(lower_year == upper_year):
            while(lower_month >= upper_month):
                lower_month = int(input("Invalid input, please try again: "))
        lower_month = int(input("Invalid input, please try again: "))
    
    user_lower_month = lower_month
    user_lower_year = lower_year
    total = 0.0

    while(upper_year >= lower_year and lower_month <= upper_month):
        for row in data_arr:
            print(int(row[0][6:]))
            print(lower_year)
            print(int(row[0][:2]))
            print(lower_month)
            print("\n")
            if(int(row[0][6:]) == lower_year and int(row[0][:2]) == lower_month):
                total += float(row[29][1:])

        if(upper_year != lower_year):
            if(lower_month != 12):
                lower_month += 1
            else:
                lower_year += 1
                lower_month = 1
        else:
            lower_month += 1
        
    print("From {:02d}/{} to {:02d}/{} you have spent ${}.".format(user_lower_month, user_lower_year, upper_month, upper_year, total))
