// Simple Express web server.

// Load the express module.
var express = require('express');
var app = express();

// Respond to requests for / with 'Hello World'.
app.get('/', function(req, res){
    res.send('Hello World!');
});

// Listen on port 3000 (non-privileged port).
app.listen(3000, () => console.log('Express server started successfully on port 3000.'));