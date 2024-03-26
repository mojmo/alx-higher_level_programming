#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const characters = JSON.parse(body).characters;

  characters.forEach(characterUrl => {
    request.get(characterUrl, (err, res, body) => {
      if (err) {
        return console.log(err);
      }

      console.log(JSON.parse(body).name);
    });
  });
});
