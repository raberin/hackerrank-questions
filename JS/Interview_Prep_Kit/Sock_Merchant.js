function sockMerchant(n, ar) {
  let map = {};
  let result = 0;
  for (let sock of ar) {
    if (map[sock]) {
      map[sock]++;
    } else {
      map[sock] = 1;
    }
  }
  //Loop a 2nd time to calculate all the pairs
  for (let key in map) {
    result += Math.floor(map[key] / 2);
  }
  return result;
}
