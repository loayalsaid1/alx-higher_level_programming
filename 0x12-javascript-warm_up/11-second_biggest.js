#!/usr/bin/node

const argv = require('node:process').argv;

if (argv.length < 4) {
  console.log(0);
} else {
  const args = argv.slice(2).map(item => Number(item));
  let maxNumber = Math.max(...args);
  args.splice(args.indexOf(maxNumber), 1);

  maxNumber = Math.max(...args);
  console.log(args[args.indexOf(maxNumber)]);
}
