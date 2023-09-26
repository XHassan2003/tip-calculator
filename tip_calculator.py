#Tip_Calculator
print("Wellcome to Tip Calculator")
total = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, 15, 20: "))
spilt = int(input("How many people to spilt the bill: "))
tip = percent / 100 * total
total_with_tip = total + tip
spilt_bill = total_with_tip / spilt
final_amount = round(spilt_bill, 2)
final_amount = "{:,2f}".format(spilt_bill)
print(f"Each person should pay: $ {final_amount}")

