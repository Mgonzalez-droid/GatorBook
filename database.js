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

/*

  var groupName = document.getElementById("gname").value  

  var searchForGName = "SELECT " + groupName +  "FROM groupList"  

  
  var useGDB = "USE gatorbookdb;"
  var createTable = "CREATE TABLE " + groupName + " ( Memberid int NOT NULL AUTO_INCREMENT, FirstName VARCHAR(255), LastName VARCHAR(255), PRIMARY KEY (Memberid))"
  
  con.query(useGDB, function(err, result) {
    if (err) throw err;
    console.log("action successful");
  });

  con.query(createTable, function(err, result) {
    if (err) throw err;
    console.log("action successful");
  });

  var insertGroup = "INSERT INTO groupListing (GroupName) VALUES?"
  
  //update groupList Table
  con.query(insertGroup, groupName, function(err, result) {
    if (err) throw err;
    console.log("Table has been updated. Number of records inserted: " + result.affectedRows);
  });


  

   

  //adding members to a group


  
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
*/

//Logic that handles checkbox options

/*$('input[type="checkbox"]').on('change', function() {
  $('input[type="checkbox"]').not(this).prop('checked', false);
})
*/






    //initialize database, work in progress...
    //var query = fs.readFileSync("database.sql").toString();
    //con.query(query, function(err, result, fields) {
    //    if(err) throw err;
    //    console.log(result)
    //});

  });
