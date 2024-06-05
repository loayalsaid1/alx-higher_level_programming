#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

let characters = [];

request(url, (err, res, body) => {
  if (!err) {
    const film = JSON.parse(body);
    characters = film.characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (err, res, body) => {
        if (!err) {
          const person = JSON.parse(body);
          console.log(person.name);
        }
      });
    }
  }
});
