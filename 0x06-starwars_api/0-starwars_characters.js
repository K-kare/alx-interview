#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, res, body) {
  if (error) throw error;
  const actor = JSON.parse(body).characters;
  exactOrder(actor, 0);
});
const exactOrder = (actor, x) => {
  if (x === actor.length) return;
  request(actor[x], function (error, res, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    exactOrder(actor, x + 1);
  });
};
