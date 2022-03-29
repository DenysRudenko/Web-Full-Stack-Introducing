var section = "Javascript"; 

switch (section) {
    case "html":
        console.log("Yo`re learning section 'Switch'");
        break
    case "css":
        console.log("Yo`re learning section 'CSS'");
        break
    case "Javascript":
        console.log("Yo`re learning section 'Javascript'");
        break
    default:
        console.log("Yo`re learning section of Javascript 'Default'")
}
//EXample of if/else
/*if (age >= 18 && age <= 25) {
    groupNumber = 1;
} else if (age > 25 && age <= 46) {
    groupNumber = 2;
} else {
    groupNumber = 3;
}*/


var age = prompt("Type your age!")
var groupNumber;

switch (true) {
    case age >= 18 && age <= 25:
        groupNumber = 1;
        break;
    case age > 25 && age <= 46:
        groupNumber = 2;
        break;
    default:
        groupNumber = 3;
}

alert("Your groupnumber is " + groupNumber);