/*
var h1 = document.getElementById("header");

console.log(h1.innerHTML);

h1.addEventListener("click", function () {
    this.style.color = "blue";
});
*/

var liElements = document.querySelectorAll("li");

console.log(liElements);

var changeLicolor = function () {
        this.style.color = "green";
    };

for (var i = 0; i < liElements.length; i++) {
    liElements[i].addEventListener("click", changeLicolor)
}