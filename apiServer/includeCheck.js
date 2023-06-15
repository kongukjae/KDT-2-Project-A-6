
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

console.log(includeCheck('asdasd123','123'))