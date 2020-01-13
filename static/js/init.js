// This file includes the following necessary jquery to enable the Materialize javascript  included in the project to initialize.



$(document).ready(function() {
			// function initMaterialize() {
				$('.collapsible').collapsible();
				$('select').formSelect();
				$('.sidenav').sidenav();
				$('.modal').modal();
				$('#alias').characterCounter();
				$(".datepicker").datepicker({
					yearRange: 15,
					autoClose: false,
					showClearBtn: true,
					i18n: {
						clear: "Clear",
						done: "Select",
						cancel: "Cancel"}
                });
            // }
});
// 			}

// $(document).ready(function() {

//     function initMaterialize() {
//         $('.collapsible').collapsible();
//         $('select').formSelect();
//         $('.sidenav').sidenav();
//         $('.modal').modal();
//         $('#alias').characterCounter();
//         $(".datepicker").datepicker({
//             yearRange: 15,
//             autoClose: false,
//             showClearBtn: true,
//             i18n: {
//                 clear: "Clear",
//                 done: "Select",
//                 cancel: "Cancel"
//             }
//         });
    // }
    // initMaterialize();
    
    // // document.getElementById("matfix").addEventListener("click", function(e) {
    // //     e.stopPropagation();
    // // });

