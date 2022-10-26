var mysql = require('mysql')
var fs = require('fs'); 

//Test database connection

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    insecureAuth : true
  });

  con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
    
    
    //initialize database, work in progress...
    //var query = fs.readFileSync("database.sql").toString();
    //con.query(query, function(err, result, fields) {
    //    if(err) throw err;
    //    console.log(result)
    //});

  });