#!/usr/bin/node

const request = require('request');
const argv = require('node:process').argv;

request.get(argv[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
