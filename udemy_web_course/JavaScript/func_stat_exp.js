/*function animalVoice(animal, animalName) {
    switch (animal) {
        case "dog":
            return animalName + " barks.";
        case "cat":
            return animalName + " meows.";
        case "pig":
            return animalName + " grunts.";
        default:
            return animalName + " make some sounds.";
    }
}

console.log(animalVoice("dog", "Richard"));*/

var animalVoice = function(animal, animalName) {
    switch (animal) {
        case "dog":
            return animalName + " barks.";
        case "cat":
            return animalName + " meows.";
        case "pig":
            return animalName + " grunts.";
        default:
            return animalName + " make some sounds.";
    }
}

console.log(animalVoice("dog", "Richard"));

animalVoice = 19;

console.log(animalVoice("cat", "Richard"));
