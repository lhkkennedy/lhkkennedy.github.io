document.getElementById("parallax").onscroll = function() {myFunction()};
function myFunction() {
var currentScrollPos = document.getElementById('parallax').scrollTop;
var navbarColor = document.getElementById("navbtn");
var navbar = document.getElementById("navbar")
  if (currentScrollPos > 300 && currentScrollPos < 600) {
	navbar.style.transform = "translate3d(0, -100%, 0)";
  } else if (currentScrollPos > 600) {
	navbar.style.backgroundColor = "rgb(73 72 72)";
	navbar.style.transform = "translate3d(0, 0, 0)";
  } else {
	navbar.style.background = "none";
	navbar.style.transform = "translate3d(0, 0, 0)";
  }
}

(function(){
    // Slide In Panel - by CodyHouse.co
	var panelTriggers = document.getElementsByClassName('js-cd-panel-trigger');
	if( panelTriggers.length > 0 ) {
		for(var i = 0; i < panelTriggers.length; i++) {
			(function(i){
				var panelClass = 'js-cd-panel-'+panelTriggers[i].getAttribute('data-panel'),
					panel = document.getElementsByClassName(panelClass)[0];
				// open panel when clicking on trigger btn
				panelTriggers[i].addEventListener('click', function(event){
					event.preventDefault();
					addClass(panel, 'cd-panel--is-visible');
					document.getElementById('navbar').style.transform = "translate3d(0, -100%, 0)"
				});
				//close panel when clicking on 'x' or outside the panel
				panel.addEventListener('click', function(event){
					if( hasClass(event.target, 'js-cd-close') || hasClass(event.target, panelClass)) {
						event.preventDefault();
						removeClass(panel, 'cd-panel--is-visible');
						document.getElementById("navbar").style.transform = "translate3d(0, 0, 0)"
					}
				});
			})(i);
		}
	}
	
	//class manipulations - needed if classList is not supported
	//https://jaketrent.com/post/addremove-classes-raw-javascript/
	function hasClass(el, className) {
	  	if (el.classList) return el.classList.contains(className);
	  	else return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'));
	}
	function addClass(el, className) {
	 	if (el.classList) el.classList.add(className);
	 	else if (!hasClass(el, className)) el.className += " " + className;
	}
	function removeClass(el, className) {
	  	if (el.classList) el.classList.remove(className);
	  	else if (hasClass(el, className)) {
	    	var reg = new RegExp('(\\s|^)' + className + '(\\s|$)');
	    	el.className=el.className.replace(reg, ' ');
	  	}
	}
})();