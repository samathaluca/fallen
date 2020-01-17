// This file includes the necessary JQuery to enable the Materialize javascript components in the project to initialize.

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
