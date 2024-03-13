#!/usr/bin/node
function logMe (arg) {
  const log = Object.getOwnPropertyDescriptor(logMe, 'log');
  if (!log) {
    logMe.log = 0;
  }
  console.log(`${logMe.log}: ${arg}`);
  logMe.log++;
}

exports.logMe = logMe;
