$(document).ready(function () {

    $('#btn-get').click(function () {
        var form_data = new FormData($('#year-input'));


        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/post_submit',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text(' Result:  ' + data);
                console.log('Success!');
            },
        });
    });

});