$(document).ready(function() {
    $('#generate').on('click', function() {
        let val = $('#num_field');
        let num = val[0].value;

        let vowel = 'False';
        let checked = $('#vowel_field').is(':checked');
        // So that it isnt 'true' and instead is True
        if (checked) {
            vowel = 'True';
        }
        req = $.ajax({
            url: '/',
            type: 'POST',
            data: { num: num, vowel: vowel }
        });
        req.done(function(data) {
            $('#sentence').text(data.sentence);
        });
    });

    $('#favorite').on('click', function() {
        let sentence = $('#sentence').text();
        req = $.ajax({
            url: '/favorites',
            type: 'POST',
            data: { sentence: sentence }
        });
    });
});
