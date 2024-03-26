#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to fetch the movie details
request.get(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const film = JSON.parse(body);
  let characterIndex = 0;

  // Define a recursive function to print characters sequentially
  const printNextCharacter = () => {
    // Check if there are more characters to print
    if (characterIndex < film.characters.length) {
      // Retrieve the URL of the next character
      const characterUrl = film.characters[characterIndex];

      // Make a GET request to fetch the character details
      request.get(characterUrl, (charErr, charRes, charBody) => {
        if (charErr) {
          return console.log(charErr);
        }

        const character = JSON.parse(charBody);
        console.log(character.name);

        // Increment the character index to process the next character
        characterIndex++;

        // Recursively call the printNextCharacter function to print the next character
        printNextCharacter();
      });
    }
  };

  // Start the process by calling the printNextCharacter function
  printNextCharacter();
});
