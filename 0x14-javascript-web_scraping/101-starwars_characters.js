#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

let characters = [];

async function printNamesInOrder (characters) {
  for (const character of characters) {
    let person = await fetch(character);
    person = await person.json();

    console.log(person.name);
  }
}

request(url, (err, res, body) => {
  if (!err) {
    const film = JSON.parse(body);
    characters = film.characters;
    printNamesInOrder(characters);
  }
});
