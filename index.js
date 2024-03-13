const express = require('express');
var mysql = require('mysql');
const app = express();
const cors = require("cors");

const corsOptions = {
    origin: "http://localhost:4321"
}

app.use(express.json());
app.use(cors(corsOptions))

const port = process.env.PORT || 3000;

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "password",
    database: "professorswork"
  });


con.connect(err => {
   if (err) {
       console.error('Error connecting to database: ', err);
       return;
   }
   console.log('Connected to database.');
});

app.listen(port, () => {
    console.log("Server listening on PORT:",port);
});

app.get("/professors/school", (request, response) => {

    query_result = con.query(`SELECT id, profName, institution FROM professors`, (err,results) => {
        if (err){
            console.error('Query Error: ', err);
            response.status(500).json({error: 'Server Error'});
            return;
        } 
        response.send(results);
    });

});

app.get("/professors/id/:id", (request, response) => {

    query_result = con.query(`SELECT * FROM professors WHERE id = '${request.params['id']}'`, (err,results) => {
        if (err){
            console.error('Query Error: ', err);
            response.status(500).json({error: 'Server Error'});
            return;
        } 
        response.send(results);
    });

});

app.get("/school-list", (request, response) => {

    query_result = con.query(`SELECT DISTINCT institution FROM professors`, (err,results) => {
        if (err){
            console.error('Query Error: ', err);
            response.status(500).json({error: 'Server Error'});
            return;
        } 
        response.send(results);
    });

});