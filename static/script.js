$(document).ready(function() {
    $("#generate").on('click', function() {
        let val = $('#num_field');
        let num = val[0].value;

        let checked = $('#vowel_field').is(':checked');
        let vowel = 'False';
        // So that it isnt 'true' and instead is True
        if (checked) {
            vowel = 'True';
        }
        console.log(vowel);
        req = $.ajax({
            url: '/',
            type: 'POST',
            data: {num: num, vowel: vowel}
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