var userName = "Jack";
var userWeight = prompt("Enter you weight!");

//---------------------------------------------
/* if (userWeight > 90) {
    alert(userName + " has reduntant weight.");
} else {
    alert(userName + " has a normal weight.");
} */
//----------------------------------------------

var weightDescription;

weightDescription = userWeight > 90 ? "redundant" : "normal";

alert(userName + " has " + weightDescription + " weight.");