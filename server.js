require('dotenv').config()

var app = require('./app/app');
var port = process.env.PORT;

var server = app.listen(port, function() {
  console.log('Express server listening on port ' + port);
});