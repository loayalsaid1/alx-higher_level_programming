#!/usr/bin/node
module.exports.addMeMaybe = (x, theFunction) => {
  theFunction(++x);
};
