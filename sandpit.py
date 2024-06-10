import pandas


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# lists to hold ticket details
all_doughnuts = ["a", "b", "c", "d", "e"]
all_prices = [7.50, 7.50, 10.50, 10.50, 6.50]

order_dict = {
    "Flavour": all_doughnuts,
    "Price": all_prices,
}

dougnut_frame = pandas.DataFrame(order_dict)
dougnut_frame = dougnut_frame.set_index('Flavour')

# Calculate the total ticket cost (ticket + surcharge)
dougnut_frame['Total'] = dougnut_frame['Flavour'] \
                            + mini_movie_frame['Price']

# calculate ticket and profit totals
total = dougnut_frame['Total'].sum()

# currency formatting (uses currency function)
add_dollars = ['Price', 'Total']
for var_item in add_dollars:
    dougnut_frame[var_item] = dougnut_frame[var_item].apply(currency)

print("---- order ----")
print()

# output table with ticket data
print(dougnut_frame)

print()
print("----- Cost -----")

# output total ticket sales and profit
print("Total cost: ${:.2f}".format(total))

