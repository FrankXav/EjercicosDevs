let Nums=[4,7,34,29,7]

function Sumaelemtos(ArrayNum){
    let n=ArrayNum.length 
    let sum=0;
    for(let i=0;i<n;i++){
        sum = sum + ArrayNum[i];
    }
    if(sum<1){
        console.log("No cumple restriccion")
    }else{
        console.log("La suma total del arreglo es: ",sum)
    }
}

Sumaelemtos(Nums)