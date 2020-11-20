$(document).ready(function(){
    console.log("selam")
    var current = 1;

    widget      = $(".tab");
    btnnext     = $(".next");
    btnback     = $(".back");
    btnsubmit   = $(".submit");

    // Init buttons and UI
    widget.not(':eq(0)').hide();
    hideButtons(current);
    fixStepIndicator(current);

    // Next button click action
    btnnext.click(function(){
        if(current < widget.length){
            // Check validation
            if($(".form").valid()){
                widget.show();
                widget.not(':eq('+(current++)+')').hide();
                fixStepIndicator(current);
            }
        }
        hideButtons(current);
    })

    // Submit button click
    // btnsubmit.click(function(){
    //     alert("Submit button clicked");
    // });


    // Back button click action
    btnback.click(function(){
        if(current > 1){
            current = current - 2;
            if(current < widget.length){
                widget.show();
                widget.not(':eq('+(current++)+')').hide();
                fixStepIndicator(current);
            }
        }
        hideButtons(current);
    })

    $('.form').validate({ // initialize plugin
        ignore:":not(:visible)",
        rules: {
            credit: { required: true, number: true },
            consumer_name     : "required",
            consumer_surname     : "required",
            email    : {required : true, email:true},
            consumer_country  : "required",
            consumer_city  : "required",
            consumer_full_address  : "required",
            cardname  : "required",
            cardnumber  : "required",
            expirationdate  : "required",
            securitycode  : "required",
        },
        errorPlacement: function(){
            return false;
        },
    });

});

function fixStepIndicator(n) {
    n=n-1;
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}

// Hide buttons according to the current step
hideButtons = function(current){
    var limit = parseInt(widget.length);

    $(".action").hide();

    if(current < limit) btnnext.show();
    if(current > 1) btnback.show();
    if (current == limit) {
        // Show entered values
        $(".display label.lbl").each(function(){
            if($(this).data("id") == "consumer_country"){
                $(this).html($("#"+$(this).data("id")+" option:selected").text());
            }
            else if($(this).data("id") == "consumer_city"){
                $(this).html($("#"+$(this).data("id")+" option:selected").text());
            }
            else if($("#"+$(this).data("id")).val() != ''){
                $(this).html($("#"+$(this).data("id")).val());
            }else{
                $(this).html($("#"+$(this).data("id")).text()+' '+currency);
            }
        });
        btnnext.hide();
        btnsubmit.show();
    }
}