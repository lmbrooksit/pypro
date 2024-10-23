print("Welcome to the tip calculator")

bill = float(input("what was the total bill? $"))
tip = int(input("What percentage tip would you like to give 10 12 15 "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
bill_per_person = bill_with_tip / people
print(round(bill_per_person, 2))