#!/usr/bin/node

const { argv } = require('node:process');

function factorial (num) {
  if (num === 1 || num === 0 || num === NaN) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(Number(argv[2])));
