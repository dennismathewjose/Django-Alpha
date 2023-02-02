// $(function() {
// 	'use strict';	
//   $('.form-control').on('input', function() {
// 	  var $field = $(this).closest('.form-group');
// 	  if (this.value) {
// 	    $field.addClass('field--not-empty');
// 	  } else {
// 	    $field.removeClass('field--not-empty');
// 	  }
// 	});
// });

const usr_vdo = document.getElementById('user');
const remote_vdo = document.getElementById('remote');
const call_btn = document.getElementById('call');

var localstream = new MediaStream();

let rtcpeerconnection;
const created = "{{created}}";
const room = "{{room}}";
let isCreated;

const constraints = {
	'video' : true,
	'audio' : true
};

var loc = window.location;
console.log(loc);
var wsStart = 'ws://'

if (loc.protocol == 'https:'){
  wsStart = 'wss://'
}

var endPoint = wsStart + loc.host + loc.pathname;
console.log(endPoint);

webSocket = new WebSocket(endPoint);

webSocket.onopen = () =>{
  console.log('opened');
  webSocket.send(JSON.stringify({
	command : "join_room",
	room : room,
  }));

  if (created == 'created'){
	isCreated = true
	navigator.mediaDevices.getUserMedia(constraints)
		.then((stream) => {
	  		localstream = stream;
	  		usr_vdo.srcObject = localstream;
	  		usr_vdo.onloadeddata = () =>{
			usr_vdo.play();
	  		};
	});
	console.log(isCreated);
  }

  else{
	isCreated = false
	var userMedia = navigator.mediaDevices.getUserMedia(constraints)
	.then((stream) =>{
	  localstream = stream;
	  usr_vdo.srcObject = localstream;
	  usr_vdo.onloadeddata = () =>{
	  	usr_vdo.play();
	  };
	  webSocket.send(JSON.stringify({
		command: "join",
		room : room,
	  }));
	});
	// .catch(error =>{
	// 	console.log('Error accessing local video',error);
	// });
	console.log(isCreated);
  }
};
webSocket.onmessage = (e) => {
  const data = JSON.parse(e.data);
  console.log(data);
  if (data['command'] == 'join'){
	if (isCreated){
	call_btn.style.display = "block";
	}
  }
};

 
