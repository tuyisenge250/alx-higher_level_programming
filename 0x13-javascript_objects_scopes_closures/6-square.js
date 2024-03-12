#!/usr/bin/node
const Squareq = require('./5-square');

class Square extends Squareq{
    charPrint(c){
        if(c === undefined){
            c = "X"
        }
        let i,j;
        for(i =0; i < this.height; i++){
            let result = "";
            for(j = 0; j < this.width; j++){
                result += c;
            }
            console.log(result);
        }
    }
}
module.exports = Square