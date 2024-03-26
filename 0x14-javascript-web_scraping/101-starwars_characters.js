#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const film = JSON.parse(body);

  film.characters.forEach(characterUrl => {
    request.get(characterUrl, (charErr, charRes, charBody) => {
      if (charErr) {
        return console.log(charErr);
      }

      const character = JSON.parse(charBody);

      console.log(character.name);
    });
  });
});
