#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

const result = {};

request(url, (err, res, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    todos.forEach(todo => {
      if (todo.completed) {
        if (result[todo.userId]) {
          result[todo.userId] += 1;
        } else {
          result[todo.userId] = 1;
        }
      }
    });

    console.log(result);
  }
});
