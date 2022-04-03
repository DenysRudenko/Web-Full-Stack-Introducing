function someFunction() {
    var x = 1;
    var y = 10;
    console.log(x);
    console.log(y);
    y++;
}

var y = 2;

someFunction();
console.log(y);

console.log("-".repeat(30));

// 1`st assigment.
// Please answer what result is expected without running the code.

var x = 7

function someFunction(){
    x++;
}

console.log(x);
x++;
console.log(x);

console.log("-".repeat(30));

//Expected result in the console = 7, 8.

// 2`nd assigment.

function someFunction() {
    var x = 4;
    x++;
}

function anotherFunction() {
    console.log(x);
}

someFunction();
anotherFunction();

//Expected result n the console = Variable x is not defined.