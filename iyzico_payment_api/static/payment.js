(function (window, $) {
    console.log("payyment")
    document.getElementById("currency").innerText = currency;

    function pay(payment_data) {

        let post_url = pay_url;
        $.ajax({
            url: post_url, // the endpoint
            type: "POST", // http method
            data: payment_data, // data sent with the post request

            // handle a successful response
            success: function (json) {
                //$('#post-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check

                if (json.error) {
                    alert(json.result);
                } else {
                    if (json.veri){
                        alert(json.veri);
                        alert("3ds is initialized")
                    }else {
                        alert("Congrulations! .Payment process is successful");
                    }
                    // window.location.href = index_url
                }
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    $('#payment_form').on('submit', function (event) {
        event.preventDefault();
        let payment_data = {
            name: $('#consumer_name').val(),
            surname: $('#consumer_surname').val(),
            email: $('#consumer_email').val(),
            country: $('#consumer_country').val(),
            city: $('#consumer_country').val(),
            full_address: $('#consumer_full_address').val(),
            credit_amount: $('#credit').val(),
            card_name: $('#cardname').val(),
            card_number: $('#cardnumber').val(),
            expiration_date: $('#expirationdate').val(),
            security_code: $('#securitycode').val(),

            // contract_read_and_accepted: $('#register-candidate-form-contract-read-and-accepted').is(':checked'),
            // type: 'candidate'
        };

        pay(payment_data);
    });

})(window, jQuery);
