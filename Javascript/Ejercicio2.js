let Numsum = [4,65,24,89,22]

function restriccion(Arreglonum){
    let prueba=true;
    let n=Arreglonum.length 
    for(let i=0;i<n;i++){
        //console.log(typeof(Arreglonum[i]))
        if (prueba === true){
            if (Arreglonum[i]<1 || Arreglonum[i]>1000000000){
                prueba = false
            }else {
                prueba = true
            }
        }
    }
    return prueba
}


function SumaMaxyMin(Numprob){
    if(restriccion(Numprob)){
        let menor = Math.min.apply(Math,Numprob)
        let mayor = Math.max.apply(Math,Numprob)
        console.log(menor)
        console.log(mayor)
        let Numerosmayor = Numprob.filter(numero => numero !== mayor)
        let Numerosmenor = Numprob.filter(numero => numero !== menor)
        let n=Numerosmayor.length 
        let sumama=0;
        let sumame=0;
    for(let i=0;i<n;i++){
        sumama = sumama + Numerosmayor[i];
        sumame = sumame + Numerosmenor[i];
    }
    console.log("La menor suma obtenido es: ",sumame)
    console.log("La mayor suma obtenido es: ",sumama)
    }else{
        console.log("Algun numero de arreglo es menor a 1 o mayo a 1x10^9")
    }
}

SumaMaxyMin(Numsum)