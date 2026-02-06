# By Nolan Nelsen
# Written on 2/5/2026
# Hot Dog

# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%.
# Write a program the inputs the type of hot dog wanted and optional toppings.
# The program then displays the hot dog cost, tax and total cost.

hot_dog = 3.50
chili_dog = 4.50
cheese = 0.50
peppers = 0.75
grilled_onions = 1.00
tax_rate = 0.07

print("Hot Dog Options:")
print("1: Hot Dog ($3.50)")
print("2: Chili Dog ($4.50)")
choice = input("Which type of hot dog do you want? (1 or 2): ")

cost = 0

if choice == "1":
    cost = hot_dog
elif choice == "2":
    cost = chili_dog

choice = input("Would you like to add cheese for an additional $0.50? (Y/N): ")
if choice == "Y":
    cost +=cheese

choice = input("Would you like to add peppers for an additional $0.75? (Y/N): ")
if choice == "Y":
    cost +=peppers

choice = input("Would you like to add grilled onions for an additional $1.00? (Y/N): ")
if choice == "Y":
    cost +=grilled_onions

tax = cost*tax_rate
total = cost + tax

print(f"Hotdog cost: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
