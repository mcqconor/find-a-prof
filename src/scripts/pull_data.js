var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "professorswork"
  });
  
  con.connect(function(err) {
    if (err) throw err;
    con.query("SELECT * FROM professors WHERE profName = 'Matthew Lassiter'", function (err, results, fields){
      if (err) throw err;
      console.log(results);
    });
  });