$(document).ready(function() {
    //alert("budget.js executed.");

    $(".categoryAmount").change(function() {
        //alert("something changed");
        $("#total").val(recalculateTotal());
    });

});

function recalculateTotal() {
    var total = $("#incomeAmount").val();

    $(".categoryAmount").each(function(i) {
        total -= $(this).val();
    });

    return total;
};

