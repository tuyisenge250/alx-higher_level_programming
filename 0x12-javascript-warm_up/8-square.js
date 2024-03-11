#!/usr/bin/node
if(isNaN(process.argv[2]) || process.argv[2] === undefined){
    console.log("Missing size");
}
else{
    let i,j;
    for(i = 0; i < process.argv[2]; i++){
        let container ="";
        for(j = 0; j < process.argv[2]; j++){
            container += "x";
        }
        console.log(container);
    }
}