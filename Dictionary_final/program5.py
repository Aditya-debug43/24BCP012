prices = {'apple': 100, 'banana': 30, 'milk': 60}
quantities = {'apple': 2, 'banana': 5, 'milk': 1}
total = 0
for item in prices:
    if item in quantities:
        total += prices[item] * quantities[item]
print("Total bill:", total)