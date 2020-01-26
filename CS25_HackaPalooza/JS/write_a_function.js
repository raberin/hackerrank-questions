const is_leap = year => {
  if (year % 4 === 0) {
    if (year % 100 !== 0) {
      leap = true;
    } else {
      if (year % 400 == 0) {
        leap = true;
      }
    }
  }
  return leap;
};

console.log(is_leap(2100)); //False
console.log(is_leap(2400)); //True
console.log(is_leap(2000)); //True
