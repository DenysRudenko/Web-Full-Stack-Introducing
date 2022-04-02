function square(number) {
    return number * number;
}

var x = square(2);
console.log(x);

function isSquareBig(side) {
    var squareArea = square(side);
    if (squareArea > 100) {
        return true;
    } else {
        return false;
    }
}

console.log(isSquareBig(2));

function twoReturns(x) {

    x = x - 8;

    console.log(x);

    return x;

    x = x + 8;

    console.log(x);

    return x;   

}

twoReturns(10);