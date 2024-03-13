#!/usr/bin/node

const dict = require('./101-data').dict;

const occurences = new Set(Object.values(dict));
const userIDs = Object.keys(dict);
const newDict = {};

for (const i of occurences) {
  newDict[i] = getSimilerIDs(i);
}

console.log(newDict);

function getSimilerIDs (number) {
  const users = [];
  for (let i = 0; i < userIDs.length; i++) {
    if (dict[userIDs[i]] === number) {
      users.push(userIDs[i]);
    }
  }

  return (users);
}
