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

def format_currency(x):
    return "$" + format(x, ".2f")

def line_total(unit_price, quantity):
    total = unit_price * quantity
    return total

def compute_totals(subtotal, tax_percent, tip_percent):
    tax = subtotal * tax_percent
    tip = subtotal * (tip_percent / 100)
    total = subtotal + tax + tip
    return tax, tip, total

def print_receipt(coffee, muffins, coffee_total, muffin_total, subtotal, tax, tip, total):

    print("--- Receipt ---")
    print(coffee, "x Coffee @ $2.25 = ", format_currency(coffee_total))
    print(muffins, "x Muffins @ $2.75 = ", format_currency(muffin_total))
    print("Subtotal: ", format_currency(subtotal))
    print("Tax: ", format_currency(tax))
    print("Tip: ", format_currency(tip))
    print("TOTAL: ", format_currency(total))
    print("Thank you!")

def main():

    coffee_price = 2.25
    muffin_price = 2.75
    tax_percent = 0.08875

    print("=== Campus Café ===")
    print(f"Coffee: ${coffee_price}")
    print(f"Muffin: ${muffin_price}")


    try:
        coffee = int(input("How many coffees?"))
        muffins = int(input("How many muffins?"))

    except ValueError:
        print("Please enter an integer greater than or equal to 0.")

    try:
        tip_percent = float(input("Enter tip percent (e.g., 10 for 10%): "))

    except ValueError:
        print("Please enter a number greater than or equal to 0.")

    coffee_total = line_total(coffee_price, coffee)
    muffin_total = line_total(muffin_price, muffins)
    subtotal = coffee_total + muffin_total

    tax, tip, total = compute_totals(subtotal, tax_percent, tip_percent)

    print_receipt(coffee, muffins, coffee_total, muffin_total, subtotal, tax, tip, total)

main()
