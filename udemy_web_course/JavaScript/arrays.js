var color1 = "red";
var color2 = "orange";
var color3 = "yellow";
var color4 = "green";
var color5 = "blue";
var color6 = "indigo";
var color7 = "violet";

var rainbowColors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

console.log("The sky is " + rainbowColors[4]);

rainbowColors[0] = "orange";
console.log(rainbowColors);

rainbowColors[8] = "red";
console.log(rainbowColors);

rainbowColors[rainbowColors.length] = "dark bule";
console.log(rainbowColors);

var emptyArray = [];
var emptyArrayNew = new Array();

var numbers = [1, 3, 5, 32];
console.log(numbers);

var anyItems = [1, "some text", null];
console.log(anyItems);
