const express = require('express'); 
const cors = require('cors');
const path = require("path");
const fs = require('fs');
const app = express();
app.use(cors({
    origin: '*',
}));

app.use(express.static(path.join(__dirname, '../examplepage/build')));

app.get('/', function (req, res) {
  req.sendFile(path.join(__dirname, '../examplepage/build/index.html'));
});

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


const jsonFile = fs.readFileSync('./indexResult.json', 'utf8');
const searchIndex = JSON.parse(jsonFile);
console.log('index 불러오기 성공')
const clusterFile = fs.readFileSync('./clusterResult.json', 'utf8');
const clusterIndex = JSON.parse(clusterFile);
console.log('cluster 불러오기 성공')



const mysql      = require('mysql');
const connection = mysql.createConnection({
    host     : 'ls-414dd39cdb7215ba67853172200804032eca5c10.cjlhhn5kbuqa.ap-northeast-2.rds.amazonaws.com',
    user     : 'root',
    password : '00000000',
    database : 'dogListApi'
  });
connection.connect();
app.get('/image/:filename',function(req,res){
    res.sendFile( __dirname + '/images/instagram/' + req.params['filename'])
})
app.get('/listVer3', function (req, res) {
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
    let searchQuery = '';
    let andFlag = false;

    for(let i = 0; i<targetKey.length;i++){
        if(column.includes(targetKey[i])){

            // console.log(targetKey[i],targetQuery[targetKey[i]])
            if(andFlag){
                whereQuery += ' AND '
            }
            if(targetKey[i]==='idx'){
                andFlag = true;
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
                let targetIndex = clusterIndex[targetQuery[targetKey[i]]]
                whereFlag = true
                if(targetIndex===undefined){
                    whereQuery += 'idx=0'
                }else{
                    searchQuery += '( '
                    let targetIndexArray = []
                    console.log(targetIndex)
                    for(let i of targetIndex){
                        for(let j of searchIndex[i]){
                            if(!targetIndexArray.includes(j)){
                                targetIndexArray.push(j)

                            }
                        }
                    }
                    for(let i = 0;i<targetIndexArray.length - 1;i++){
                        searchQuery += `idx=${targetIndexArray[i]} OR `
                    }
                    searchQuery += `idx=${targetIndexArray[targetIndexArray.length-1]} )`
                    console.log(targetIndexArray);
                    whereQuery += searchQuery;
                }
            }else{
                andFlag = true;
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
        console.log('MySQL 조회 완료');
        res.send(JSON.stringify(rows)); 
    });

}); 


app.get('/listVer2', function (req, res) {
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
    let searchQuery = '';
    let andFlag = false;

    for(let i = 0; i<targetKey.length;i++){
        if(column.includes(targetKey[i])){

            // console.log(targetKey[i],targetQuery[targetKey[i]])
            if(andFlag){
                whereQuery += ' AND '
            }
            if(targetKey[i]==='idx'){
                andFlag = true;
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
                let targetIndex = searchIndex[targetQuery[targetKey[i]]]
                whereFlag = true
                if(targetIndex===undefined){
                    whereQuery += 'idx=0'
                }else{
                    searchQuery += '( '
                    for(let i = 0;i<targetIndex.length - 1;i++){
                        searchQuery += `idx=${targetIndex[i]} OR `
                    }
                    searchQuery += `idx=${targetIndex[targetIndex.length - 1]} )`
                    whereQuery += searchQuery;
                }
            }else{
                andFlag = true;
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
        console.log('MySQL 조회 완료');
        res.send(JSON.stringify(rows)); 
    });

}); 



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

            // console.log(targetKey[i],targetQuery[targetKey[i]])
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
        console.log('MySQL조회완료')
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