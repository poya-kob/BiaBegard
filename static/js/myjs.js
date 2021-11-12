$("#select_next").click(function () {
    $("#select_address").submit();
    return false;
});
$(document).ready(function () {
    var $ostan = $("#ostan");
    var $shahrestan = $("#shahrestan");
    var $shahr = $("#shahr");
    var $rosta = $("#rosta");
    var $shahrestanOptions = $shahrestan.find("option");
    var $shahrOptions = $shahr.find("option");
    var $rostaOptions = $rosta.find("option");
    $ostan.on('change', function () {
        var ostan_id = parseInt($(this).val());
        if (ostan_id > 0) {
            $shahrestanOptions.each(function (el) {
                if (parseInt($(this).data("ostanid")) === ostan_id) {
                    $(this).show();
                    var shahrestan_id = parseInt(($(this).val()))
                    $shahrOptions.each(function (elm) {
                        if (parseInt($(this).data("ostanid")) === ostan_id && parseInt($(this).data("shahrestanid")) === shahrestan_id)
                            $(this).show();
                        else
                            $(this).hide();
                    });
                    $rostaOptions.each(function (elm) {
                        if (parseInt($(this).data("ostanid")) === ostan_id && parseInt($(this).data("shahrestanid")) === shahrestan_id)
                            $(this).show();
                        else
                            $(this).hide();
                    });
                } else
                    $(this).hide();
            });
        } else {
            $shahrestanOptions.show();
        }
    }).trigger('change')
})