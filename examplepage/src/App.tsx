import React, {useState, useEffect, useRef} from 'react';
import './App.css';

function RootWrap(){
  const [targetUrl, setTargetUrl] = useState<string>('')
  const [dogList, setDogList] = useState<any[]>([])
  const changeDogList: React.Dispatch<React.SetStateAction<any[]>> = (value) => {
    setDogList(value);
  };
  const changeSearch = (value:string):void => {
    setTargetUrl(value);
    return;
  };
  return <div className="Main">
    <Header />
    <SearchBarCover search={changeSearch} setDogList={changeDogList}/>
    <FilterButtonCover/>
    <DogListCover search={targetUrl} dogList={dogList} setDogList={changeDogList} />
  </div>
;
}

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
  search: (value: string) => void;
  setDogList: React.Dispatch<React.SetStateAction<any[]>>;
}
function SearchBarCover(props : propsTypeSearchBarCover){
  const searchBar = useRef<HTMLInputElement>(null);
  useEffect(()=>{
    searchBar.current?.addEventListener('keyup',function(e){
      if(e.key==='Enter'){
        if(typeof(searchBar.current?.value)==='string'){
          props.search(searchBar.current?.value)
          console.log('search :' + searchBar.current?.value)
          fetch(`http://localhost:2080/list?numOfRows=100&numOfPage=1&search=${props.search}`)
          .then(response => response.json())
          .then((result) =>{
            props.setDogList((prev) => [...result]);
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
class FilterButton extends React.Component {
  render() {
    return (
      <div className="FilterButton">
      </div>
    );
  }
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
  useEffect(()=>{
    if(imageDiv.current !== null){
      imageDiv.current.style.backgroundImage = `url(${props.image})`
      imageDiv.current.addEventListener('click',()=>{
        window.open(props.webLink)
      })
    }
  });
  return <div className="DogListContent">
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
  search:string;
  dogList:any[];
  setDogList: React.Dispatch<React.SetStateAction<any[]>>;
}
function DogListCover(props:propsTypeDogListCover){

    const lastEnd = useRef<HTMLInputElement>(null);
    var numOfPage = 1
    let urlResult = `http://localhost:2080/list?numOfRows=5&numOfPage=${numOfPage}`

    useEffect(()=>{
      function bringNewData(url:string):void{
        numOfPage += 1;
        if(props.search !== ''){
          urlResult = `http://localhost:2080/list?numOfRows=100&numOfPage=${numOfPage}&search=${props.search}`
        }else{
          urlResult = `http://localhost:2080/list?numOfRows=5&numOfPage=${numOfPage}`
        }
        console.log(props.search)
        console.log(url)
        fetch(url)
          .then(response => response.json())
          .then((result) =>{
            props.setDogList((prev) => [...prev, ...result]);
            console.log(numOfPage)     
          });
      }
      const observer = new IntersectionObserver(()=>{bringNewData(urlResult)})
      if(lastEnd.current !== null){
        observer.observe(lastEnd.current)
      }
      // return () => observer.disconnect()
    },[props.search]);
    const dogComponent : JSX.Element[] =props.dogList.map((currentDog)=> <DogListContent image={currentDog.imageLink} date={currentDog.date}  age={currentDog.age} location={currentDog.location} webLink={currentDog.webLink} breed={currentDog.breed}/>)
    return <div className="DogListCover">
        {dogComponent}
        <div className='IntersectionObserver' ref={lastEnd}></div>
      </div>
}





function App() {
  return (
    <RootWrap />
  );
}

export default App;
