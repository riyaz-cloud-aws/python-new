name = input("Enter Student Name: ")
grade =  int(input("Enter  Student Grade : "))
base_fee =  float(input("Extra Base_Fee : "))
discount_percentage =  float(input("Extra Discount_Percentage % (if any) "))
topper =  input("Is the student an academic topper? (yes/no): ")

# validate grade
if grade < 1 or grade > 12:
    print("Invalid grade! grade must be between 1 to 12.")
else:
    if grade >= 9:
        if topper == "yes":
         initial_disocunt = 20
        else: 
         initial_discount = 10 
    elif grade >= 6:
         initial_disocunt = 5
    else :
          initial_disocunt = 0


# initial discount logic
if grade == 10:
     extra_discount = 3
elif grade == 12:
     extra_discount = 5
else :
     extra_discount = 0

# total discount
total_discount = initial_disocunt + extra_discount + discount_percentage

# calculations

discount_amount = (total_discount / 100) * base_fee
final_fee = base_fee - discount_amount


print("\n--- Tution Fee Summary ---") 
print("Student name:", name)
print("Grade :", grade)
print("Base fee:", base_fee)
print("Academic Topper:", topper)
print("Total Discount:", total_discount)
print("Discount Amount:", discount_amount)
print("Total amount to be paid :", final_fee)