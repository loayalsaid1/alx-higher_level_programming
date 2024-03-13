#!/usr/bin/node

const { exit } = require('node:process');
const fs = require('fs');
const argv = require('node:process').argv;

if (argv.length < 5) {
  exit(1);
}

const fileAName = argv[2];
const fileBName = argv[3];
const fileCName = argv[4];

fs.readFile(fileAName, 'utf-8', (err, data1) => {
  if (err) {
    console.error('Error reading file A:', err);
    exit(1);
  }

  fs.readFile(fileBName, 'utf-8', (err, data2) => {
    if (err) {
      console.error('Error reading file B:', err);
      exit(2);
    }

    const concatinatedContent = `${data1}${data2}`;

    fs.writeFile(fileCName, concatinatedContent, 'utf-8', (err) => {
      if (err) {
        console.error('Error writing file B:', err);
        exit(2);
      }
    });
  });
});
