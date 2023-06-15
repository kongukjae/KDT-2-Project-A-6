import React, {useState, useEffect, useRef} from 'react';
import './App.css';
import { count } from 'console';

class Header extends React.Component {
  render() {
    return (
      <div className="Header">
        유기견 모아보기
      </div>
    );
  }
}

interface propsTypeSearchBarCover {
  setTargetUrl:  React.Dispatch<React.SetStateAction<any[]>>;
  setDogList: React.Dispatch<React.SetStateAction<any[]>>;
}

function SearchBarCover(props : propsTypeSearchBarCover){
  const searchBar = useRef<HTMLInputElement>(null);
  useEffect(()=>{
    searchBar.current?.addEventListener('keyup',function(e){
      if(e.key==='Enter'){
        if(typeof(searchBar.current?.value)==='string'){
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



class FilterButtonCover extends React.Component {
  render() {
    return (
      <div className="FilterButtonCover">
        <FilterButton/>
        <FilterButton/>
        <FilterButton/>
        <div className='FilterEndGap'></div>
      </div>
    );
  }
}

class FilterButton extends React.Component {
  render() {
    return (
      <div className="FilterButton">
      </div>
    );
  }
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
}
function DogListCover(props:propsTypeDogListCover){
    const lastEnd = useRef<HTMLInputElement>(null);

    useEffect(()=>{
      fetch(`http://localhost:2080/listVer2?numOfRows=10&numOfPage=1`)
          .then(response => response.json())
          .then((result) =>{
            props.setDogList(result);
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

    const dogComponent : JSX.Element[] =props.dogList.map((currentDog, index)=> <DogListContent key={index} image={currentDog.imageLink} date={currentDog.date}  age={currentDog.age} location={currentDog.location} webLink={currentDog.webLink} breed={currentDog.breed}/>)
    return <div className="DogListCover">
        {dogComponent}
        <div className='IntersectionObserver' ref={lastEnd}></div>
      </div>
}

function RootWrap(){
  const [targetUrl, setTargetUrl] = useState<any[]>(['http://localhost:2080/listVer2?numOfRows=10&numOfPage=',''])
  const [dogList, setDogList] = useState<any[]>([])
  const changeDogList: React.Dispatch<React.SetStateAction<any[]>> = (value) => {
    setDogList(value);
  };
  const changeTargetUrl: React.Dispatch<React.SetStateAction<any[]>> = (value) => {
    setTargetUrl(value);
  };
  return <div className="Main">
    <Header />
    <SearchBarCover setTargetUrl={changeTargetUrl} setDogList={changeDogList}/>
    <FilterButtonCover/>
    <DogListCover setTargetUrl={changeTargetUrl} targetUrl={targetUrl} dogList={dogList} setDogList={changeDogList} />
  </div>
;
}

function App() {
  return (
    <RootWrap />
  );
}

export default App;
