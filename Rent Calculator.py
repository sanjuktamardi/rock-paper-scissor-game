# inputs
person = int(input("enter the number of person :"))
rent = int(input("enter your hostel rent :"))
food = int(input("enter your food cost :"))
electricity = int(input("Enter the total of electricity spend :"))
charge_per_unit = int(input("enter the charge/unit amount : "))

# Billing calculation
total_electricity_bill = charge_per_unit * electricity
total_bill = (food+rent+total_electricity_bill)/person

# Output
print("Each person will pay:",total_bill,"rs.")


