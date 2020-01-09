function countingValleys(n, s) {
  let valleys = 0;
  let currLevel = 0;
  for (let step of s) {
    //If it goes up past sea level, increment valleys
    if (step === "U") {
      currLevel++;
      if (currLevel === 0) {
        valleys++;
      }
    } else {
      currLevel--;
    }
  }
  return valleys;
}
