var carToyota = ["Camry", 2010, "sedan", "black", true];
console.log(carToyota[1]);

var carToyota = {
    model: "Camry",
    year: "2010",
    carBody: "sedan",
    color: "black",
    hasAirbag: true
};

var x = "hasAirbag";
console.log(carToyota["carBody"]);
console.log(carToyota.color);
console.log(carToyota.hasAirbag);

carToyota.color = "red";
console.log(carToyota.color);
console.log(carToyota);
carToyota.year += 2
console.log(carToyota);

var carMazda = {}
var carOpel = new Object();
carOpel.model = "hatchback";
carOpel.year = 2021;
carOpel.carBody = "CX5";
carOpel.color = "yellow";
carOpel.hasAirbag = true
carOpel.doorNumber = "2";

console.log(carOpel);

carMazda.year = 2018;
carMazda.model = "crossover";
carMazda.carBody = "CX7";
carMazda.hasAirbag = false
carMazda.doorNumber = 4;

console.log(carMazda);