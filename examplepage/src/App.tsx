import React, {useState, useEffect, useRef} from 'react';
import './App.css';
import { count } from 'console';

function Header(){
    const header = useRef<HTMLInputElement>(null);
    useEffect(()=>{
      header.current?.addEventListener('click',()=>{
        window.location.reload();
      })
    },[])
    return <div className="Header" ref={header}>
        유기견 검색엔진
      </div>
   
}

interface propsTypeSearchBarCover {
  setTargetUrl:  React.Dispatch<React.SetStateAction<any[]>>;
  setDogList: React.Dispatch<React.SetStateAction<any[]>>;
  setMoreInfoButtonFirstTime: React.Dispatch<React.SetStateAction<any>>;
}

function SearchBarCover(props : propsTypeSearchBarCover){
  const searchBar = useRef<HTMLInputElement>(null);
  useEffect(()=>{
    searchBar.current?.addEventListener('keyup',function(e){
      if(e.key==='Enter'){
        if(typeof(searchBar.current?.value)==='string'){
          props.setMoreInfoButtonFirstTime(true);
          let searchKey = searchBar.current.value;
          props.setTargetUrl(['http://localhost:2080/listVer2?numOfRows=10&numOfPage=',`&search=${searchKey}`])
          console.log('search :' + searchBar.current?.value)
          fetch(`http://localhost:2080/listVer2?numOfRows=10&numOfPage=1&search=${searchKey}`)
          .then(response => response.json())
          .then((result) =>{
            props.setDogList(result);
          });
        }else{
          alert('유효한 값을 입력해주세요')
        }
      }
    }
    )
    // props.search('123')  
  },[])
  
  return <div className="SearchBarCover">
  <input type='text' placeholder='검색' className='SearchBar' ref={searchBar}/>
</div>
;
}


interface propsTypedogListContent {
  date:string;
  age:string;
  location:string;
  image:string;
  webLink : string;
  breed : string
}

function DogListContent(props : propsTypedogListContent){
  const imageDiv = useRef<HTMLInputElement>(null);
  const moveToLink = () => {
    window.open(props.webLink);
  };
  useEffect(()=>{
    if(imageDiv.current !== null){
      imageDiv.current.style.backgroundImage = `url(${props.image})`
    }
  },[props]);
  return <div className="DogListContent" onClick={moveToLink}>
    <div className='DogListContentImage' ref={imageDiv}></div>
    <div className = 'DogListContentWirteWrap'>
      <div className='DogListContentWrite'>{props.breed}</div>
      <div className='DogListContentWrite'>{props.age}</div>
      <div className='DogListContentWrite'>{props.location}</div>
      <div className='DogListContentDate'>{props.date.slice(0,10)}</div>
    </div>
  </div>
;
}

interface propsTypeDogListCover {
  setTargetUrl:  React.Dispatch<React.SetStateAction<any[]>>;
  targetUrl:any[];
  dogList:any[];
  setDogList: React.Dispatch<React.SetStateAction<any[]>>;
  setMoreInfoButtonFirstTime: React.Dispatch<React.SetStateAction<any>>;
  moreInfoButtonFirstTime: boolean;
}
function DogListCover(props:propsTypeDogListCover){
    const lastEnd = useRef<HTMLInputElement>(null);
    const [moreInfoButton,setMoreInfoButton] = useState(false)
    


    useEffect(()=>{
      let url : any = props.targetUrl[0] + '1'
      fetch(url)
          .then(response => response.json())
          .then((result) =>{
            props.setDogList(result);
            if(result.length === 0){
              setMoreInfoButton(true)
            }
          });
    },[])
    useEffect(()=>{
      let numOfPage = 2;
      function bringNewData(entries: IntersectionObserverEntry[]):void{

        const entry = entries.find((entry) => entry.isIntersecting);
        if(entry){
          let url = props.targetUrl[0] + numOfPage + props.targetUrl[1]
          console.log(url)
          fetch(url)
            .then(response => response.json())
            .then((result) =>{
              props.setDogList((prev) => [...prev, ...result]);
              if(result.length === 0){
                setMoreInfoButton(true)
              }
            });
          console.log(numOfPage)
          console.log(props.targetUrl)
          numOfPage += 1;
        }
      }
      

      const observer = new IntersectionObserver((entries)=>{bringNewData(entries)})
      if(lastEnd.current !== null){
        observer.observe(lastEnd.current)
      }
      return () => observer.disconnect()
    },[props.targetUrl])
    const moreInfoClick = () => {
      let searchQuery = props.targetUrl[1]
      props.setMoreInfoButtonFirstTime(false)
      console.log(searchQuery)
      fetch('http://localhost:2080/listVer3?numOfRows=10&numOfPage=1' + searchQuery)
            .then(response => response.json())
            .then((result) =>{
              props.setDogList((prev) => [...prev, ...result]);
              if(result.length === 0){
                setMoreInfoButton(true)
              }
            });
      props.setTargetUrl(['http://localhost:2080/listVer3?numOfRows=10&numOfPage=',searchQuery])
      setMoreInfoButton(false)
    };

    const dogComponent : JSX.Element[] =props.dogList.map((currentDog, index)=> <DogListContent key={index} image={currentDog.imageLink} date={currentDog.date}  age={currentDog.age} location={currentDog.location} webLink={currentDog.webLink} breed={currentDog.breed}/>)
    return <div className="DogListCover">
        {dogComponent}
        { moreInfoButton && props.moreInfoButtonFirstTime ? <div className='moreInfoButton' onClick={moreInfoClick}>더 많은 검색 결과 보기</div> : null }
        <div className='IntersectionObserver' ref={lastEnd}></div>
      </div>
}

function RootWrap(){
  const [targetUrl, setTargetUrl] = useState<any[]>(['http://localhost:2080/listVer2?numOfRows=10&numOfPage=',''])
  const [dogList, setDogList] = useState<any[]>([])
  const [moreInfoButtonFirstTime,setMoreInfoButtonFirstTime] = useState(true)
  const changeDogList: React.Dispatch<React.SetStateAction<any[]>> = (value) => {
    setDogList(value);
  };
  const changeTargetUrl: React.Dispatch<React.SetStateAction<any[]>> = (value) => {
    setTargetUrl(value);
  };
  const changeMoreInfoButtonFirstTime: React.Dispatch<React.SetStateAction<any>> = (value) => {
    setMoreInfoButtonFirstTime(value);
  };
  return <div className="Main">
    <Header />
    <SearchBarCover setTargetUrl={changeTargetUrl} setDogList={changeDogList} setMoreInfoButtonFirstTime={changeMoreInfoButtonFirstTime}/>
    <DogListCover setTargetUrl={changeTargetUrl} targetUrl={targetUrl} dogList={dogList} setDogList={changeDogList} setMoreInfoButtonFirstTime={changeMoreInfoButtonFirstTime} moreInfoButtonFirstTime={moreInfoButtonFirstTime}/>
  </div>
;
}

function App() {
  return (
    <RootWrap />
  );
}

export default App;
