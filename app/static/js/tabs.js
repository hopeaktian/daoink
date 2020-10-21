// for tabs

$(function(){
	  var _showTab = 0;
	  $('.fortabs').each(function(){
		  var $tab = $(this);
		  var $defaultLi = $('ul.tabs li', $tab).eq(_showTab).addClass('active');
		  $($defaultLi.find('a').attr('href')).siblings().hide();
		  $('ul.tabs li', $tab).click(function() {
			  var $this = $(this),
				  _clickTab = $this.find('a').attr('href');
			  $this.addClass('active').siblings('.active').removeClass('active');
			  $(_clickTab).stop(false, true).fadeIn().siblings().hide();

			  return false;
		  }).find('a').focus(function(){
			  this.blur();
		  });
	  });
  });
  
//random
$(function() {
	$(".radomtab .tabs li").eq(Math.floor(Math.random()*$('.fortabs .tabs li').length)).click();
});