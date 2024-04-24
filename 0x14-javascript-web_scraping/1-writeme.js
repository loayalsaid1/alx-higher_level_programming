#!/usr/bin/node

const fs = require('fs');
const argv = require('node:process').argv;

fs.writeFile(argv[2], argv[3], 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
