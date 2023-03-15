#!/usr/bin/node
//prints the value of the argument
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
