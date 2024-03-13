#!/usr/bin/node

function nbOccurences (list, searchElement) {
  if (!(list instanceof Array)) {
    return (0);
  }
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  return (count);
}

module.exports.nbOccurences = nbOccurences;
