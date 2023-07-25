# for this TIP CALCULATOR, you can ONLY give 5%,10%,15%, or 20% tips
#print this
print ("""
Welcome to the TIP CALCULATOR
******************************
""")

# put the available tips in a list
perctips = [5,10,15,20]

# get the total bill
bill = float(input ("What is the total bill? "))
# get the percentage tip
tip = float (input ("How much percentage tip would like to add? 5, 10,  15, or 20: "))
# if the tip you selected tip is in the list, calculate the bill per person
if tip in perctips:
    person = float (input ("How many persons to split bill? "))
    total_bill = bill + (bill * tip/100)
    bill_per_person = total_bill/person
    # round to do 2 decimal place
    final_amt = round (bill_per_person, 2)
    print (f"Each person should pay {final_amt}")
# if the tip you selected is not in the list, the program stops
else:
    print ("That percentage tip is invalid.")