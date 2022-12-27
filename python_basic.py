
#print("Good Morning")
#city_name=input("What city did you grew up")
#pet_name=input("whats your pet name")
#band_name= input("city_name"+("pet_name"))
#print("heloo there\nheloo there")
print("Welcome to Tip Calculator!")

bill =  int(input("What is the total bill? $"))
people= int(input("How many people will split the bill?"))
tip = int(input("How much will you tip? $"))
bill_with_tip = tip/100 *bill+bill
print(bill_with_tip)
total_bill = bill+bill_with_tip
bill_per_each= total_bill/people
final_amount =round(bill_per_each,2)
print(f"Each should pay: ${final_amount}")
print("I want a new bill")

