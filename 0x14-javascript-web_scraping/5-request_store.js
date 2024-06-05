#!/usr/bin/node

const fs = require('node:fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      console.log(err);
    });
  }
});
