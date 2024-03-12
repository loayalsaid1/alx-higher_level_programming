#!/usr/bin/node

const argv = require('node:process').argv;

add(Number(argv[2]), Number(argv[3]));

function add (a, b) {
  console.log(a + b);
}
