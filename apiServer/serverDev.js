const express = require('express'); 
const cors = require('cors');
const app = express();
app.use(cors({
    origin: '*',
}));

function includeCheck(targetText, keyWord){
    includeFlag = false
    targetTextArray = targetText.split('')
    keyWordArray = keyWord.split('')
    stackList = []
    for(let i of targetTextArray){
        if(i === keyWordArray[stackList.length]){
            stackList.push(i)
        }else{
            stackList = []
        }
        if(keyWordArray.length === stackList.length){
            includeFlag = true
            break

        }
    }
    return includeFlag
}

const mysql      = require('mysql');
const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '00000000',
  database : 'dogListApi'
});
connection.connect();
app.get('/image/:filename',function(req,res){
    res.sendFile( __dirname + '/images/instagram/' + req.params['filename'])
})

app.get('/list', function (req, res) {
    let targetQuery = req.query;
    let column = ['date','location','idx','breed','age','dataFrom','numOfRows','numOfPage','search'];
    let targetKey = Object.keys(targetQuery);
    let selectQuery = 'SELECT * FROM dogList';
    let whereQuery = 'WHERE ';
    let whereFlag = false;
    let numOfRows = 0;
    let numOfPage = 0;
    let numOfRowsFlag = false;
    let numOfPageFlag = false;
    let searchFlag = false;
    let searchKeyWord = '';


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
            }else if(targetKey[i]==='search'){
                searchFlag = true;
                searchKeyWord = targetQuery[targetKey[i]]
            }else{
                whereFlag = true;
                whereQuery += targetKey[i] + '=';
                whereQuery += '"'+targetQuery[targetKey[i]]+'"';
            }
        };
    }
    if(whereFlag){
        selectQuery += " " + whereQuery;
    };
    selectQuery += ' ORDER BY date desc'
    if(numOfRowsFlag && numOfPageFlag){
        selectQuery += " " + `LIMIT ${numOfPage * numOfRows - 1} , ${numOfRows}`;
    }else if(numOfPageFlag){
        selectQuery += " " + `LIMIT ${numOfPage * 1000 - 1} , 1000`;
    }else if(numOfRowsFlag){
        selectQuery += " " + `LIMIT ${numOfRows}`;
    }else{
        selectQuery += " " + "LIMIT 1000";
    } 
    
    connection.query(selectQuery, (error, rows, fields) => {
        if (error) throw error;
        console.log(rows);
        if(searchFlag){
            let checkList = [];
            // let roopFlag = false
            for(let i of rows){
                for(let j of Object.values(i)){
                    if(includeCheck(String(j),searchKeyWord)){
                        // roopFlag = true;
                        checkList.push(i);
                        break
                    }
                }
                // if(roopFlag){
                //     break
                // }
            }
            res.send(JSON.stringify(checkList)); 
        }else{
            res.send(JSON.stringify(rows)); 
        }
        
    });

}); 
// connection.end();
app.listen(2080, function() {
    console.log('listening on 2080')
})