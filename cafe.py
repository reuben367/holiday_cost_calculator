# code to calculate total value of all stock items on a menu

menu = ["ham", "egg", "chips", "toast"]

stock = {'ham': 30, 'eggs' : 62, 'chips' : 634, 'toast' : 70}

price = {'ham': 1.20, 'eggs' : 0.65, 'chips' : 2.5, 'toast' : 1}

total_value = 0

# iterate over each key: value pair in stock dictionary, if key matches key in item multiply stock value by item value and add to total
for item in stock:
    if item in price:
        total_value += stock[item] * price[item]

print(f"Total value of all stock is £ {total_value}")

# alternative solution that removes the consider iterating with .items() method, however I am unsure
# why this is a better solution
# for key, value in stock.items():
#     if key in price:
#         total_value += value * price[key]

# print(f"Total value of all stock is £ {total_value}")
    




#for item, quantity in stock.items():

# for item,  in stock:
#     if item in price:
#         total_value += stock[item] * price[item]

# stock_value = stock.values()
# print(stock_value)
# # total = 0
# for i in range(0,len(menu)):
#     print(menu[i])
#     if stock



# for quantity in stock.values():
#     for amount in price.values():
#         if stock.keys() == price.keys():
#             print(stock.keys())



#print(stock.keys())
# calculate total stock, multiply each item by its stock value and by price value
# item_value = (stock[items] * price[items])
# print(menu)
# print(stock)
# print(price)

#print(float(stock['ham']) * float(price['ham']))