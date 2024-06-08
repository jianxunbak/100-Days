print("welcome to the tip calculator")
total_bill = float(input("what was the total bill?"))
percent = float(input("how much tip would you like to give? 10, 12 or 15?"))
Nos = float(input("how many people to split the bill with?"))
tip = (total_bill) * ((percent / 100) + 1) / Nos
final = "{:.2f}".format(tip)
print(f"Each person should pay: ${final}")

