<script type="text/javascript">
  $(document).ready(function () {
  
    $('#btn-get').click(function () {
        var result = { };
        $.each($('form').serializeArray(), function() {
            result[this.name] = this.value;
        });
        var form_data='{"yearinput":"' + result.yearinput+'"}';
        
        $.ajax({
            method: 'POST',
            url: '/post_submit',
            data: form_data,
            contentType: "application/json",
            success: function (data) {
                // Get and display the result
                alert(data);
                console.log(data);
            },
        });
    });

});
        
</script>