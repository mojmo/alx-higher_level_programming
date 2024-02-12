#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) { return 1; }
  return n * factorial(n - 1);
}

const num = Number(process.argv[2]);

console.log(isNaN(num) ? 1 : factorial(num));
