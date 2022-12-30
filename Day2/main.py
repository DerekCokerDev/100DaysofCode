print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_of_people = input("How many people will split the bill? ")

each_pay = float(total_bill) * (1 + (float(tip_percentage)/100)) / int(num_of_people)

print(f"Each person should pay: ${each_pay:.2f}")
