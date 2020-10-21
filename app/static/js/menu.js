

//for main menu
$(document).ready(function () {
	var isMenuOpen = false;

	$('#menu-btn1').click(function () {
		if (isMenuOpen == false) {
			$(".mainnav-wrap").clearQueue().animate({
				right: '0px'
			})
			$("#menu_back1").fadeIn('fast');
			$("#close-btn1").fadeIn(300);

			isMenuOpen = true;
		}
	});
	//bg
	$('#menu_back1').click(function () {
		if (isMenuOpen == true) {
			$(".mainnav-wrap").clearQueue().animate({
				right: '-250px'
			})
			$("body").clearQueue().animate({
				"margin-right": '0px'
			})
			$("#menu_back1").fadeOut('fast');
			$(this).fadeOut(200);

			isMenuOpen = false;
		}
	});
	//delbtn
	$('#close-btn1').click(function () {
		if (isMenuOpen == true) {
			$(".mainnav-wrap").clearQueue().animate({
				right: '-250px'
			})
			$("body").clearQueue().animate({
				"margin-right": '0px'
			})
			$("#menu_back1").fadeOut('fast');
			$(this).fadeOut(200);

			isMenuOpen = false;
		}
	});
	
});

//for member menu
$(document).ready(function () {
	var isMenuOpen = false;

	$('#menu-btn2').click(function () {
		if (isMenuOpen == false) {
			$(".navbar").clearQueue().animate({
				right: '0px'
			})
			$("#menu_back2").fadeIn('fast');
			$("#close-btn2").fadeIn(300);

			isMenuOpen = true;
		}
	});
	//bg
	$('#menu_back2').click(function () {
		if (isMenuOpen == true) {
			$(".navbar").clearQueue().animate({
				right: '-250px'
			})
			$("body").clearQueue().animate({
				"margin-right": '0px'
			})
			$("#menu_back2").fadeOut('fast');
			$(this).fadeOut(200);

			isMenuOpen = false;
		}
	});
		//delbtn
	$('#close-btn2').click(function () {
		if (isMenuOpen == true) {
			$(".navbar").clearQueue().animate({
				right: '-250px'
			})
			$("body").clearQueue().animate({
				"margin-right": '0px'
			})
			$("#menu_back2").fadeOut('fast');
			$(this).fadeOut(200);

			isMenuOpen = false;
		}
	});
});

//for submenu
function WinOnResize(){
	 if ( document.body.clientWidth < 766 ) {
		
		var curr = null;
		$('#mainnav ul>li>a').click(function(){
			if($(this).parent('li').index() != curr){	
				$('#mainnav .submenu').slideUp(500);
				$(this).next().stop(true,false).slideDown(500);
				curr = $(this).parent('li').index();
			}else{
				$(this).next().stop(true,false).slideUp(500);
				curr = null;
			}
		});
		
		  
	 } else {
		 
	 }
	 
 }
 window.onresize=WinOnResize
 window.onload=WinOnResize


//function WinOnResize(){
//	 if ( document.body.clientWidth > 680 ) {
//
//	 	$(document).on("scroll",function(){
//	 	    if($(document).scrollTop()>100){
//        $("header").removeClass("large").addClass("small");
//        } else{
//        $("header").removeClass("small").addClass("large");
//        }
//        });
//		  
//	 } else {
//		 
//		 $(document).on("scroll",function(){
//	 	    if($(document).scrollTop()>30){
//        $("header").removeClass("large").addClass("small");
//        } else{
//        $("header").removeClass("small").addClass("large");
//        }
//        });
//	 }
//	 
// }
// window.onresize=WinOnResize
// window.onload=WinOnResize
// 
//
//$(function(){
//	var $cart = $('header'),
//		_top = $cart.offset().top;
//	
//	var $win = $(window).scroll(function(){
//		if($win.scrollTop() >= _top){
//			if($cart.css('position')!='fixed'){
//				$cart.css({
//					position: 'fixed',
//					top: 0
//				});
//			}
//		}else{
//			$cart.css({
//				position: 'static'
//			});
//		}
//	});
//});