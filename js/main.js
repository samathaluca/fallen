document.getElementById("matfix").addEventListener("click", function(e) {
	e.stopPropagation();
});

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, options);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.datepicker').datepicker();
  });

  $('.datepicker').pickadate({
            selectMonths: true, // Creates a dropdown to control month
            selectYears: 15, // Creates a dropdown of 15 years to control year,
            today: 'Today',
            clear: 'Clear',
            close: 'Ok',
            closeOnSelect: false // Close upon selecting a date,
    });

    
        <!-- $(document).ready(function(){
            $('.datepicker').datepicker();
         }); -->

        <!-- document.getElementById("matfix").addEventListener("click", function(e) {e.stopPropagation();
        }); -->