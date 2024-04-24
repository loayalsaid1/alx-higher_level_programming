#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

if (argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
    process.exit(1);
  }

  try {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } catch (parseError) {
    console.error('Error parsing response body:', parseError);
    process.exit(1);
  }
});
