(function() {
  'use strict';
  kintone.events.on('app.record.index.show', function(event) {
    
    console.log(event);
    alert("Page is loading");
    
  });
})();
