$(document).ready(function() {
    $("#generate").on('click', function() {
        let val = $('#input_field');
        let num = val[0].value;
        req = $.ajax({
            url: '/',
            type: 'POST',
            data: {num: num}
        })
        req.done(function(data) {
            $('#sentence').text(data.sentence);
        });
    });

    $("#favorite").on('click', function() {
        let sentence = $('#sentence').text();
        req = $.ajax({
            url: '/favorites',
            type: 'POST',
            data: {sentence: sentence}
        })
        req.done(function(data) {
            console.log('req done')
        });
    });
});