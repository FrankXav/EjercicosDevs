const num = 5; //Declaracion de constantes 
console.log("La constante vale: ", num)

let var1; //declaracion de variables 
var1=23;
console.log("El valor de la variable es: ",var1)

//Condicional if

if(var1===23){
    console.log("True condition")
}else if(num===5){
    console.log("True condition")
}else{
    console.log("Ninguna condcion es verdadera")
}

const miArreglo = ['leon','tortuga','jirafa']

//for
for(let i = 0; i < 3; i++){
    console.log("Animal: ",miArreglo[i])
}
//range js

miArreglo.forEach(element => {
    console.log('Animal ', element)
});

//Crear array apartir de otro
const nuevoarray =miArreglo.map(animal => {
    return animal + " grande";  //creara el nuevo array con lo que retornemos 
})

console.log(nuevoarray)

//condiciones array
ArrayNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

let ValoresAltos = ArrayNum.filter(numero => numero > 10); //La condicion es numero >10

console.log(ValoresAltos)

//agregar elemento a array
ArrayNum.push(25)
console.log(ArrayNum)
//Alt+Shift+a comentar bloque

/* let preubaendato = prompt("Ingrese un dato") //Ventana emeergente
console.log(typeof(preubaendato)) */

/* let a = parseInt(readLine());
console.log(typeof(a)) */

/* process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

function solveMeFirst(a, b) {
  // Hint: Type return a+b below   
  return a+b;
}


function main() {
    var a = parseInt(readLine());
    var b = parseInt(readLine());;

    var res = solveMeFirst(a, b);
    console.log(res);
} */

let a;
let b;

a=6;
b=4

function SolveMeFirst(num1,num2){
	return num1+num2
}


console.log(SolveMeFirst(6,4))