// gotop

$(document).ready(function(){

	// hide #back-top first
	$("#gotop").hide();
	
	// fade in #back-top
	$(function () {
		$(window).scroll(function () {
			if ($(this).scrollTop() > 100) {
				$('#gotop').fadeIn();
			} else {
				$('#gotop').fadeOut();
			}
		});

		// scroll body to 0px on click
		$('#gotop').click(function () {
			$('body,html').animate({
				scrollTop:0
			}, 800);
			return false;
		});
	});

});