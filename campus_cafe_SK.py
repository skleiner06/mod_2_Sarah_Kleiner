'''
Name: Sarah Kleiner
Assignment: Campus Cafe

# PSEUDOCODE:
#
# display menu:
#
# coffee = $2.25
# muffins = $2.75
#
# input= how many coffees? integer >= 0
# input= how mnay muffins? integer >= 0
# input= enter tip percent nubmer >= 0
#
# coffee total = price * quantity
# muffin total = price * quantity
# subtotal = coffee total + muffin total
# tax = subtotal * 0.08875
# tip = subtotal * tip percent/100
#
# total = subtotal + tax + tip
#
# print (receipt)
# print (quantity x item @ price = total)
# print (quantity x item @ price = total)
# print (subtotal)
# print (tax)
# print (tip)
# print (total)
'''
# Defines a function that returns every number with two places after decimal point
def format_currency(x):
    return "$" + format(x, ".2f")

# Defines a function that establishes totas is the unit price times quantity
def line_total(unit_price, quantity):
    total = unit_price * quantity
    return total

# Defines a function that establishes the value of tax, tip and total
def compute_totals(subtotal, tax_percent, tip_percent):
    tax = subtotal * tax_percent
    tip = subtotal * (tip_percent / 100)
    total = subtotal + tax + tip
    return tax, tip, total

# Defines a function that prints the receipt
def print_receipt(coffee, muffins, coffee_total, muffin_total, subtotal, tax, tip, total):

    print("--- Receipt ---")
    print(coffee, "x Coffee @ $2.25 = ", format_currency(coffee_total))
    print(muffins, "x Muffins @ $2.75 = ", format_currency(muffin_total))
    print("Subtotal: ", format_currency(subtotal))
    print("Tax: ", format_currency(tax))
    print("Tip: ", format_currency(tip))
    print("TOTAL: ", format_currency(total))
    print("Thank you!")

# Defines a function that prints the main body and operations on this receipt
def main():

    # Price of the items and tax
    coffee_price = 2.25
    muffin_price = 2.75
    tax_percent = 0.08875

    # Prints the first few lines of receipt
    print("=== Campus Café ===")
    print(f"Coffee: ${coffee_price}")
    print(f"Muffin: ${muffin_price}")

    # User input using try/except to obtain the correct values
    try:
        coffee = int(input("How many coffees?"))
        muffins = int(input("How many muffins?"))

    except ValueError:
        print("Please enter an integer greater than or equal to 0.")

    # User input using try/except to obtain the correct value
    try:
        tip_percent = float(input("Enter tip percent (e.g., 10 for 10%): "))

    except ValueError:
        print("Please enter a number greater than or equal to 0.")

    # Variable that calculates the line_total for each item
    coffee_total = line_total(coffee_price, coffee)
    muffin_total = line_total(muffin_price, muffins)
    subtotal = coffee_total + muffin_total

    # Calls the function that computes the value for each of the arguments
    tax, tip, total = compute_totals(subtotal, tax_percent, tip_percent)

    # Prints the receipt with the totals
    print_receipt(coffee, muffins, coffee_total, muffin_total, subtotal, tax, tip, total)

main() # Calls the function main()
