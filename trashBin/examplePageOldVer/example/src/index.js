import React, {useEffect, useState} from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

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
function DogListContent(props){
  return <div className="DogListContent">
    <div className='DogListContentImage'></div>
    <div className='DogListContentWrite'>{props.date},{props.age},{props.location}</div>
  </div>
;
}

function DogListCover(){
    useEffect(()=>{
      setTimeout(()=>{
        console.log('hi')
      },1000)
    },[]);

    return <div className="DogListCover">
        <DogListContent image='image1' date='date1' age='age1' location='location1' />
        <DogListContent image='image2' date='date2' age='age2' location='location2' />
        <DogListContent image='image3' date='date3' age='age3' location='location3' />
        <DogListContent image='image4' date='date4' age='age4' location='location4' />
      </div>
}


  
  class Main extends React.Component {
    render() {
      return (
        <div className="Main">
          <Header />
          <SearchBarCover/>
          <FilterButtonCover/>
          <DogListCover />
        </div>
      );
    }
  }
  
  // ========================================
  
  const root = ReactDOM.createRoot(document.getElementById("root"));
  root.render(<Main />);
  