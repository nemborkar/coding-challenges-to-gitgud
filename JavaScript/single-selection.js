(function() {
    'use strict';
    var dept_selection = "department "; //Set the field code of the Department Selection field
    var error_message = 'Please select ONE department';
    
    var myEvent = ['app.record.create.submit', 'app.record.edit.submit', 'app.record.index.edit.submit'];
    kintone.events.on(myEvent, function(event) {
        // Get the User Selection field information
        var record = event.record;
        var selectedUsers = record[dept_selection]['value'];
        if (selectedUsers.length > 1) {
            // If more than one person is specified, set message to error property
            event.error = error_message;
            alert('Please select ONE department');
        }
        return event;
    });
})();


//-------------------------------------

(function() {
  'use strict';
  kintone.events.on('app.record.index.show', function(event) {
    
    console.log(event);
        alert('JS plugin is working');
        return event;
        
  });
})();
  
(function() {
    'use strict';
    var dept_selection = "department "; //Set the field code of the Department Selection field
    var error_message = 'Please select ONE department';
    
    var myEvent = ['app.record.create.submit', 'app.record.edit.submit', 'app.record.index.edit.submit'];
    kintone.events.on(myEvent, function(event) {
        // Get the User Selection field information
        var record = event.record;
        var selectedUsers = record[dept_selection]['value'];
        if (selectedUsers.length > 1) {
            // If more than one person is specified, set message to error property
            event.error = error_message;
            alert('Please select ONE department');
        }
        return event;
    });
})();