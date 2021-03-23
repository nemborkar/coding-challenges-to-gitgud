(function(){
	'use strict'
	
	var handler = function(event){
		console.log(event);
		alert('This is working');
		return event;
	}

})();


var user = kintone.getLoginUser();
console.log(user);

// Sample response
// {
//   'id': '7',
//   'code': 'john-d',
//   'name': 'John Doe',
//   'email': 'johndoe@kintone.com',
//   'url': 'http://www.kintone.com',
//   'employeeNumber': '100',
//   'phone': '415-000-0000',
//   'mobilePhone': '400-000-0000',
//   'extensionNumber': '1001',
//   'timezone': 'America/Los_Angeles',
//   'isGuest': false
//   'language': 'en'
// }