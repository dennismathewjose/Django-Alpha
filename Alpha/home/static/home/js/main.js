$(function() {
	'use strict';

	
  $('.form-control').on('input', function() {
	  var $field = $(this).closest('.form-group');
	  if (this.value) {
	    $field.addClass('field--not-empty');
	  } else {
	    $field.removeClass('field--not-empty');
	  }
	});

});

var labelUsername = document.querySelector('#labelUsr');
var inputUsername = document.querySelector('#chat-username');
var callButton = document.querySelector('#callButton');

var username;
callButton.addEventListener('click', () => {
	username = inputUsername.value;
	if (username == ''){
		return;
	}
	inputUsername.value = '';
	inputUsername.disabled = true;
	inputUsername.style.visibility = 'hidden';

	callButton.disabled = true;
	callButton.style.visibility = 'hidden';

	var labelUsername = document.querySelector('#labelUsr');
	labelUsername.innerHTML = username;

});
