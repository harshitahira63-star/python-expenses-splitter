#bill split calculator
total_bill=float(input("enter total bill amount:₹"))
number_of_people= int(input("enter number of people :"))
split_amount=total_bill/number_of_people
print(f"each person should pay:₹{split_amount:.2f}") 