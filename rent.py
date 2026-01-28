## inputs we need from the user
# total rent
# total food ordered for sancking
# electricity units spend
# charge per unit
# person living in room/flat


rent = int(input("Enter your room/hostel rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_bill = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of person living in room/hostel = "))

total_bill = electricity_bill * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person bill pay  = "  , output)