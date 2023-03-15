#!/usr/bin/node

const myString = 'C is fun';
let x = Math.floor(Number(process.argv[2]));
if( x == 0 || isNaN(x))
{
    console.log('Missing number of occurrences');
}
else
{
    for(let i=0; i < x; i++)
    {
        console.log(myString);
    }
}
