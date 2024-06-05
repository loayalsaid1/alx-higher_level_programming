#!/usr/bin/node

const request = require('request');

const api = process.argv[2];
const id = 18;
let count = 0;

request(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].endsWith(`${id}/`)) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
