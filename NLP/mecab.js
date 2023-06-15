let mecab = require('mecab-ya');
let text = '해운대구는 대구가 아니다.';

function returnNoun(text,cb){
    let resultArray = []
    mecab.pos(text, (err, result) => {
        for(let i of result){
            if(i[1][0]==='N'){
                resultArray.push(i[0])
            }
        }
        cb(resultArray)
    });    
}

returnNoun(text,(i)=>{console.log(i)})

// mecab.morphs(text, (err, result) => {
//     console.log('morphs : ', result);
// });

// console.log('nouns : ', mecab.nounsSync(text));