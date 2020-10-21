
//bannner
var swiper1 = new Swiper('#banner', {
   pagination: '.sp1',
   paginationClickable: true,
   autoplay:4000,
   speed: 900,
   spaceBetween: 10,
   autoplayDisableOnInteraction:false
}); 

// three category
var swiper2 = new Swiper('.threecate', {
	pagination: '.sp2',
	paginationClickable: true,
	slidesPerView: 'auto',
	spaceBetween: 11,
	freeMode: true,
	breakpoints: {
		480: {
		  slidesPerView: 2.5,
		  spaceBetween: 8,
		  slidesPerGroup:2.5
		},
		767: {
		  slidesPerView: 3,
		},
		1000: {
		  slidesPerView: 4.5,
		},
		1020: {
		  slidesPerView: 5,
		}
	}
});


// hot books
var swiper3 = new Swiper('.hotbook', {
	pagination: '.sp3',
	paginationClickable: true,
	slidesPerView: 2,
	slidesPerGroup:2,
	spaceBetween: 12,
	freeMode: true,
	breakpoints: {
		480: {
		  slidesPerView: 1.5,
		  slidesPerGroup:1.5,
		  spaceBetween: 8
		},
	}
});


// msg
var swiper4 = new Swiper('.message', {
	pagination: '.sp4',
	paginationClickable: true,
	slidesPerView: 1,
	spaceBetween: 5,
});


$('.swiper-slide a').click(function() { window.location.href = $(this).attr("href"); });