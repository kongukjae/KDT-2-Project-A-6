let jin = document.getElementById('jin');
let cnt = 0;

setInterval(()=>{
  if(cnt%2===0){
    jin.style.color = 'blue'
  }else{
    jin.style.color = 'black'
  }
  cnt ++;
},500)