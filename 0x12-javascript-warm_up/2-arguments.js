#!/usr/bin/node

const argv = require('node:process').argv;

const argsLen = argv.length - 2;

if (argsLen === 0) {
  console.log('No argument');
} else if (argsLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
