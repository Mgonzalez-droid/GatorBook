var mysql = require('mysql')
var fs = require('fs');

//Test database connection

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    insecureAuth : true,
    database: "gatorbookdb"
  });

  con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");

    //group database actions



    //var useGDB = "USING gatorbookdb"
    //var createTABLe = "CREATE table "

  var sql = "INSERT INTO Members (FirstName, LastName) VALUES?"

  var values = [
    ['John', 'Martin'],
    ['Thomas','Johnson'],
    ['James', 'Brown']

  ];

  con.query(sql, [values], function(err, result) {

    if (err) throw err;
    console.log("Number of records inserted: " + result.affectedRows);

  });








    //initialize database, work in progress...
    //var query = fs.readFileSync("database.sql").toString();
    //con.query(query, function(err, result, fields) {
    //    if(err) throw err;
    //    console.log(result)
    //});

  });
