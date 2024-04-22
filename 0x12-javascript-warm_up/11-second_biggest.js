#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  const myArr = argv.slice(2);
  myArr.sort((a, b) => b - a);
  console.log(myArr[1]);
}
