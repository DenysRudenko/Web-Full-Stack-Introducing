function isNumberOdd(number) {
    return number % 2 !== 0;
}

var x = isNumberOdd(10); // false
console.log(x);
console.log(isNumberOdd(0)); // false
isNumberOdd(0); // false
isNumberOdd(23); // true

console.log("-".repeat(10));

function factorial(naturalNumber) {
    var result = 1;
    for (i = 1; i <= naturalNumber; i++){
        result = result * i;
    }
    return result;
}

console.log(factorial(5)); // 120
console.log(factorial(7)); // 5040
console.log(factorial(0)); // 1

console.log("-".repeat(10));

function changeSpaceToUnderscore(text) {
    var resultText = text.replace(/ /g, "_");
    return resultText;
}

console.log(changeSpaceToUnderscore("create function"));
console.log(changeSpaceToUnderscore("my first name"));
console.log(changeSpaceToUnderscore("user"));

