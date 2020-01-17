// This file includes the following necessary jquery to enable the Materialize javascript  included in the project to initialize.

$(document).ready(function() {
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
});
