import React, { useState } from 'react';

function HomePage() {
  return <h1>Home Page</h1>;
}

function AboutPage() {
  return <h1>About Page</h1>;
}

function ContactPage() {
  return <h1>Contact Page</h1>;
}

function App() {
  const [currentPage, setCurrentPage] = useState('home');

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <HomePage />;
      case 'about':
        return <AboutPage />;
      case 'contact':
        return <ContactPage />;
      default:
        return <HomePage />;
    }
  };

  return (
    <div>
      <nav>
        <ul>
          <li>
            <button onClick={() => setCurrentPage('home')}>Home</button>
          </li>
          <li>
            <button onClick={() => setCurrentPage('about')}>About</button>
          </li>
          <li>
            <button onClick={() => setCurrentPage('contact')}>Contact</button>
          </li>
        </ul>
      </nav>
      {renderPage()}
    </div>
  );
}

export default App;
