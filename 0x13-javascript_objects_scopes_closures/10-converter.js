#!/usr/bin/node
function converter (base) {
  function convert (number) {
    return (number.toString(base));
  }
  return (convert);
}

exports.converter = converter;
