$('li').click(function () {
    $(this).toggleClass('done');
})

$('span').click(function (event) {
    console.log('A span is clicked!');
    event.stopPropagation();
})

$('li').click(function () {
    $(this).toggleClass('A li is clicked!');
})

$('ul').click(function () {
    console.log('A ul is clicked!');
})

$('div').click(function () {
    $(this).toggleClass('A div is clicked!');
})

$('body').click(function () {
    $(this).toggleClass('A body is clicked!');
})

$('html').click(function () {
    console.log('A html is clicked!');
})

