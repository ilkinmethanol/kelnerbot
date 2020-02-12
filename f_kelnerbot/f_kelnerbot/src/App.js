import React from 'react';
import './App.css';
import Meals from './components/Meals';
import MenuPanel from './components/MenuPanel';
import axios from 'axios';
import Orders from './components/Orders';
function App() {

  return (

    <div className="App">
    <MenuPanel></MenuPanel>
    <Meals></Meals>
    
    </div>
  );
}

export default App;
