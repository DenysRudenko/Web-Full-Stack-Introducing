$('ul').on('click', 'li', function () {
    $(this).toggleClass('done');
})

$('ul').on('click', 'span', function (event) {
    event.stopPropagation();
    $(this).parent().fadeOut(function () {
        $(this).remove();
    });
})

$('input').keypress(function (event) {
    if (event.which === 13) {
        var itemText = $(this).val();                                     //method val
        $(this).val('');
        $('ul').append('<li><span>x</span> ' + itemText + '</li>');        //adding new element
    }
})

$('h2 span').click(function () {
    $('input').fadeToggle();
})

