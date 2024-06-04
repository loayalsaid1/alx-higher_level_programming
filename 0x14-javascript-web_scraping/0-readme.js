#!/usr/bin/node

const fs = require('node:fs');

const path = process.argv[2];

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
