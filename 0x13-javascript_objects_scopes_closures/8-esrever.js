#!/usr/bin/node

exports.esrever = (list) => {
  const newList = [];
  const len = list.length;

  for (let i = 0; i < len; i++) {
    newList.push(list.pop());
  }

  return (newList);
};
