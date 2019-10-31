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
});