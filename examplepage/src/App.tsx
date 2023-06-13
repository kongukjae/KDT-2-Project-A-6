import React, {useState, useEffect, useRef} from 'react';
import './App.css';

class Header extends React.Component {
  render() {
    return (
      <div className="Header">
        유기견 모아보기
      </div>
    );
  }
}
class SearchBarCover extends React.Component {
  render() {
    return (
      <div className="SearchBarCover">
        <input type='text' placeholder='검색' className='SearchBar'/>
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
interface propsType {
  date:string;
  age:string;
  location:string;
  image:string;
  webLink : string;
  breed : string
}

function DogListContent(props : propsType){
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

function DogListCover(){
    const [dogList, setDogList] = useState<any[]>([])
    const lastEnd = useRef<HTMLInputElement>(null);
    var numOfPage = 1
    // useEffect(()=>{
    //   // fetch('http://43.201.52.54:2080/list?numOfRows=4')
    //   fetch('http://localhost:2080/list?numOfRows=10')
    //     .then(response => response.json())
    //     .then((result) =>{
    //       setDogList(result);
    //       console.log(result)
    //       console.log('hi')

    //     });
    // },[]);
    function bringNewData(){
      fetch(`http://localhost:2080/list?numOfRows=5&numOfPage=${numOfPage}`)
        .then(response => response.json())
        .then((result) =>{
          setDogList((prev)=>[...prev, ...result]);
          numOfPage += 1;
          console.log(numOfPage)
        });
    }
    useEffect(()=>{
      const observer = new IntersectionObserver(bringNewData)
      if(lastEnd.current !== null){
        observer.observe(lastEnd.current)
      }
      return () => observer.disconnect()
    },[]);
    const dogComponent : JSX.Element[] = dogList.map((currentDog)=> <DogListContent image={currentDog.imageLink} date={currentDog.date}  age={currentDog.age} location={currentDog.location} webLink={currentDog.webLink} breed={currentDog.breed}/>)
    return <div className="DogListCover">
        {dogComponent}
        <div className='IntersectionObserver' ref={lastEnd}></div>
      </div>
}





function App() {
  return (
    <div className="Main">
      <Header />
      <SearchBarCover/>
      <FilterButtonCover/>
      <DogListCover />
    </div>
  );
}

export default App;
