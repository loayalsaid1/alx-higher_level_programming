#!/usr/bin/node

const fs = require('node:fs');

const path = process.argv[2];
const writeText = process.argv[3];

fs.writeFile(path, writeText, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
