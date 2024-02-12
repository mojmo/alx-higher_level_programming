#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

if (numbers.length <= 1) {
  console.log(0);
} else {
  const sortedArray = numbers.sort((a, b) => b - a);
  console.log(sortedArray[1]);
}
