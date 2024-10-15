# Program Name: Exam1.py
# Course: IT1114
# Student Name: Zenzele Broomfield
# Assignment Number: Exam 1
# Due Date: 9/29/2024
# Purpose: help users with tax calculations
# Resources: IDLE(Python 3.12 64 bit)

# to calculate tax based on income
def calculate_income_tax(income):
    if income < 10000:
        return income * 0.023
    elif 10000 <= income <= 50000:
        return income * 0.045
    else:
        return income * 0.061

# input section
income = float(input("What was your total income for this tax year?: "))

# marital status input
married = input("Are you married? [y/n]: ").lower()
if married == "y":
    years_married = int(input("How long have you been married?: "))
else:
    years_married = 0 # no deduction then

# elevation input
elevation_choice = int(input("Is the elevation of your home adresss below-1, at-2, above-3 sea level?[1/2/3]: "))

if elevation_choice == 3:
    bedrooms = int(input("How many bedrooms are in your house?: "))
else:
    bedrooms = 0 # only matters for people above sea level

# inital tax calculations
tax = calculate_income_tax(income)

# adjustments based on marital statue
if married == "y":
    tax -= 1.62 * years_married

# adjustments based on elevation
if elevation_choice == 1:
    tax += 18.32
if elevation_choice == 2:
    tax += income * 0.016
if elevation_choice == 3:
    tax += 5 * bedrooms

# just to make sure the tax doesnt go below zero
tax = max(tax, 0)

# output
print(f"The total tax for {income} is: ${tax:2f}")
