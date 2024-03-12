#!/usr/bin/node

const argv = require('node:process').argv;
const number = Number(argv[2]);

console.log(factorial(number));

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return (1);
  }

  return (n * factorial(n - 1));
}
