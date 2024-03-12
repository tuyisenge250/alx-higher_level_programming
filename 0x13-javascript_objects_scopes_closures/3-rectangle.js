class Rectangle{
    constructor(w,h){
        if((w > 0) && (h > 0)){
            this.width = w;
            this.height = h
        }
    }
    print(){
        let i,j;
        for(i =0; i < this.height; i++){
            let result = "";
            for(j = 0; j < this.width; j++){
                result += "X";
            }
            console.log(result);
        }
    }
}
module.exports = Rectangle