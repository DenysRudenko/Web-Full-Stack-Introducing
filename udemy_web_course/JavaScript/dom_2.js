var ul = document.getElementsByTagName("ul");
console.log(ul[0].innerHTML);

var li = document.getElementsByTagName("li");
console.log(li[0].innerHTML);
li[0].textContent = "The <strong>html</strong> elements as objects";
console.log(li[0].innerHTML);