#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
