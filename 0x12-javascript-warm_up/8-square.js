#!/usr/bin/node

const { argv } = require('node:process');

if (Number(argv[2])) {
  for (let i = 0; i < Number(argv[2]); i++) {
    for (let j = 0; j < Number(argv[2]); j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
