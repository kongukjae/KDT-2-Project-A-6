const express = require('express'); 
const app = express();
const mysql      = require('mysql');
const connection = mysql.createConnection({
  host     : 'ls-414dd39cdb7215ba67853172200804032eca5c10.cjlhhn5kbuqa.ap-northeast-2.rds.amazonaws.com',
  user     : 'root',
  password : '00000000',
  database : 'dogListApi'
});

connection.connect();
app.get('/list', function (req, res) {
    let targetQuery = req.query;
    let column = ['date','location','idx','breed','age','dataFrom','numOfRows','numOfPage'];
    let targetKey = Object.keys(targetQuery);
    let selectQuery = 'SELECT * FROM dogList';
    let whereQuery = 'WHERE ';
    let whereFlag = false;
    let numOfRows = 0;
    let numOfPage = 0;
    let numOfRowsFlag = false;
    let numOfPageFlag = false;


    for(let i = 0; i<targetKey.length;i++){
        if(column.includes(targetKey[i])){

            console.log(targetKey[i],targetQuery[targetKey[i]])
            if(whereQuery.length>6){
                whereQuery += ' AND '
            }
            if(targetKey[i]==='idx'){
                whereFlag = true
                whereQuery += targetKey[i] + '='
                whereQuery += targetQuery[targetKey[i]]
            }else if(targetKey[i]==='numOfRows'){
                try{
                    numOfRows = Number(targetQuery[targetKey[i]]);
                    numOfRowsFlag = true;
                    if(numOfRows == NaN){
                        throw new Error('type Error')
                    }
                }catch(error){
                    console.log('typeErr');
                }
            }else if(targetKey[i]==='numOfPage'){
                try{
                    numOfPage = Number(targetQuery[targetKey[i]]);
                    numOfPageFlag = true;
                    if(numOfpage == NaN){
                        throw new Error('type Error')
                    }
                }catch(error){
                    console.log('typeErr');
                }
            }else{
                whereFlag = true
                whereQuery += targetKey[i] + '='
                whereQuery += '"'+targetQuery[targetKey[i]]+'"'
            }
        };
    }
    if(whereFlag){
        selectQuery += " " + whereQuery;
    };
    if(numOfRowsFlag && numOfPageFlag){
        selectQuery += " " + `LIMIT ${numOfPage * numOfRows - 1} , ${numOfRows}`;
    }else if(numOfPageFlag){
        selectQuery += " " + `LIMIT ${numOfPage * 1000 - 1} , 1000`;
    }else if(numOfRowsFlag){
        selectQuery += " " + `LIMIT ${numOfRows}`;
    }else{
        selectQuery += " " + "LIMIT 1000";
    }
    
    connection.query(selectQuery + ' ORDER BY date desc', (error, rows, fields) => {
        if (error) throw error;
        console.log(rows);
        res.send(JSON.stringify(rows)); 
    });

}); 
// connection.end();
app.listen(2080, function() {
    console.log('listening on 2080')
})