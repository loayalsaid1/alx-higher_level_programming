#!/usr/bin/node

const fs = require('fs');
const argv = require('node:process').argv;

fs.readFile(argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`${data}`);
  }
});
