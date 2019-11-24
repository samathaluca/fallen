$(document).ready(function() {

    function initMaterialize() {
        $('.collapsible').collapsible();
        $('select').formSelect();
        $('.sidenav').sidenav();
        $('.datepicker').datepicker();
    }
    initMaterialize();
    
    document.getElementById("matfix").addEventListener("click", function(e) {
        e.stopPropagation();
    });


    // $('.datepicker').datepicker();
    // $('.datepicker').pickadate({
    //     selectMonths: true, // Creates a dropdown to control month
    //     selectYears: 15, // Creates a dropdown of 15 years to control year,
    //     today: 'Today',
    //     clear: 'Clear',
    //     close: 'Ok',
    //     closeOnSelect: false // Close upon selecting a date,
    // });

});