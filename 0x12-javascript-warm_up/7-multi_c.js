#!/usr/bin/node
const x = process.argv[2]
if(isNaN(x) || x === undefined){
    console.log("Missing number of occurrences");
}
else{
    for( n = 0; n < x; n++){
        console.log("C is fun");
    }
}