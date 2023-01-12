# cwChapter2.py
# Student Name: Tavaris Hooks
# Date: 01/11/2023
# Program Name: ClassWork (1/12/2023)
# Description: Program that will ask the user to enter the amount of purchase, then display the amount
#of the purchase, tax rates, and the total of the sale. 

# 1. Ask the user to enter the amount of the purchase
# 2. Create variables for both tax rates
# 3. Create total tax rate variable
# 4. Multiply and then add the total tax rate to the purchase amount for the total of the sale. 
# 5. Program should display everything from the previous steps and the total of sale.

Purchase_Amount = float(input("Enter the amount of the purchase. $")) # This will get the amount from user.

State_Sales_Tax = 0.05                                              # State Sales tax variable.

County_Sales_Tax = 0.025                                            # County sales tax variable.

Total_Sales_Tax = County_Sales_Tax + State_Sales_Tax                # Total Sales tax variable.

Sale_Total = Total_Sales_Tax * Purchase_Amount + Purchase_Amount    # This will give the total of the sale.

print("Amount of Purchase:", Purchase_Amount)                       # Display purchase amount.

print("State Sales Tax:", State_Sales_Tax)                          # Display state sales tax.

print("County Sales Tax:", County_Sales_Tax )                       # Display county sales tax.

print("Total Sales Tax:", Total_Sales_Tax)                          # Display total sales tax.

print("Total of the Sale:", Sale_Total)                             # Display the total of sale.



