var height = prompt("Please input your height in meters")
var weight = prompt("Please input your weight")

var bodyWeightIndex = weight / (height * height);
var doYouHaveExcessWeight = bodyWeightIndex > 28;

alert("You have excess weight:" + doYouHaveExcessWeight);
