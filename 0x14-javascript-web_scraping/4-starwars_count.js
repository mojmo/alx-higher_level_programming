#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      if (film.characters.find((character) => character.endsWith('/18/'))) {
        count++;
      }
    });

    console.log(count);
  }
});
