print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip /100)

final_amount = tip_amount + bill

final_amount_per_person = round((final_amount/people), 2)

print(f"Each person should tip {final_amount_per_person} $")
