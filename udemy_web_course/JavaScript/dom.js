/*
document.getElementById();
document.getElementsByClassName();
document.getElementsByTagName();
document.querySelector();
document.querySelectorAll();
*/


document.getElementById("header").innerHTML = "New Value";

var y = document.getElementsByClassName("firstThreeElements");
console.log(y);
console.log(y[1].innerHTML);

console.log(document.getElementsByTagName("body"));

console.log(document.querySelector("#header").innerHTML);

console.log(document.querySelectorAll("li"));