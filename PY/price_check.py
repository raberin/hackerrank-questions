"""
Given product list and their prices, check if the products being sold have price discrepencies
Example:
products = [egg, milk, cheese]
productPrices = [2.89, 3.29, 5.79]
productSold = [egg, egg, milk, cheese]
productSoldPrices = [2.89, 2.99, 3.29, 5.79]
Answer => The 2nd batch of eggs sold were sold for 0.10 cents higher there is 1 price discrepency
"""


def price_check(products, product_prices, product_sold, sold_price):
    # Create a map to hold all products and prices
    map = {}
    for i in range(len(products)):
        map[products[i]] = product_prices[i]
    # Create result and increment when theres a price discrepency
    result = 0
    # Loop through sold products/prices and cross check with map to see if theres a discrepency
    for i in range(len(product_sold)):
        # Check map's values and compare with sold prices
        if map[product_sold[i]] != sold_price[i]:
            result += 1
        else:
            continue
    return result


products = ["egg", "milk", 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold = ["egg", "egg", "milk", 'cheese']
productSoldPrices = [2.89, 2.99, 3.29, 5.79]
print(price_check(products, productPrices,
                  productSold, productSoldPrices))  # Answer is 1
