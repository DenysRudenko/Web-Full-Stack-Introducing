// push/pop
// shift/unshift
// index0f
// slice

var names = ["John", "Jane", "Jack", "Jim"];
console.log(names);
//names[4] = "Jeen";
names.push("Jeen"); // use .push to add new element to array
console.log(names);

var x = names.push("Jeen");
x = names.push("Ivan");
console.log(names);
console.log(x);

var y = names.pop();
console.log(names);
console.log(y);

console.log("-".repeat(30));

names.unshift("Irene");
console.log(names);
console.log(x);

y = names.shift();
console.log(names);
console.log(y);