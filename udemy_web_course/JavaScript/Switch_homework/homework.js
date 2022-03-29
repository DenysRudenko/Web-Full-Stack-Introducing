var userName = prompt("Enter your login!")
var userPassword = prompt("Enter your password!")

switch (true) {
    case userName === "Vasya" && userPassword === "1111":
        alert("You`re Welcome " + userName);
        break;
    case userName === "Vanya" && userPassword === "2222":
        alert("You`re Welcome " + userName);
        break;
    case userName === "Admin" && userPassword === "1111":
        alert("You`re Administrator! You can edit a website!");
        break;
    default:
        alert("Your password or login wrong!");    
}
