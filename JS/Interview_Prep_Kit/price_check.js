/* 
Given product list and their prices, check if the products being sold have price discrepencies
Example:
products = [egg, milk, cheese]
productPrices = [2.89, 3.29, 5.79]
productSold = [egg, egg, milk, cheese]
productSoldPrices = [2.89, 2.99, 3.29, 5.79]
Answer => The 2nd batch of eggs sold were sold for 0.10 cents higher there is 1 price discrepency
*/
function priceCheck(products, productPrices, productSold, soldPrice) {
  // Store products and prices in hash
  let map = {};
  for (let i = 0; i < products.length; i++) {
    map[products[i]] = productPrices[i];
  }
  // Create result and increment for every price discrepency
  let result = 0;
  // Loop through sold and check of the values from hash is the same as sold prices
  for (let i = 0; i < productSold.length; i++) {
    if (map[productSold[i]] !== soldPrice[i]) {
      result++;
    } else {
      continue;
    }
  }
  return result;
}
