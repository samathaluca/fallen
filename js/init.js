$(document).ready(function() {

    function initMaterialize() {
        $('.collapsible').collapsible();
        $('select').formSelect();
        $('.sidenav').sidenav();
        $(".datepicker").datepicker({
            yearRange: 15,
            autoClose: false,
            showClearBtn: true,
            i18n: {
                clear: "Clear",
                done: "Select",
                cancel: "Cancel"
            }
        });
    }
    initMaterialize();
    
    document.getElementById("matfix").addEventListener("click", function(e) {
        e.stopPropagation();
    });

});