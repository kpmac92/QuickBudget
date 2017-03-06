$(document).ready(function() {
    //alert("budget.js executed.");

    $(".categoryAmount").change(function() {
        //alert("something changed");
        $("#total").val($(this).val());
    });

});

