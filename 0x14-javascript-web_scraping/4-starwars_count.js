#!/usr/bin/node

const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/people/18';
request(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).films;

    console.log(films.length);
  }
});
