#!/usr/bin/node

const request = require('request');

const filmID = process.argv[2];
if (!filmID) {
  process.exit();
}

const url = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const jsonResponse = JSON.parse(body);
    console.log(jsonResponse.title);
  }
});
