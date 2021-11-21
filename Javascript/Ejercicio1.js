let a;
let b;

a=-2;
b=4;



function SolveMeFirst(num1,num2){
	if (num1<=1 && num2<=1000){
        return num1+num2
    } else{
        return "No cumple las restricciones"
    }
    
}


console.log(SolveMeFirst(a,b))