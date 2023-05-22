#!/usr/bin/node

const request = require('request');

// Movie ID (episode number)
const movieID = process.argv[2];

// API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Send GET request to the Star Wars API
request(apiUrl, function(error, response, body) {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const movieTitle = movieData.title;
    console.log(`Title of Episode ${movieID}: ${movieTitle}`);
  } else {
    console.log('Error fetching movie data.');
  }
});

