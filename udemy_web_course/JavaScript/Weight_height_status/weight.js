var age = prompt("Type your age!");
var height = prompt("Type your height in metres!");
var kilograms = prompt("Type your weight in kilograms!");

var formulaIndex = kilograms / (height * height);
var groupNumber;

if (age >= 18 && age <= 25) {
    groupNumber = 1;
} else if (age > 25 && age <= 46) {
    groupNumber = 2;
} else {
    groupNumber = 3;
}

if (groupNumber === 1 && kilograms < 17.5) {
    alert("Not enough kilograms!WARNING!REally bad four your health!");
} else if (groupNumber === 1 && formulaIndex >= 17.5 && formulaIndex < 19.5) {
    alert("Your weight not enough,WARNING for your health!");
} else if (groupNumber === 1 && formulaIndex >= 19.5 && formulaIndex < 23) {
    alert("Your weight is normal!");
} else if (groupNumber === 1 && formulaIndex >= 23 && formulaIndex < 27.5) {
    alert("Your weight is bigger than needed!");
} else if (groupNumber === 1 && formulaIndex >= 27.5 && formulaIndex < 30) {
    alert("Overwight by 1-st period!!!!");
} else if (groupNumber === 1 && formulaIndex >= 30 && formulaIndex < 35) {
    alert("Overwight by 2-nd period!!!!");
} else if (groupNumber === 1 && formulaIndex >= 35 && formulaIndex < 40) {
    alert("Overwight by 3-nd period!!!!");
} else if (groupNumber === 1 && formulaIndex >= 40) {
    alert("Overwight by 4-rd period!!!!");
} else if (groupNumber === 2 && kilograms < 18) {
    alert("Not enough kilograms!WARNING!REally bad four your health!");
} else if (groupNumber === 2 && formulaIndex >= 18 && formulaIndex < 20) {
    alert("Your weight not enough,WARNING for your health!");
} else if (groupNumber === 2 && formulaIndex >= 20 && formulaIndex < 26) {
    alert("Your weight is normal!");
} else if (groupNumber === 2 && formulaIndex >= 26 && formulaIndex < 28) {
    alert("Your weight is bigger than needed!");
} else if (groupNumber === 2 && formulaIndex >= 28 && formulaIndex < 31) {
    alert("Overwight by 1-st period!!!!");
} else if (groupNumber === 2 && formulaIndex >= 31 && formulaIndex < 36) {
    alert("Overwight by 2-nd period!!!!");
} else if (groupNumber === 2 && formulaIndex >= 36 && formulaIndex < 41) {
    alert("Overwight by 3-nd period!!!!");
} else if (groupNumber === 2 && formulaIndex >= 41) {
    alert("Overwight by 4-rd period!!!!");
} else if (groupNumber === 3) {
    alert("Not data for your age!")
}