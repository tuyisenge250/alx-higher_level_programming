#!/usr/bin/node
if(Number(process.argv[2]) === NaN || Number(process.argv[2]) === 0 || Number(process.argv[2]) === 1){
    console.log(1);
}
else{
    let i;
    let result = 1;
    for(i = 2; i <= Number(process.argv[2]); i++){
        result *= i;
    }
    console.log(result);
}