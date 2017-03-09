$(document).ready(function() {
    //alert("budget.js executed.");

    $(".categoryAmount").change(recalculateTotal);

    $("#incomeAmount").change(recalculateTotal);

});

function recalculateTotal() {
    var total = $("#incomeAmount").val();

    $(".categoryAmount").each(function(i) {
        total -= $(this).val();
    });

     $("#total").val(total);
};

