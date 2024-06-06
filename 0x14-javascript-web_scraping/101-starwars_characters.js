#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

let characters = [];

request(url, (err, res, body) => {
  if (!err) {
    const film = JSON.parse(body);
    characters = film.characters;

    const characterPromises = characters.map(character => {
      return new Promise((resolve, reject) => {
        request(character, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch((err) => console.log(err));
  }
});
