var userName = prompt("Whats is your name?");
var userAge = prompt("Type your age!");
var isMarried = false;

if (userAge >= 18) {
    alert(userName + " is adult.");
} else if (userAge < 10) {
    alert(userName + " is a child.");
} else if (userAge > 10 && userAge < 18) { // also we can use || //
    alert(userName + " is a teeneger.")
}

if (isMarried) {
    alert(userName + " is married.")
} else {
    alert(userName + " maybe will married soon :)")
}