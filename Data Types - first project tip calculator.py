#Welcome to the tip calculator.
#What was the total bill? $124.56
#What percentage tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 7
#Each person should pay: $19.93
print("Welcome to the tip calculator.")
billamount=float(input("What was the total bill? $"))
bill=float(input("What percentage tip would you like to give? 10, 12, or 15?"))
members=int(input("How many people to split the bill?"))
bill_tip_percent=bill/100
tip=billamount*bill_tip_percent
total_bill=billamount+tip
bill_per_eachone = total_bill/members
#used round function to print 2 digit in float output.
print(f"Each person should pay: {round((bill_per_eachone),2)}")